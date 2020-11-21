def execute(es, target_index, slices=5):
    source_index = 'project_*'

    body = {
        "source": {"index": source_index},
        "dest": {"index": target_index}
    }

    result = es.reindex(
        body=body,
        wait_for_completion=False,
        request_timeout=300,
        slices=slices)

    return result['task']
