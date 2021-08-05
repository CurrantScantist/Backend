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
    return {
        "id": str(techstack["_id"]),
        "name": techstack["name"],
        "owner": techstack["owner"],
        # "releases": techstack["releases"],
    }
    
# Retrieve all techstacks present in the database
async def retrieve_techstacks():
    techstacks = []
    async for techstack in techstack_collection.find():
        techstacks.append(techstack_helper(techstack))
    print(techstacks)
    return techstacks


# Retrieve a techstack with a matching ID
async def retrieve_techstack(name: str, owner:str) -> dict:

    techstack = await techstack_collection.find_one({"name": name, "owner": owner})
    if techstack:
        return techstack_helper(techstack)


# Retrieve all techstack repo detail with few information (Id, name and owner)
async def retrieve_techstack_name() -> dict:
    techstacks_name = []
    async for techstack in techstack_collection.find():
        techstacks_name.append(techstack_helper_name(techstack))
    print(techstacks_name)
    return techstacks_name

