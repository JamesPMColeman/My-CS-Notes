import logging
import queue


class PipelineQueue(queue.Queue):
    """
    This class allows a single element to pass between producer and consumer.
    """
    def __init__(self):
        super().__init__(maxsize=10)

    def get_message(self, name):
        logging.debug("%s: about to acquire a message from the queue", name)
        value = self.get()
        logging.debug("%s: received %d from the queue", name, value)
        return value

    def set_message(self, value, name):
        logging.debug("%s: about to about to add %d to the queue", name, value)
        self.put(value)
        logging.debug("%s: added %d to the queue", name, value)
