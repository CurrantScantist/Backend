from server.database.connect import DatabaseConnection
import os
from dotenv import load_dotenv
import json

"""
Retrieve techstack and techstack data from the mongodb database
"""
# Connecting to MongoDB and getting the database test_db with the collection name repositories
load_dotenv()
PASSWORD = os.getenv('PASSWORD')
USERNAME = os.getenv('NAME')
CONNECTION_STRING = f"mongodb+srv://{USERNAME}:" \
                    f"{PASSWORD}@cluster0.vao3k.mongodb.net/test_db?retryWrites=true&w=majority&ssl=true" \
                    f"&ssl_cert_reqs=CERT_NONE"
database = DatabaseConnection(CONNECTION_STRING)
database.connection_to_db("test_db")
techstack_collection = database.database_name.get_collection("repositories")


# helpers

def techstack_helper(techstack: dict) -> dict:
    """
    Helps retrieve_techstack return techstack metadata in dictionary form.
    :param techstack: techstack object from database
    :return: techstack metadata in an ordered dictionary format
    """
    techstack["id"] = str(techstack["_id"])
    del techstack["_id"]
    return techstack


def techstack_helper_important_info(techstack) -> dict:
    '''
    Helps retrieve only id, name, and owner of a techstack in dictionary format.
    :param techstack: techstack object from database
    :return: given techstack's id, name and owner.
    '''
    return {
        "id": str(techstack["_id"]),
        "name": techstack["name"],
        "owner": techstack["owner"],
        "stargazers_count": techstack["stargazers_count"],
        "topics": techstack["topics"],
        "forks": techstack["forks"],
        # "releases": techstack["releases"],
    }


async def retrieve_techstacks():
    '''
    Retrieve all unique techstacks in the database
    :return: all techstacks present in the database
    '''
    
    techstacks = []
    async for techstack in techstack_collection.find():
        techstacks.append(techstack_helper(techstack))
    return techstacks


async def retrieve_techstack(name: str, owner: str) -> dict:
    '''
    Retrieve a specific techstack and its metadata, from the database with matching name and owner
    :param name: name attribute of the techstack
    :param owner: owner attribute of the techstack
    :return: Call techstack_helper() on the given techstack, which returns its respective metadata
    '''
    techstack = await techstack_collection.find_one({"name": name, "owner": owner})
    if techstack:
        return techstack_helper(techstack)


async def retrieve_techstack_important_info() -> dict:
    '''
    Retrieve all techstack repo detail with few information (Id, name and owner)
    :return: Call retrieve_techstack_important_info() on the given techstack, which returns its techstack id, name, 
    owner and imortant information.
    '''

    techstacks_important_info = []
    async for techstack in techstack_collection.find({}, {"_id": 1, "name": 1, "owner": 1, "stargazers_count": 1, "topics":1, "forks": 1}):
        techstacks_important_info.append(techstack_helper(techstack))
    return techstacks_important_info


async def retrieve_techstack_contribution_data(name: str, owner: str) -> dict:
    '''
    Retrieve all techstack repo contribution and collaboration detail with few information (Id, name and owner)
    :return: Call retrieve_techstack_contribution_data() on the given techstack, which returns its techstack id, name, 
    owner and commit/ contribution data in object format.
    '''

    techstack = await techstack_collection.find_one({"name": name, "owner": owner},
                                                    {"_id": 1, "name": 1, "owner": 1, "commits_per_author": 1})
    if techstack:
        return techstack_helper(techstack)
    else:
        return None


async def retrieve_top_ten_techstacks() -> dict:
    """
    Retrieve the top ten techstacks from the database based on highest to lowest stargazer count
    :return: top 10 techstacks and their full metadata
    """
    techstacks = []
    async for techstack in techstack_collection.find({},{"_id":0}).sort([('stargazers_count', -1)]).limit(10):
        techstacks.append(techstack)

    return techstacks


async def retrieve_similar_repository_data(name: str, owner: str, num_repositories=5) -> list:
    """
    Retrieves up to 5 repositories that are similar to an inputted repository (the inputted repository is guaranteed
    to be one of the 5 repositories). For repositories that have github topics, two repositories are considered similar
    if they have at least one tag in common. For repositories that don't have github topics, repositories that share the
    same predominant language are considered similar. In the case when there are more than 4 repositories that are
    similar to the inputted repository, the most popular 4 are returned (measured based on the stargazers_count).
    :param name: the name of the repository
    :param owner: the owner of the repository
    :param num_repositories: the maximum number of repositories to include in the response
    :return: the response model for successful requests otherwise a HTTPException is raised
    """
    input_repo = await techstack_collection.find_one({"name": name, "owner": owner},
                                                     {"topics": 1, "_id": 0, "num_components": 1,
                                                      "num_vulnerabilities": 1, "size": 1, "language": 1})
    if input_repo is None:
        return []
    try:
        original_topics = input_repo["topics"]
        topics = original_topics.copy()
        if input_repo["language"].lower() in topics:
            topics.remove(input_repo["language"].lower())
    except KeyError:
        return []

    repo = {"name": name, "owner": owner}
    original_topics_set = set(original_topics)
    repo.update(input_repo)
    repo["common_topics"] = repo.pop("topics")
    repo["common_language"] = repo.pop("language")
    repos = [repo]

    async def process_repos(similar_repos):
        """
        Local function to process the pymongo cursor for repositories
        """
        processed_repos = []
        async for repo in similar_repos:
            repo.update({"common_topics": original_topics_set.intersection(set(repo["topics"]))})
            repo["common_language"] = None
            if repo["language"] == input_repo["language"]:
                repo["common_language"] = repo["language"]

            repo.pop("topics")
            processed_repos.append(repo)
        return processed_repos

    if len(topics) != 0:
        similar_repos = techstack_collection.find({"name": {"$ne": name}, "topics": {"$in": topics}},
                                                  {"name": 1, "owner": 1, "_id": 0,
                                                   "num_components": 1, "num_vulnerabilities": 1, "size": 1,
                                                   "topics": 1,
                                                   "language": 1}) \
            .sort([('stargazers_count', -1)]).limit(num_repositories - 1)

        repos += await process_repos(similar_repos)

    # if not enough repositories were found using github topics, find repos that have the same main language
    num_repositories_to_find = num_repositories - len(repos)
    if num_repositories_to_find == 0:
        return repos

    similar_language_repos = techstack_collection.find({"name": {"$ne": name}, "language": input_repo["language"]},
                                                       {"name": 1, "owner": 1, "_id": 0,
                                                        "num_components": 1, "num_vulnerabilities": 1, "size": 1,
                                                        "topics": 1,
                                                        "language": 1}) \
        .sort([('stargazers_count', -1)]).limit(num_repositories_to_find)

    repos += await process_repos(similar_language_repos)

    return repos


async def retrieve_nodelink_data(name: str, owner: str) -> list:
    """
    Retrieve nodelink data informnation from the database
    :param name: name of repository
    :param owner: name of repository owner
    :return: nodelink_info from the database
    """
    techstack_nodelink_info = await techstack_collection.find_one({"name": name, "owner": owner},
                                                                  {"_id": 0, "name": 1, "owner": 1, "nodelink_data": 1})
    return techstack_nodelink_info


async def retrieve_techstack_heatmap(name: str, owner: str) -> dict:
    """
    Retrieve techstack information for heatmap (No of Commits, Open Issues, Pull Requests)
    :return: the response model for successful requests having heatmap information otherwise a HTTPException is raised
    """

    techstack_heatmap_info = await techstack_collection.find_one({"name": name, "owner": owner}, {"_id": 1, "name": 1, "owner": 1, "heatmap_data": 1 })
    if techstack_heatmap_info:
        return techstack_helper(techstack_heatmap_info)
    else: 
        return None
