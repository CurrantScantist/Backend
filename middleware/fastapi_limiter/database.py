#!/usr/bin/env python3
import collections
import motor.motor_asyncio
from bson.objectid import ObjectId


"""
MongoDB server seperate connection class to make more maintaniable and extensible
"""

class DatabaseConnection:
  """DataConnection Class to easy connection with multiple database using single class
  """

  def __init__ (self, CONNECTION_STRING, DB_NAME, COLLECTION_NAME):
    """ Initialising values and connecting to the database

    Args:
        CONNECTION_STRING ([string]): [A MongoDB connection string including password and database name]
    """
    self.db_name = DB_NAME
    self.MONGO_DETAILS = CONNECTION_STRING
    self.client = motor.motor_asyncio.AsyncIOMotorClient(self.MONGO_DETAILS)
    self.collection_name = COLLECTION_NAME

  def connection_to_db(self, db_name):
    """Establish the connection with the database by providing the database name

    Args:
        db_name ([string]): [Accepting a string as a name of database colletion name to connect a single database]
    """
    if db_name == "development":
      database = self.client.development
      return database
    return False

  async def getListOfWhiteListedIp(self):
    output = self.connection_to_db(self.db_name)
    if (output):
      developers_ip_collection = output.get_collection(self.collection_name)
      collection_of_ips = []
      async for ip in developers_ip_collection.find({},{"ip_address": 1}):
        collection_of_ips.append(ip["ip_address"])
      return collection_of_ips
    else:
      print("Database doesn't exist")
      return False
  
    
