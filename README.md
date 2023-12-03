# API to connect model ML

A building RESTful APIs with FastAPI and MongoDB. 

## Features
+ Python FastAPI backend.
+ MongoDB database.
+ Authentication JWT
+ Deployment

## Using the applicaiton

To use the application, follow the outlined steps:

1. Clone this repository and create a virtual environment in it:

```console
$ python3 -m venv venv
```

2. Install the modules listed in the `requirements.txt` file:

```console
(venv)$ pip3 install -r requirements.txt
```
3. You also need to start your mongodb instance either locally or on Docker as well as create a `.env.dev` file. See the `.env.sample` for configurations. 

Example for running locally MongoDB at port 27017:
```console
cp .env.sample .env
```

4. Start the application:

```console
python main.py
```

The starter listens on port 8000 on address [0.0.0.0](0.0.0.0:8080). 

![image](https://github.com/zikrisuanda11/cafeanalyzer-api/assets/91446630/efa34262-0f7a-4079-acbc-22b62d98ab2e)


## Maps API Key

you need add your maps api key
more details: https://developers.google.com/maps/documentation/places/web-service/get-api-key#console_1

## Deployment

This application can be deployed on Cloud Run
