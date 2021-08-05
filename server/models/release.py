from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class releaseSchema(BaseModel):
    name: str = Field(...)
    owner: str = Field(...)
    tag_name: str = Field(...)
    LOC: list = Field(...)
    committed_date: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "id": "60fc0777f113c31336c7e596",
                "name": "vue",
                "owner": "vuejs",
                "tag_name": "Cybernetically enhanced web apps",
                "LOC": {
                    "TypeScript": {
                        "nfiles": 60,
                        "blank": 3112
                        },
                    "JavaScript":{
                        "nfiles": 212,
                        "blank": 2214
                    }
                },
                "committed_date":"2032-04-23T10:20:30.400+02:30"
            }
        }


class UpdateReleaseModel(BaseModel):
    name: str = Field(...)
    owner: str = Field(...)
    tag_name: str = Field(...)
    LOC: list = Field(...)
    committed_date: str = Field(...)
    
    
    class Config:
        schema_extra = {
            "example": {
                "id": "60fc0777f113c31336c7e596",
                "name": "vue",
                "owner": "vuejs",
                "tag_name": "Cybernetically enhanced web apps",
                "LOC": {
                    "TypeScript": {
                        "nfiles": 60,
                        "blank": 3112
                        },
                    "JavaScript":{
                        "nfiles": 212,
                        "blank": 2214
                    }
                },
                "committed_date":"2032-04-23T10:20:30.400+02:30"
            }
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
