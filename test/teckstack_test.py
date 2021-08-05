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

# Positive test cases for techstack/detailed endpoint
def test_endpoint_techstack_detailed_status_code():

    response = client.get("/techstack/detailed")
    assert response.status_code == 200, "f{response.status_code} coming from endpoint techstack/detailed"

def test_endpoint_techstack_detailed_json_format():

    check = False
    response = client.get("/techstack/detailed")
    try:
        responses = response.json()
        check = True
    except ValueError as valueerror:
        print(valueerror)

    assert check, "API endpoint `techstack/detailed` is not responsding in JSON format"


def test_endpoint_techstack_detailed_performance_sanity():

    # time is in nanosecond (since the epoch: unix time)
    maximum_tolerance_time = 1.0
    t0 = time.time()
    response = client.get("/techstack/detailed")
    t1 = time.time()

    total = t1 - t0
    print(total)
    assert total < maximum_tolerance_time, "API endpoint `techstack/detailed` is crossing performance threshold"

# Negative test for techstack/detailed endpoint
def test_endpoint_techstack_detailed_wrong_link():

    response = client.get("/techstac/detailed")
    assert  response.status_code == 404, "There supposed to error in the endpoint link: `techstack/detailed`"   
