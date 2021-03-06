from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
from server.database.techstack import (
    retrieve_techstack,
    retrieve_techstack_important_info,
    retrieve_techstack_contribution_data,
    retrieve_similar_repository_data,
    retrieve_nodelink_data,
    retrieve_techstack_heatmap,
    retrieve_top_ten_techstacks,
    retrieve_similar_repository_data
)
from server.models.techstack import (
    ErrorResponseModel,
    ResponseModel,
)

router = APIRouter()


@router.get("/list", response_description="Techstacks retrieved")
async def get_list_of_techstacks():
    '''
    Once called, starts the process of retrieving all techstacks, but only accompanied with their id, name and owner.
    :return: Response Model that gives indication that all techstack retrieval and their id,name and owner metadata,
    is successful.
    '''
    techstacks = await retrieve_techstack_important_info()
    if techstacks:
        return ResponseModel(techstacks, "Techstacks data retrieved successfully")
    return ResponseModel(techstacks, "Empty list returned")


@router.get("/nodelink_data", response_description="nodelink data retrieved")
async def get_nodelink_data(name, owner):
    '''
    Once called, will retrieve the nodelink data from the database
    :return: Response model that gives indication that all nodelink data retrieval is complete
    '''
    nodelink_data = await retrieve_nodelink_data(name, owner)
    if nodelink_data:
        return ResponseModel(nodelink_data, "nodelink  data retrieved successfully")
    return ResponseModel(nodelink_data, "Empty list returned")


@router.get("/topten", response_description="Techstack data retrieved")
async def get_top_ten_techstacks():
    '''
    Once called, starts the process of retrieving top 10 techstacks based on highest to lowest stargazer count.
    :return: Response Model that gives indication that top ten techstack retrieval and their metadata,
    is successful.
    '''
    techstacks = await retrieve_top_ten_techstacks()
    if techstacks:
        return ResponseModel(techstacks, "Techstacks data retrieved successfully")
    return ResponseModel(techstacks, "Empty list returned")


@router.get("/{name_owner}", response_description="Techstack data retrieved")
async def get_specific_techstack_data(name, owner):
    '''
    Once the techstack name and owner name is provided, starts the process of retrieving the specified techstack data
    :param name: Endpoint which asks for techstack name
    :param owner: Endpoint which asks for techstack owner name
    :return: response model that indicates techstack retrieval success or failure
    '''
    techstack = await retrieve_techstack(name, owner)
    if techstack:
        return ResponseModel(techstack, "Techstack data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Techstack doesn't exist.")


@router.get("/contribution/{name_owner}", response_description="Techstack data retrieved")
async def get_techstack_contribution_data(name, owner):
    '''
    Once the techstack name and owner name is provided, starts the process of retrieving the specified techstack data
    :param name: Endpoint which asks for techstack name
    :param owner: Endpoint which asks for techstack owner name
    :return: response model that indicates techstack retrieval success or failure
    '''
    techstack = await retrieve_techstack_contribution_data(name, owner)

    if techstack:
        return ResponseModel(techstack, "Techstack data retrieved successfully")
    raise HTTPException(status_code=404, detail="Item not found")


@router.get("/similar/{name_owner}", response_description="Similar repository data retrieved")
async def get_similar_repository_data(name, owner):
    """
    Retrieves up to 5 repositories that are similar to an inputted repository (the inputted repository is guaranteed
    to be one of the 5 repositories). For repositories that have github topics, two repositories are considered similar
    if they have at least one tag in common. For repositories that don't have github topics, repositories that share the
    same predominant language are considered similar. In the case when there are more than 4 repositories that are
    similar to the inputted repository, the most popular 4 are returned (measured based on the stargazers_count).
    :param name: the name of the repository
    :param owner: the owner of the repository
    :return: the response model for successful requests otherwise a HTTPException is raised
    """
    repos = await retrieve_similar_repository_data(name, owner)

    if len(repos) == 1:
        if any([key not in repos[0] for key in ["num_components", "num_vulnerabilities", "size"]]):
            raise HTTPException(status_code=404, detail="Input repository does not have the required dependency data")

    if repos:
        return ResponseModel(repos, "Similar repository data retrieved")
    raise HTTPException(status_code=404, detail="Repository not found")


@router.get("/heatmap/{name_owner}", response_description="Heatmap data retrieved")
async def get_heatmap_data_for_techstack(name, owner):
    '''
    Once the techstack name and owner name is provided, starts the process of retrieving heatmap data for the techstack
    :param name: Endpoint which asks for techstack name
    :param owner: Endpoint which asks for techstack owner name
    :return: response model that indicates heatmap data retrieval success or failure
    '''
    techstack = await retrieve_techstack_heatmap(name,owner)
   
    if techstack:
        return ResponseModel(techstack, "Techstack data retrieved successfully")
    raise HTTPException(status_code=404, detail="Item not found")





