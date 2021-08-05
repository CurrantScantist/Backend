from server.database.connect import DatabaseConnection
import os
from dotenv import load_dotenv

"""
Retrieve techstack and techstack data from the mongodb database
"""
# Connecting to MongoDB and getting the database test_db with the collection name repositories
load_dotenv()
CONNECTION_STRING=os.getenv('CONNECTION_STRING')
database = DatabaseConnection(CONNECTION_STRING)
database.connection_to_db("test_db")
techstack_collection = database.database_name.get_collection("repositories")


# helpers

def techstack_helper(techstack) -> dict:
    """
    Helps retrieve_techstack return techstack metadata in dictionary form.
    :param techstack: techstack object from database
    :return: techstack metadata in an ordered dictionary format
    """
    return {
        "id": str(techstack["_id"]),
        # "releases": techstack["releases"],
        "name": techstack["name"],
        "owner": techstack["owner"],
        "description": techstack["description"],
        "forks": techstack["forks"],
        "forks_count": techstack["forks_count"],
        "language": techstack["language"],
        "stargazers_count": techstack["stargazers_count"],
        "watchers_count": techstack["watchers_count"],
        "watchers": techstack["watchers"],
        "size": techstack["size"],
        "default_branch": techstack["default_branch"],
        "open_issues_count": techstack["open_issues_count"],
        "open_issues": techstack["open_issues"],
        "has_issues": techstack["has_issues"],
        "archived": techstack["archived"],
        "disabled": techstack["disabled"],
        "pushed_at": techstack["pushed_at"],
        "created_at": techstack["created_at"],
        "updated_at": techstack["updated_at"],
        "languages": techstack["languages"],
        "topics": techstack["topics"],
    }
def techstack_helper_name(techstack) -> dict:
    '''
    Helps retrieve only id, name, and owner of a techstack in dictionary format.
    :param techstack: techstack object from database
    :return: given techstack's id, name and owner.
    '''
    return {
        "id": str(techstack["_id"]),
        "name": techstack["name"],
        "owner": techstack["owner"],
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
    print(techstacks)
    return techstacks


async def retrieve_techstack(name: str, owner:str) -> dict:
    '''
    Retrieve a specific techstack and its metadata, from the database with matching name and owner
    :param name: name attribute of the techstack
    :param owner: owner attribute of the techstack
    :return: Call techstack_helper() on the given techstack, which returns its respective metadata
    '''
    techstack = await techstack_collection.find_one({"name": name, "owner": owner})
    if techstack:
        return techstack_helper(techstack)


async def retrieve_techstack_name() -> dict:
    '''
    Retrieve all techstack repo detail with few information (Id, name and owner)
    :return: Call techstack_helper_name() on the given techstack, which returns its techstack id, name and owner.
    '''
    
    techstacks_name = []
    async for techstack in techstack_collection.find():
        techstacks_name.append(techstack_helper_name(techstack))
    print(techstacks_name)
    return techstacks_name

