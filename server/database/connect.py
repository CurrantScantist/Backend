#!/usr/bin/env python3
import motor.motor_asyncio

"""
MongoDB server seperate connection class to make more maintaniable and extensible
"""


class DatabaseConnection:
    """DataConnection Class to easy connection with multiple database using single class
    """

    def __init__(self, CONNECTION_STRING):
        """ Initialising values and connecting to the database

        Args:
            CONNECTION_STRING ([string]): [A MongoDB connection string including password and database name]
        """
        self.MONGO_DETAILS = CONNECTION_STRING
        self.client = motor.motor_asyncio.AsyncIOMotorClient(self.MONGO_DETAILS)
        self.database_name = None

    def connection_to_db(self, db_name):
        """Establish the connection with the database by providing the database name

        Args:
            db_name ([string]): [Accepting a string as a name of database colletion name to connect a single database]
        """
        if db_name == "test_db":
            self.database_name = self.client.test_db
