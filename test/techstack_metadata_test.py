# Mounting the directory to app
import os
import sys
from fastapi.testclient import TestClient
import time

# # Works on server machine
# from server.database import connect
# from dotenv import load_dotenv

# from test.fail_secrets import CONNECTION_STRING_FAIL
# Testing should work
# # Works on Local Machine
from server.database import connect
from dotenv import load_dotenv

from server.app import app
from test.fail_secrets import CONNECTION_STRING_FAIL

client = TestClient(app)

# Positive Testing for Database connection
def test_mongoDB_connection_correct():

    check = False
    load_dotenv()
    CONNECTION_STRING=os.getenv('CONNECTION_STRING')
    # Connecting to MongoDB and getting the database test_db with the collection name repositories
    try:
        database = connect.DatabaseConnection(CONNECTION_STRING)
        database.client.server_info()
        database.connection_to_db("test_db")
        check = True
    except Exception as e: 
        print(e)
    assert check, "There is an issue in connection with MongoDB either in database name or authentication"

# Negative Testing for Database connection
def test_mongoDB_connection_fail():

    check = False
    # Connecting to false string MongoDB and getting the database test_db with the collection name repositories
    try:
        database = connect.DatabaseConnection(CONNECTION_STRING_FAIL)
        database.client.server_info()
        database.connection_to_db("test_db")
    except Exception as e: 
        check = True
        print(e)
    assert check, "There should be an issue in connection with MongoDB for authentication"

def test_endpoint_release_detailed_json_format():

    check = False
    response = client.get("/release/{name_owner}")
    try:
        responses = response.json()
        check = True
    except ValueError as valueerror:
        print(valueerror)

    assert check, "API endpoint `/release/{name_owner}` is not responsding in JSON format"


def test_endpoint_release_detailed_performance_sanity():

    # time is in nanosecond (since the epoch: unix time)
    maximum_tolerance_time = 1.0
    t0 = time.time()
    response = client.get("/release/{name_owner}")
    t1 = time.time()

    total = t1 - t0
    print(total)
    assert total < maximum_tolerance_time, "API endpoint `/release/{name_owner}` is crossing performance threshold"

# Negative test for /release/{name_owner} endpoint
def test_endpoint_release_detailed_wrong_link():

    response = client.get("/releae/{name_owner}")
    assert  response.status_code == 404, "There supposed to error in the endpoint link: `/release/{name_owner}'"   
