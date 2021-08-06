# import motor.motor_asyncio
# from bson.objectid import ObjectId
# from server.secrets import CONNECTION_STRING

# MONGO_DETAILS = CONNECTION_STRING

# client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

# database = client.test_db

# techstack_collection = database.get_collection("repositories")


# def techstack_helper(techstack) -> dict:
#     """
#     Helps retrieve_techstack return techstack metadata in dictionary form.
#     :param techstack: techstack object from database
#     :return: techstack metadata in an ordered dictionary format
#     """
#     return {
#         "id": str(techstack["_id"]),
#         "name": techstack["name"],
#         "owner": techstack["owner"],
#         "description": techstack["description"],
#         "forks": techstack["forks"],
#         "forks_count": techstack["forks_count"],
#         "language": techstack["language"],
#         "stargazers_count": techstack["stargazers_count"],
#         "watchers_count": techstack["watchers_count"],
#         "watchers": techstack["watchers"],
#         "size": techstack["size"],
#         "default_branch": techstack["default_branch"],
#         "open_issues_count": techstack["open_issues_count"],
#         "open_issues": techstack["open_issues"],
#         "has_issues": techstack["has_issues"],
#         "archived": techstack["archived"],
#         "disabled": techstack["disabled"],
#         "pushed_at": techstack["pushed_at"],
#         "created_at": techstack["created_at"],
#         "updated_at": techstack["updated_at"],
#         "languages": techstack["languages"],
#         "topics": techstack["topics"],
#     }


# async def retrieve_techstacks():
#     '''
#     Retrieve all unique techstacks in the database
#     :return: all techstacks present in the database
#     '''
#     techstacks = []
#     async for techstack in techstack_collection.find():
#         techstacks.append(techstack_helper(techstack))
#     print(techstacks)
#     return techstacks


# async def retrieve_techstack(name: str, owner: str) -> dict:
#     '''
#     Retrieve a specific techstack and its metadata, from the database
#     :param name: name attribute of the techstack
#     :param owner: owner attribute of the techstack
#     :return: Call techstack_helper() on the given techstack, which returns its respective metadata
#     '''
#     techstack = await techstack_collection.find_one({"name": name, "owner": owner})
#     if techstack:
#         return techstack_helper(techstack)
