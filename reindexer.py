
class Reindexer:
    def __init__(self, es):
        self.es = es

    def execute(self, target_index, slices=5):
        body = {
            "source": {"index": "project_*"},
            "dest": {"index": target_index}
        }

        result = self.es.reindex(
            body=body,
            wait_for_completion=False,
            request_timeout=300,
            slices=slices)

        return result['task']
