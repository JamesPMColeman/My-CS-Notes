import threading
import logging


class Pipeline:
    """
    This class allows a single element to pass between producer and consumer.
    """
    def __init__(self):
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()

    def get_message(self, name):
        logging.debug("%s: about to acquire consumer lock", name)
        self.consumer_lock.acquire()
        logging.debug("%s: has consumer lock", name)
        message = self.message
        logging.debug("%s: about to release producer lock", name)
        self.producer_lock.release()
        logging.debug("%s: producer lock released", name)
        return message

    def set_message(self, message, name):
        logging.debug("%s: about to acquire producer lock", name)
        self.producer_lock.acquire()
        logging.debug("%s: has producer lock", name)
        self.message = message
        logging.debug("%s: about to release consumer lock", name)
        self.consumer_lock.release()
        logging.debug("%s: consumer lock released", name)
