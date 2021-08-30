from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class scaSchema(BaseModel):
    name: str = Field(...)
    owner: str = Field(...)
    tag_name: str = Field(...)
    results: dict = Field(...)
    status: str = Field(...)

    class Config:
        schema_extra = {
        "id": "610912e6799bad69e5fc2640",
        "name": "vue",
        "owner": "vuejs",
        "tag_name": "v2.6.14",
        "results": {
            "vulnerabilities": [
            {
                "public_id": "abcd",
                "library": "click",
                "library_version": "7.1.2",
                "issue_source": "ci",
                "issue_type": "cve",
                "description": "click/install.py in click does not require files in package filesystem tarballs to start with ./ (dot slash), which allows remote attackers to install an alternate security policy and gain privileges via a crafted package, as demonstrated by the test.mmrow app for Ubuntu phone.",
                "score": 8.6
            }
            ],
            "licenses": [
                {
                    "license_name": "abcde",
                    "library": "markupsafe",
                    "file_count": 0,
                    "vendor": "",
                    "status": "N.A.",
                    "action_type": "Permissive",
                    "score": 2
                },
                {        
                    "license_name": "abcdef",
                    "library": "six",
                    "file_count": 0,
                    "vendor": "",
                    "status": "N.A.",
                    "action_type": "Permissive",
                    "score": 1
                }
            ],
            "policy_deny": "false",
            "lib_ver_count": 13,
            "issue_breakdown": 
            {
                "critical": 0,
                "high": 0,
                "median": 0,
                "low": 0,
                "none": 0
            },
            "compliance_policy_breakdown": 
            {
                "approve": 0,
                "flag": 0,
                "deny": 0
            }
        },
        "status": "finished"
    }

class UpdateScaModel(BaseModel):
    name: str = Field(...)
    owner: str = Field(...)
    tag_name: str = Field(...)
    results: dict = Field(...)
    status: str = Field(...)

    class Config:
        schema_extra = {
        "id": "610912e6799bad69e5fc2640",
        "name": "vue",
        "owner": "vuejs",
        "tag_name": "v2.6.14",
        "results": {
            "vulnerabilities": [
            {
                "public_id": "abcd",
                "library": "click",
                "library_version": "7.1.2",
                "issue_source": "ci",
                "issue_type": "cve",
                "description": "click/install.py in click does not require files in package filesystem tarballs to start with ./ (dot slash), which allows remote attackers to install an alternate security policy and gain privileges via a crafted package, as demonstrated by the test.mmrow app for Ubuntu phone.",
                "score": 8.6
            }
            ],
            "licenses": [
                {
                    "license_name": "abcde",
                    "library": "markupsafe",
                    "file_count": 0,
                    "vendor": "",
                    "status": "N.A.",
                    "action_type": "Permissive",
                    "score": 2
                },
                {        
                    "license_name": "abcdef",
                    "library": "six",
                    "file_count": 0,
                    "vendor": "",
                    "status": "N.A.",
                    "action_type": "Permissive",
                    "score": 1
                }
            ],
            "policy_deny": "false",
            "lib_ver_count": 13,
            "issue_breakdown": 
            {
                "critical": 0,
                "high": 0,
                "median": 0,
                "low": 0,
                "none": 0
            },
            "compliance_policy_breakdown": 
            {
                "approve": 0,
                "flag": 0,
                "deny": 0
            }
        },
        "status": "finished"
    }

    
def ResponseModel(data, message):
    '''
    Returns a response model, with the queried data, response code and response message
    :param data: query payload
    :param message: message of success or failure
    :return: Returns Response body, code, and message of success or failure
    '''
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    '''
    Returns an error statement indicating the error type, error code and its description.
    :param error: indication message of error
    :param code: error code
    :param message: error description
    :return: an error response model, indicating the error type, error code and its description.
    '''
    return {"error": error, "code": code, "message": message}