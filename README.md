 <h1 align="center">Backend Service</h1>
<p align="center">
<!--   <img src=""/> -->
</p>

![build](https://github.com/CurrantScantist/Backend/actions/workflows/main.yml/badge.svg)
![version](https://img.shields.io/badge/version-1.0.0-blue)


## Introduction
The Backend service is being used to establish communication with database. 

#### Python Framework
[FASTAPI](https://fastapi.tiangolo.com/) framework is a modern, fast, robust, easy scalable  web framework for building APIs with Python 3.6+.
The key features:
* Fast: One of the fastest Python open source framework [link](https://fastapi.tiangolo.com/#performance)
* Easy Scalable and Maintainable
* Easy Learning: Designed to be easy to use and learn. Less time reading docs.
* Robust: Get production-ready code. With automatic interactive documentation.
and many more..

Please follow [official documentation](https://fastapi.tiangolo.com/features/) for further information.


#### Module Structure

![image](https://user-images.githubusercontent.com/47905424/141119145-82aac46e-530a-4717-8fb3-204a9867f0be.png)

##### Current services module structure 

![image](https://user-images.githubusercontent.com/47905424/141119444-f62400df-c18e-4fef-af8a-f6d197ca21ac.png)



## Getting Up and Running

#### First time setup  
```
1.Ensure that you have a virtual environment setup for **python3.6+**, and it is activated.
If not, please setup a new virtual environment for python3.6+

2. Ensure that .env file exists in Backend root directory.
If not, please checkout configuration section.

3. Ensure that you are in root directory of ```Backend```  

4. pip install -r requirements.txt  
5. python main.py  
```
#### Normal Execution
Activate your python3.6+ virtual environment.  
```python main.py```

#### API Doc
1. Normal Excecution 
2. visit ```http://127.0.0.1:3333/docs```


#### Normal Test Execution


* Ensure that you have a virtual environment setup for **python3.6+**, and it is activated.
* Ensure that you are in root directory of ```Backend``` 
```
 pytest test/[file name that ends with test.py]
```

Generating coverage report 

```
coverage run -m pytest -v test && coverage report -m
```




## APIs
This project has several APIs:
* The API Serves the communication with database and any device. 
* The ```GET``` request has been used predominately in the API endpoints.

### Endpoints
![image](https://user-images.githubusercontent.com/47905424/141135175-ec37e4c8-05dd-444f-91d9-fedb851068a0.png)



## Unit / Automated Tests
* Github Action is being used to automated Tests.
* Unit tests for APIs have been standardised for the GET request.
* Test File Structure   
```
|..  
    ├── test                  
          |── [xyz] _ test.py                
|..   
```
* Adding new test file
  + By convention and setup, the new test should go into ```test``` file 



## Error Handling

## Configuration
 
#### Database connection
MONGODB is being used as a database platform for NoSQL database.   
Contact exisitng Developers/maintainers to get either admin access or developer access for MONGODB.

1. Create ```.env``` file in the root directory
2. Add following variables with your access details

```
PASSWORD={.............}
NAME={.........}
```



## Server Configuration 

#### DOCKER

DOCKER file configuration to run on server

```
# syntax=docker/dockerfile:1

FROM python:3.7

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 3333

COPY . .

CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "3333"]

```

Note: Configuration might not be updated. Therefore, please confirm with DOCKER file from the repository only. 


## Feedback

All bugs, feature requests, pull requests, feedback, etc., are welcome. [Create an issue.](https://github.com/CurrantScantist/Backend/issues)

## Next Step

* API limiter
* Add on APIs as per the new feature request
* Minimise additional dependencies
* Area of improvement regarding API's performance


