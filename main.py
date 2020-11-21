from elasticsearch import Elasticsearch
from pprint import pformat

es = Elasticsearch()

print(pformat(es.cluster.health()))
