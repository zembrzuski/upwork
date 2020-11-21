import logging


def check_task_status(es, task_id):
    """
    It is a very very very simple function to check the task status.

    I know it is a weird way to check that, and I know
    I am blocking the python application, but it was made just to
    show task management api knowledge.
    """
    completed = False

    while not completed:
        task_status = es.tasks.get(task_id=task_id)['completed']
        logging.info('task status: {} - {}'.format(task_id, task_status))
        completed = task_status

    print('ok')
