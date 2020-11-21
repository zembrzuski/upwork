from elasticsearch import Elasticsearch
from datetime import datetime
from flask import Flask
from flask import request

es = Elasticsearch()

app = Flask(__name__)

# TODO I haven't implemented any validation
# TODO I haven't checked the content-type. I assume the client is very kindy with us and always send a json.


@app.route('/ingest', methods=['POST'])
def ingest():
    result = es.index(
        index=request.json['index'],
        body=request.json['payload']
    )

    return result


app.run()
