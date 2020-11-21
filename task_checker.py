import logging


class TaskChecker:
    """
    It is a very very very simple function to check the task status.

    I know it is a weird way to check that, and I know
    I am blocking the python application, but it was made just to
    show task management api knowledge.
    """

    def __init__(self, es):
        self.es = es

    def check_task_status(self, task_id):
        completed = False

        while not completed:
            task_status = self.es.tasks.get(task_id=task_id)['completed']
            logging.info('task status: {} - {}'.format(task_id, task_status))
            completed = task_status
