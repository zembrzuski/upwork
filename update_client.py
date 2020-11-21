from elasticsearch import Elasticsearch
from datetime import datetime

es = Elasticsearch()


update_definition = {
        "query": {
            "match_all": {}
        },
        "script": {
            "source": "DateFormat df = new SimpleDateFormat(\"yyyy-MM-dd'T'HH:mm:ss.SSS'Z'\"); "
                      "Date date = new Date(); "
                      "ctx._source.last_updated=df.format(date);",
            "lang": "painless"
        }
    }


def execute():
    # TODO slicing, throttling, etc.

    result = es.update_by_query(
        index='reidexed_projects',
        body=update_definition,
        wait_for_completion=False
    )

    return result['task']
