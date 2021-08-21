#!/usr/bin/env python3
import motor.motor_asyncio
from dotenv import load_dotenv
import os

"""
MongoDB server seperate connection class to make more maintaniable and extensible
"""


class DatabaseConnection:
    """DataConnection Class to easy connection with multiple database using single class
    """

    def __init__(self):
        """
        Initialising values and connecting to the database
        """
        load_dotenv()
        password = os.getenv('PASSWORD')
        username = os.getenv('NAME')

        self.MONGO_DETAILS = f"mongodb+srv://{username}:{password}@cluster0.vao3k.mongodb.net/test_db?retryWrites" \
                             f"=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
        self.client = motor.motor_asyncio.AsyncIOMotorClient(self.MONGO_DETAILS)
        self.database_name = None

    def connection_to_db(self, db_name):
        """Establish the connection with the database by providing the database name

        Args:
            db_name ([string]): [Accepting a string as a name of database collection name to connect a single database]
        """
        if db_name == "test_db":
            self.database_name = self.client.test_db
