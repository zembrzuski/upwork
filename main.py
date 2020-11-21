import data_ingestion
import reindex_client
import task_management_client
import update_client

# TODO throttling, slicing, etc.

# data_ingestion.init_database()
task_id = reindex_client.execute()
task_management_client.check_task_status(task_id)
update_client.execute()
