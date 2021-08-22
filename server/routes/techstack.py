from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database.techstack import (
    retrieve_techstack,
    retrieve_techstacks,
    retrieve_techstack_important_info,
    retrieve_techstack_commit_data
)
from server.models.techstack import (
    ErrorResponseModel,
    ResponseModel,
    TechstackSchema,
    UpdateTechstackModel,
)

router = APIRouter()


@router.get("/detailed", response_description="Techstacks retrieved")
async def get_techstacks():
    '''
    Once called, starts the process of retrieving all techstacks, accompanied with all their metadata.
    :return:  Response Model that gives indication of all techstack retrieval success or failure
    '''
    techstacks = await retrieve_techstacks()
    if techstacks:
        return ResponseModel(techstacks, "Techstacks data retrieved successfully")
    return ResponseModel(techstacks, "Empty list returned")

    
@router.get("/list", response_description="Techstacks retrieved")
async def get_techstacks():
    '''
    Once called, starts the process of retrieving all techstacks, but only accompanied with their id, name and owner.
    :return: Response Model that gives indication that all techstack retrieval and their id,name and owner metadata, is successful.
    '''
    techstacks = await retrieve_techstack_important_info()
    if techstacks:
        return ResponseModel(techstacks, "Techstacks data retrieved successfully")
    return ResponseModel(techstacks, "Empty list returned")


# @router.get("/{name_owner}", response_description="Techstack data retrieved")
# async def get_techstack_data(name, owner):
#     '''
#     Once the techstack name and owner name is provided, starts the process of retrieving the specified techstack data
#     :param name: Endpoint which asks for techstack name
#     :param owner: Endpoint which asks for techstack owner name
#     :return: response model that indicates techstack retrieval success or failure
#     '''
#     techstack = await retrieve_techstack(name,owner)
#     print("shouldn't be here")
#     if techstack:
#         return ResponseModel(techstack, "Techstack data retrieved successfully")
#     return ErrorResponseModel("An error occurred.", 404, "Techstack doesn't exist.")


@router.get("/commit_data", response_description="Techstack commit and contributor data retrieved")
async def get_techstack_commit_data(name, owner):
    '''
    Once the techstack name and owner name is provided, starts the process of retrieving the specified techstack data
    :param name: Endpoint which asks for techstack name
    :param owner: Endpoint which asks for techstack owner name
    :return: response model that indicates techstack retrieval success or failure
    '''
    techstack = await retrieve_techstack_commit_data(name,owner)
    print(techstack)
    if techstack:
        return ResponseModel(techstack, "Techstack data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Techstack doesn't exist.")




