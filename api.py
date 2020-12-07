import pandas as pd
from flask import Flask
from flask import abort
from flask import request
from flask_restful import Resource, Api, reqparse
import json
import os
import os.path

dataDir = './data/'

app = Flask(__name__)
api = Api(app)

# Assert CSV files have been converted to JSON in project dir.
def assertJsons():
    if os.path.isfile('./data/companies.json') and os.path.isfile('./data/master.json'):
        return True
    else:
        return False

def handleGET_set(dataName):
    assertJsons()

    with open(dataDir + dataName + '.json') as jsonStruct:
        return json.load(jsonStruct)

def handlePOST_set(data):
    if not request.json:
        abort(400)
    else:
        #Handle list without name/data fields - ConvertRecord-NiFi outputs a large list (array) of individual JSON objects constructed from rows of CSV
        if isinstance(data, list):
            with open(dataDir + 'list' + '.json', 'w') as outfile:
                json.dump(data, outfile)
            return json.dumps({'success': True}), 201, {'ContentType': 'application/json'}
        else:
            with open(dataDir + data['name'] + '.json', 'w') as outfile:
                json.dump(data['data'], outfile)
            return json.dumps({'sucess': True}), 201, {'ContentType': 'application/json'}

def handleDELETE_set(dataName):
    assertJsons()
    dataPath = dataDir + dataName + '.json'

    if os.path.exists(dataPath):
        os.remove(dataPath)
    else:
        return json.dumps({'message': 'no data of name' + dataName}), 404

# Home route - localhost:5000/ - Only accepts GET requests
@app.route('/', methods=['GET'])
def home():
    return "<h1>Miniature Python-Flask API</h1> <p> This API was built using Python/Flask and has 3 endpoints: GET, POST and DELETE"

# All data route - localhost/5000/data/'dataset' - Returns all data from specified dataset
# Can perform DELETE on dataset or POST new entry without specifying dataset
@app.route('/dataset/all', methods=['GET', 'DELETE', 'POST'])
def dataset():
    if request.method == 'GET':
        if request.args:
            req = request.args.get('name')
            return {req: handleGET_set(req)}, 200
        else:
            return 'Please enter Request Arguments', 404

    elif request.method == 'DELETE':
        req = request.args.get('name')
        return {req: handleDELETE_set(req)}, 204

        return "Handle dataSET DELETE"

    elif request.method == 'POST':
        data = request.get_json()
        return handlePOST_set(data)

# TODO: Finish single index data endpoints
# Data route - localhost/5000/data/'dataset'/'index' - Returns individual data entry from specified dataset
# Can perform DELETE on data entry or POST new entry without index
@app.route('/dataset/', methods=['GET', 'DELETE', 'POST'])
def singleData():
    if request.method == 'GET':
        return "Handle data index GET"
    elif request.method == 'DELETE':
        return "Handle data index DELETE"
    elif request.method == 'POST':
        return "Handle data index POST"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
