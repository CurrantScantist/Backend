from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database.sca import (
    retrieve_sca_data

)
from server.models.sca import (
    ErrorResponseModel,
    ResponseModel,
    scaSchema,
    UpdateScaModel,
)


router = APIRouter()


@router.get("/{name_owner_tag_name}", response_description="SCA data retrieved")
async def get_sca_data_using_name_owner_tag_name(name, owner,tag_name):
    '''
    Once the techstack name and owner name and tag_name is provided, it signals the start of the process of retrieving the specified sca_data
    :param name: Endpoint which asks for release name
    :param owner: Endpoint which asks for release owner name
    :param tag_name: Endpoint which asks for tag_name
    :return: response model that indicates sca_data retrieval success or failure
    '''
    sca_data = await retrieve_sca_data(name,owner,tag_name)
    if sca_data:
        return ResponseModel(sca_data, "sca_data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "sca_data doesn't exist.")