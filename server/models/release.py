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
        "id": "610912e6799bad69e5fc2640",
        "name": "vue",
        "owner": "vuejs",
        "tag_name": "v2.6.14",
        "LOC": {
          "JavaScript": {
            "nFiles": 431,
            "blank": 15859,
            "comment": 17485,
            "code": 137694
          },
          "TypeScript": {
            "nFiles": 19,
            "blank": 230,
            "comment": 78,
            "code": 1595
          },
          "HTML": {
            "nFiles": 18,
            "blank": 83,
            "comment": 39,
            "code": 1280
          },
          "Markdown": {
            "nFiles": 13,
            "blank": 305,
            "comment": 0,
            "code": 1206
          },
          "CSS": {
            "nFiles": 9,
            "blank": 130,
            "comment": 8,
            "code": 717
          },
          "Vuejs Component": {
            "nFiles": 27,
            "blank": 50,
            "comment": 12,
            "code": 644
          },
          "JSON": {
            "nFiles": 12,
            "blank": 0,
            "comment": 0,
            "code": 339
          },
          "YAML": {
            "nFiles": 3,
            "blank": 9,
            "comment": 2,
            "code": 139
          },
          "Bourne Shell": {
            "nFiles": 2,
            "blank": 16,
            "comment": 17,
            "code": 85
          },
          "Bourne Again Shell": {
            "nFiles": 2,
            "blank": 4,
            "comment": 1,
            "code": 16
          },
          "SUM": {
            "blank": 16686,
            "comment": 17642,
            "code": 143715,
            "nFiles": 536
          }
        },
        "committed_date": "2021-06-07T09:55:28"
        
    }


class UpdateReleaseModel(BaseModel):
    name: str = Field(...)
    owner: str = Field(...)
    tag_name: str = Field(...)
    LOC: list = Field(...)
    committed_date: str = Field(...)
    
    
    class Config:
        schema_extra = {
        "id": "610912e6799bad69e5fc2640",
        "name": "vue",
        "owner": "vuejs",
        "tag_name": "v2.6.14",
        "LOC": {
          "JavaScript": {
            "nFiles": 431,
            "blank": 15859,
            "comment": 17485,
            "code": 137694
          },
          "TypeScript": {
            "nFiles": 19,
            "blank": 230,
            "comment": 78,
            "code": 1595
          },
          "HTML": {
            "nFiles": 18,
            "blank": 83,
            "comment": 39,
            "code": 1280
          },
          "Markdown": {
            "nFiles": 13,
            "blank": 305,
            "comment": 0,
            "code": 1206
          },
          "CSS": {
            "nFiles": 9,
            "blank": 130,
            "comment": 8,
            "code": 717
          },
          "Vuejs Component": {
            "nFiles": 27,
            "blank": 50,
            "comment": 12,
            "code": 644
          },
          "JSON": {
            "nFiles": 12,
            "blank": 0,
            "comment": 0,
            "code": 339
          },
          "YAML": {
            "nFiles": 3,
            "blank": 9,
            "comment": 2,
            "code": 139
          },
          "Bourne Shell": {
            "nFiles": 2,
            "blank": 16,
            "comment": 17,
            "code": 85
          },
          "Bourne Again Shell": {
            "nFiles": 2,
            "blank": 4,
            "comment": 1,
            "code": 16
          },
          "SUM": {
            "blank": 16686,
            "comment": 17642,
            "code": 143715,
            "nFiles": 536
          }
        },
        "committed_date": "2021-06-07T09:55:28"
        
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
