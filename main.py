import data_ingestion
import reindex_client
import task_management_client
import update_client

# TODO throttling, slicing, etc.
# TODO write about possible timezone issues.

# data_ingestion.init_database()
reindex_task_id = reindex_client.execute()
task_management_client.check_task_status(reindex_task_id)

update_task_id = update_client.execute()
task_management_client.check_task_status(update_task_id)

print('finished')
