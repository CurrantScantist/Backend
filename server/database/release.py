from server.database.connect import DatabaseConnection
import os
from dotenv import load_dotenv

"""
Retrieve release and release data from the mongodb database
"""
# Connecting to MongoDB and getting the database test_db with the collection name releases
load_dotenv()
CONNECTION_STRING=os.getenv('CONNECTION_STRING')
database = DatabaseConnection(CONNECTION_STRING)
database.connection_to_db("test_db")
release_collection = database.database_name.get_collection("releases")


# Retrieve all releases for name and owner
async def retrieve_releases(name: str, owner: str) -> list:
    '''
    Retrieve all releases and its metadata, from the database with matching name and owner
    :param name: name attribute of the release's techstack
    :param owner: owner attribute of the release's techstack
    :return: Call release_helper() on the given release, which returns its respective metadata
    '''
    
    releases = []
    async for release in release_collection.find({"name": name, "owner": owner}, {"_id": 0, "LOC": 0}).sort([('committed_date', 1)]):
        releases.append(release)
    return releases
