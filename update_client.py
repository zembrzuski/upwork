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


def execute(es, target_index, slices=5):
    result = es.update_by_query(
        index=target_index,
        body=update_definition,
        wait_for_completion=False,
        slices=5
    )

    return result['task']
