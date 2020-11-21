from datetime import datetime
import logging


class DataIngestion:
    """
    Script responsible for initial data ingestion.
    """

    def __init__(self, es):
        self.es = es

    def init_database(self, number_of_documents_per_index):
        logging.info('creating indices')
        self.__insert_a_hundred_documents(1, number_of_documents_per_index)
        self.__insert_a_hundred_documents(2, number_of_documents_per_index)
        self.__insert_a_hundred_documents(3, number_of_documents_per_index)
        logging.info('finished indices creation')

    def __insert_a_hundred_documents(self, index_counter, number_of_documents_per_index):
        index_name = 'project_{}'.format(index_counter)

        for i in range(0, number_of_documents_per_index):
            self.__simple_index(index_name, i)

    def __simple_index(self, index_name, i):
        body = {
            'alfa': 'a',
            'beta': 'b',
            'counter': i,
            'original_index': index_name,
            'last_updated': datetime.now()
        }

        self.es.index(index=index_name, body=body)
