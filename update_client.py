from elasticsearch import Elasticsearch
from datetime import datetime

es = Elasticsearch()


def execute():
    # TODO slicing, throttling, etc.

    search_definition = {
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

    result = es.update_by_query(
        index='reidexed_projects',
        body=search_definition,
        wait_for_completion=True
    )

    searched = es.search(
        index='reidexed_projects',
        size=10000
    )
    print('coi')

    print(result)
