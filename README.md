
<h1 align="center">Backend Service</h1>
<p align="center">
  <img src="https://user-images.githubusercontent.com/47905424/140928672-f03254c1-51b6-4c6f-bbb1-a9a45239cdcf.png"width="400px"/>
</p>


## Introduction
The Backend service is being used to establish communication between Database. 

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

#### Normal Test Execution


* Ensure that you have a virtual environment setup for **python3.6+**, and it is activated.
* Ensure that you are in root directory of ```Backend``` 
```
 pytest test/[file name that ends with test.py]
```

Generating cover report 

```
coverage run -m pytest -v test && coverage report -m
```




## APIs
This project has several APIs exposed:
* The API Serves the communication with database and any device. 
* The ```GET``` request has been used predominately in the API endpoints.


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

## Server Configuration 






## Further Resource




How to use in a development setting.

1. Ensure that you have a virtual environment setup
2. activate this virtual environment: .\backendEnv\Scripts\activate
3. Ensure that .env file exists in Backend root directory (includes db key)
4. cd Backend
5. python main.py
