from server.database.connect import DatabaseConnection
import os
from dotenv import load_dotenv
import json

"""
Retrieve techstack and techstack data from the mongodb database
"""
# Connecting to MongoDB and getting the database test_db with the collection name repositories
load_dotenv()
PASSWORD=os.getenv('PASSWORD')
USERNAME=os.getenv('NAME')
CONNECTION_STRING=f"mongodb+srv://{USERNAME}:{PASSWORD}@cluster0.vao3k.mongodb.net/test_db?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
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
    techstack["id"] =str(techstack["_id"])
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


async def retrieve_techstack_important_info() -> dict:
    '''
    Retrieve all techstack repo detail with few information (Id, name and owner)
    :return: Call retrieve_techstack_important_info() on the given techstack, which returns its techstack id, name, 
    owner and imortant information.
    '''
    
    techstacks_important_info = []
    async for techstack in techstack_collection.find():
        techstacks_important_info.append(techstack_helper_important_info(techstack))
    return techstacks_important_info



async def retrieve_techstack_contribution_data(name: str, owner:str) -> dict:
    '''
    Retrieve all techstack repo contribution and collaboration detail with few information (Id, name and owner)
    :return: Call retrieve_techstack_contribution_data() on the given techstack, which returns its techstack id, name, 
    owner and commit/ contribution data in object format.
    '''
    
    techstack = await techstack_collection.find_one({"name": name, "owner": owner}, {"_id": 1, "name": 1, "owner": 1, "commits_per_author": 1 })
    if techstack:
        return techstack_helper(techstack)
    else: 
        return None