from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database.release import (
    retrieve_releases

)
from server.models.release import (
    ErrorResponseModel,
    ResponseModel,
    releaseSchema,
    UpdateReleaseModel,
)


router = APIRouter()


@router.get("/{name_owner}", response_description="release data retrieved")
async def get_release_data(name, owner):
    '''
    Once the release name and owner name is provided, starts the process of retrieving the specified release data
    :param name: Endpoint which asks for release name
    :param owner: Endpoint which asks for release owner name
    :return: response model that indicates release retrieval success or failure
    '''
    release = await retrieve_releases(name,owner)
    if release:
        return ResponseModel(release, "release data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "release doesn't exist.")
