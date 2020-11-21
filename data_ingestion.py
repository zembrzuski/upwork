from elasticsearch import Elasticsearch
from datetime import datetime

es = Elasticsearch()

# TODO inject es client.


def init_database():
    insert_a_hundred_documents(1)
    insert_a_hundred_documents(2)
    insert_a_hundred_documents(3)

    print('do-it')


def insert_a_hundred_documents(index_counter):
    # TODO it would be better if I could generate random data
    index_name = 'project_{}'.format(index_counter)
    for i in range(1, 100):
        __simple_index(index_name, i)


def __simple_index(index_name, i):
    # TODO better to use bulk api

    body = {
        'alfa': 'a',
        'beta': 'b',
        'counter': i,
        'original_index': index_name,
        'last_updated': datetime.now()
    }

    es.index(
        index=index_name,
        body=body
    )

    print(body)
