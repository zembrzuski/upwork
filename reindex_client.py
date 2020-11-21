from elasticsearch import Elasticsearch
from datetime import datetime

es = Elasticsearch()

# TODO inject es client.


def execute():

    # TODO control better the throttling

    source_index = 'project_*'
    destination_index = 'reidexed_projects'

    body = {
        "source": {"index": source_index},
        "dest": {"index": destination_index}
    }

    result = es.reindex(
        body=body,
        wait_for_completion=False,
        request_timeout=300,
    )

    return result['task']
