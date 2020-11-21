
class UpdateClient:

    def __init__(self, es):
        self.es = es
        self.update_definition = {
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

    def execute(self, target_index, slices=5):
        result = self.es.update_by_query(
            index=target_index,
            body=self.update_definition,
            wait_for_completion=False,
            slices=slices)

        return result['task']
