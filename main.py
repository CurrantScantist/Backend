import uvicorn
import os
import sys
# print(os.getcwd())
# sys.path.insert(0, os.getcwd()+"/FastAPI-mongoDB/app")
# print(os.getcwd())

if __name__ == "__main__":
    uvicorn.run("server.app:app", host="0.0.0.0", port=3333, reload=True)

    # Here, we instructed the file to run a Uvicorn server on port 8000 and reload on every file change.