import data_ingestion
import reindex_client
import task_management_client
import update_client
from elasticsearch import Elasticsearch
import logging


if __name__ == '__main__':
    es = Elasticsearch()
    target_index = 'target_index'

    data_ingestion.init_database(es)
    reindex_task_id = reindex_client.execute(es, target_index)
    task_management_client.check_task_status(es, reindex_task_id)

    update_task_id = update_client.execute(es, target_index)
    task_management_client.check_task_status(es, update_task_id)

    logging.info('finished initial script')
