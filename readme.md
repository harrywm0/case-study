# Low-Side Data Ingestion Case-study

To be used as an upskilling and familiarity exercise for new joiners on low-side. The repository includes a small API written with Python-Flask, an associated Dockerfile to create an image and a docker-compose scripts which will deploy the development environment. Below are instructions for running the environment and accessing each component application.  

## Running with Docker

This repository includes a Dockerfile and docker-compose .yml file, which allow the entire project to be installed and ran in Docker containers. This includes bundled NiFi, ElasticSearch and Kibana applications, as well as containerizing the Python-Flask API and making exposing all endpoints.

 To launch the project using Docker, install Docker Desktop and simply use 
 ` docker-compose up ` 
 in the terminal in the working directory. It may take a short while to download and install the relevant images but eventually the applications will be available at their default ports:

  - Python-Flask API: localhost:5000
  - NiFi: localhost:8080
  - ElasticSearch: localhost:9200 / 9300
  - Kibana: localhost:5601
  
## SmallFlaskAPI

Miniature Python-Flask API, with csv -> json processor for NiFi Upskilling 

api.py handles the spinning up of the Flask API, while format.py formats the raw synthetic data .csv files to JSON for the API to handle.

Simply pull down the Synthetic-data repo into the project directory and reference the relative .csv file paths.

Just run:
  `python api.py`
from the project directory,

api.py will run format.py as an import. format.py simply formats one of the synthetic datasets into json and stores in the 
'data' directory.

You should see an output of:

`* Serving Flask app "api" (lazy loading)`

`* Environment: production`

`   WARNING: This is a development server. Do not use it in a production deployment.`

`   Use a production WSGI server instead.`

` * Debug mode: off `

` * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`

 
 You can now query the API at http://localhost:5000/dataset/all + a query with key/value
 
 Current endpoints:
 GET, POST, DELETE
