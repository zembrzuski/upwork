from datetime import datetime


def init_database(es):
    insert_a_hundred_documents(1)
    insert_a_hundred_documents(2)
    insert_a_hundred_documents(3)


def insert_a_hundred_documents(es, index_counter):
    index_name = 'project_{}'.format(index_counter)

    for i in range(1, 100):
        __simple_index(es, index_name, i)


def __simple_index(es, index_name, i):
    body = {
        'alfa': 'a',
        'beta': 'b',
        'counter': i,
        'original_index': index_name,
        'last_updated': datetime.now()
    }

    es.index(index=index_name, body=body)
