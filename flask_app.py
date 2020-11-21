from elasticsearch import Elasticsearch
from flask import Flask
from flask import request
import os

es_host = os.getenv('ES_HOSTS')
es = Elasticsearch(hosts=es_host)
app = Flask(__name__)


@app.route('/ingest', methods=['POST'])
def ingest():
    result = es.index(
        index=request.json['index'],
        body=request.json['payload'])

    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0')
