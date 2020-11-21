import logging
import time
from elasticsearch.exceptions import ConnectionError


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

    def block_until_elasticsearch_is_healthy(self):
        """"
        Weird way of orchestrating containers because docker-compose does not
        have a sofisticated way to do that. I need to wait not only the boot
        of the container, but also the boot of the application inside the container.
        """

        while True:
            try:
                if self.es.cluster.health()['status'] == 'green':
                    return True
            except ConnectionError:
                logging.info('waiting for elasticsearch boot')
                time.sleep(3)
