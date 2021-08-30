from server.database.connect import DatabaseConnection
import os
from dotenv import load_dotenv

"""
Retrieve sca_data and sca_data data from the mongodb database
"""
# Connecting to MongoDB and getting the database test_db with the collection name sca_data
load_dotenv()
CONNECTION_STRING=os.getenv('CONNECTION_STRING')
database = DatabaseConnection(CONNECTION_STRING)
database.connection_to_db("test_db")
sca_data_collection = database.database_name.get_collection("sca_data")

# helpers

def sca_data_helper(sca_data) -> dict:
    """
    Helps retrieve_sca_data return sca_data in dictionary form.
    :param sca_data: sca_data object from database
    :return: sca_data in an ordered dictionary format
    """
    return {
        "id": str(sca_data["_id"]),
        "name": sca_data["name"],
        "owner": sca_data["owner"],
        "tag_name": sca_data["tag_name"],
        "results": sca_data["results"],
        "status": sca_data["status"]
    }

# Retrieve all sca_data given the name and owner of the techstack it analyses
async def retrieve_sca_data(name: str, owner:str, tag_name:str) -> dict:
    '''
    Retrieve all sca_data, from the database with matching name and owner
    :param name: name attribute of techstack that sca_data relates to
    :param owner: owner attribute of the techstack that sca_data relates to
    :return: Call sca_data_helper() on the given sca_data, which returns its data
    '''
    
    sca_data_list = []
    async for sca_data in sca_data_collection.find({"name": name, "owner": owner, "tag_name": tag_name}):
        sca_data_list.insert(0,sca_data_helper(sca_data))
    return sca_data_list