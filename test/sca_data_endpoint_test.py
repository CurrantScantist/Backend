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

# SCA_data endpoint testing 
    
def test_endpoint_sca_data_detailed_json_format():

    check = False
    response = client.get("/sca_data/{name_owner_tag_name}")
    try:
        responses = response.json()
        check = True
    except ValueError as valueerror:
        print(valueerror)

    assert check, "API endpoint `/sca_data/{name_owner_tag_name}` is not responding in JSON format"


def test_endpoint_sca_data_detailed_performance_sanity():

    # time is in nanosecond (since the epoch: unix time)
    maximum_tolerance_time = 1.0
    t0 = time.time()
    response = client.get("/sca_data/{name_owner_tag_name}")
    t1 = time.time()

    total = t1 - t0
    print(total)
    assert total < maximum_tolerance_time, "API endpoint `/sca_data/{name_owner_tag_name}` is crossing performance threshold"

# Negative test for /sca_data/{name_owner} endpoint
def test_endpoint_sca_data_detailed_wrong_link():

    response = client.get("/releae/{name_owner_tag_name}")
    assert  response.status_code == 404, "There supposed to error in the endpoint link: `/sca_data/{name_owner_tag_name}'"   

