from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class TechstackSchema(BaseModel):
    name: str = Field(...)
    owner: str = Field(...)
    description: str = Field(...)
    forks: float = Field(...)
    forks_count: float = Field(...)
    language: str = Field(...)
    stargazers_count: float = Field(...)
    watchers_count: float = Field(...)
    watchers: float = Field(...)
    size: float = Field(...)
    default_branch: str = Field(...)
    open_issues_count: float = Field(...)
    open_issues: float = Field(...)
    has_issues: bool = Field(...)
    archived: bool = Field(...)
    disabled: bool = Field(...)
    pushed_at: str = Field(...)
    created_at: str = Field(...)
    updated_at: str = Field(...)
    languages: list = Field(...)
    topics: list = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "id": "60fc0777f113c31336c7e596",
                "techstack_name": "svelte",
                "owner": "sveltejs",
                "description": "Cybernetically enhanced web apps",
                "forks": 2317,
                "forks_count": 2317,
                "language": "TypeScript",
                "stargazers_count": 48744,
                "watchers_count": 48744,
                "watchers": 48744,
                "size": 67214,
                "default_branch": "master",
                "open_issues_count": 573,
                "open_issues": 573,
                "has_issues": True,
                "archived": False,
                "disabled": False,
                "pushed_at": "2021-07-24T18:30:36Z",
                "created_at": "2016-11-20T18:13:05Z",
                "updated_at": "2021-07-25T03:36:42Z",
                "languages": {
                    "TypeScript": 714949,
                    "Svelte": 557000,
                    "JavaScript": 9669
                },
                "topics": [
                    "template",
                    "ui",
                    "compiler"
                ]
            }
        }


class UpdateTechstackModel(BaseModel):
    name: str = Field(...)
    owner: str = Field(...)
    description: str = Field(...)
    forks: float = Field(...)
    forks_count: float = Field(...)
    language: str = Field(...)
    stargazers_count: float = Field(...)
    watchers_count: float = Field(...)
    watchers: float = Field(...)
    size: float = Field(...)
    default_branch: str = Field(...)
    open_issues_count: float = Field(...)
    open_issues: float = Field(...)
    has_issues: bool = Field(...)
    archived: bool = Field(...)
    disabled: bool = Field(...)
    pushed_at: str = Field(...)
    created_at: str = Field(...)
    updated_at: str = Field(...)
    languages: list = Field(...)
    topics: list = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "id": "60fc0777f113c31336c7e596",
                "releases": {
                    "v3.40.0": {}
                },
                "techstack_name": "svelte",
                "owner": "sveltejs",
                "description": "Cybernetically enhanced web apps",
                "forks": 2317,
                "forks_count": 2317,
                "language": "TypeScript",
                "stargazers_count": 48744,
                "watchers_count": 48744,
                "watchers": 48744,
                "size": 67214,
                "default_branch": "master",
                "open_issues_count": 573,
                "open_issues": 573,
                "has_issues": True,
                "archived": False,
                "disabled": False,
                "pushed_at": "2021-07-24T18:30:36Z",
                "created_at": "2016-11-20T18:13:05Z",
                "updated_at": "2021-07-25T03:36:42Z",
                "languages": {
                    "TypeScript": 714949,
                    "Svelte": 557000,
                    "JavaScript": 9669
                },
                "topics": [
                    "template",
                    "ui",
                    "compiler"
                ]
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
