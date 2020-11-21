from elasticsearch import Elasticsearch
from flask import Flask
from flask import request

es = Elasticsearch()
app = Flask(__name__)


@app.route('/ingest', methods=['POST'])
def ingest():
    result = es.index(
        index=request.json['index'],
        body=request.json['payload'])

    return result


if __name__ == '__main__':
    app.run()
