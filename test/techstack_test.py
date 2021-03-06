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
    PASSWORD = os.getenv('PASSWORD')
    USERNAME = os.getenv('NAME')
    CONNECTION_STRING = f"mongodb+srv://{USERNAME}:" \
                        f"{PASSWORD}@cluster0.vao3k.mongodb.net/test_db?retryWrites=true&w=majority"
    print(CONNECTION_STRING)
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


# Positive test cases for /nodelink_data endpoint
# def test_endpoint_nodelink_data_status_code():
#
#     response = client.get("/techstack/nodelink_data")
#     assert response.status_code == 200, "f{response.status_code} coming from endpoint techstack/nodelink_data"

def test_endpoint_nodelink_data_json_format():

    check = False
    response = client.get("/techstack/nodelink_data")

# Negative test for techstack/detailed endpoint
def test_endpoint_techstack_detailed_wrong_link():
    response = client.get("/techstac/detailed")
    assert response.status_code == 404, "There supposed to error in the endpoint link: `techstack/detailed`"


# Testing topten endpoint
# Positive test cases for techstack/topten endpoint
def test_endpoint_techstack_topten_status_code():
    response = client.get("/techstack/topten")
    print(response)
    assert response.status_code == 200, "f{response.status_code} coming from endpoint techstack/topten"


def test_endpoint_techstack_topten_json_format():
    check = False
    response = client.get("/techstack/topten")
    try:
        responses = response.json()
        check = True
    except ValueError as valueerror:
        print(valueerror)

    assert check, "API endpoint `techstack/nodelink_data` is not responding in JSON format"
    assert check, "API endpoint `techstack/topten` is not responding in JSON format"


def test_endpoint_techstack_topten_performance_sanity():
    # time is in nanosecond (since the epoch: unix time)
    maximum_tolerance_time = 1.0
    t0 = time.time()
    response = client.get("/techstack/topten")
    t1 = time.time()

    total = t1 - t0
    print(total)
    assert total < maximum_tolerance_time, "API endpoint `techstack/topten` is crossing performance threshold"


def test_endpoint_nodelink_data_performance_sanity():

    # time is in nanosecond (since the epoch: unix time)
    maximum_tolerance_time = 1.0
    t0 = time.time()
    response = client.get("/techstack/nodelink_data")
    t1 = time.time()

    total = t1 - t0
    print(total)
    assert total < maximum_tolerance_time, "API endpoint `techstack/nodelink_data` is crossing performance threshold"

# Testing contribution endpoint 
# Positive test cases for techstack/contribution endpoint
def test_endpoint_techstack_contribution_status_code():
    response = client.get("/techstack/contribution/{name_owner}?name=bottle&owner=bottlepy")
    print(response)
    assert response.status_code == 200, "f{response.status_code} coming from endpoint techstack/contribution"


def test_endpoint_techstack_contribution_json_format():
    check = False
    response = client.get("/techstack/contribution/{name_owner}?name=bottle&owner=bottlepy")
    try:
        responses = response.json()
        check = True
    except ValueError as valueerror:
        print(valueerror)

    assert check, "API endpoint `techstack/detailed` is not responding in JSON format"


def test_endpoint_techstack_contribution_performance_sanity():
    # time is in nanosecond (since the epoch: unix time)
    maximum_tolerance_time = 1.0
    t0 = time.time()
    response = client.get("/techstack/contribution/{name_owner}?name=bottle&owner=bottlepy")
    t1 = time.time()

    total = t1 - t0
    print(total)
    assert total < maximum_tolerance_time, "API endpoint `techstack/detailed` is crossing performance threshold"


# Negative test for techstack/detailed endpoint
def test_endpoint_techstack_contribution_wrong_parameter():
    response = client.get("/techstack/contribution/{name_owner}?name=bott&owner=bottlepy")
    assert response.status_code == 404, "There supposed to error in the endpoint link: `techstack/contribution` because techstack does not exist in the database"


def test_endpoint_retrieve_similar_repositories_success():
    response = client.get("/techstack/similar/{name_owner}?name=tqdm&owner=tqdm")
    assert response.status_code == 200
    assert response.json()


def test_endpoint_retrieve_similar_repositories_not_found():
    response = client.get("/techstack/similar/{name_owner}?name=tqd&owner=tqdm")
    assert response.status_code == 404


# Testing /Heatmap endpoint
def test_endpoint_techstack_heatmap_status_code():
    response = client.get("/techstack/heatmap/{name_owner}?name=vue&owner=vuejs")
    assert response.status_code == 200, "f{response.status_code} coming from endpoint techstack/heatmap"


def test_endpoint_techstack_contribution_json_format():

    check = False
    response = client.get("/techstack/heatmap/{name_owner}?name=vue&owner=vuejs")
    try:
        responses = response.json()
        check = True
    except ValueError as valueerror:
        print(valueerror)

    assert check, "API endpoint `techstack/heatmap` is not responsding in JSON format"

def test_endpoint_techstack_contribution_performance_sanity():

    # time is in nanosecond (since the epoch: unix time)
    maximum_tolerance_time = 1.0
    t0 = time.time()
    response = client.get("/techstack/heatmap/{name_owner}?name=vue&owner=vuejs")
    t1 = time.time()
    total = t1 - t0
    assert total < maximum_tolerance_time, "API endpoint `techstack/heatmap` is crossing performance threshold"
