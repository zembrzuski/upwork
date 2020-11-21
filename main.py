from data_ingestion import DataIngestion
from reindexer import Reindexer
from task_checker import TaskChecker
from update_client import UpdateClient
from elasticsearch import Elasticsearch
import logging
import sys


def __configure_log():
    root = logging.getLogger()
    root.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)


if __name__ == '__main__':
    __configure_log()
    es = Elasticsearch()
    data_ingestion = DataIngestion(es)
    reindex_client = Reindexer(es)
    task_management_client = TaskChecker(es)
    update_client = UpdateClient(es)

    number_of_documents_per_index = 100
    target_index = 'target_index'

    data_ingestion.init_database(number_of_documents_per_index)

    reindex_task_id = reindex_client.execute(target_index)
    task_management_client.check_task_status(reindex_task_id)

    update_task_id = update_client.execute(target_index)
    task_management_client.check_task_status(update_task_id)

    logging.info('finished initial script')
