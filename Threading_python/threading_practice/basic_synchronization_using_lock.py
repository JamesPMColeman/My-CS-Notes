import concurrent.futures
import threading
import logging
import time


class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def locked_update(self, name):
        logging.info("Thread %s: starting update", name)
        logging.debug("Thread %s about to lock", name)
        with self._lock:
            logging.debug("Thread %s has lock", name)
            local_copy = self.value
            local_copy += 1
            time.sleep(2)
            self.value= local_copy
            logging.debug("Thread %s about to release lock", name)
        logging.debug("Thread %s has released lock", name)
        logging.info("Thread %s: finishing update", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format,
                        level=logging.DEBUG,
                        datefmt="%H:%M:%S")

    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d.", database.value)

    # two threads are going run .update() at the same time
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as needle:
        for index in range(2):
            # .submit() allows both positional and named arguments
            # to be passed the function running in the thread
            needle.submit(database.locked_update, index)

    logging.info("Testing update Dending value is %d.", database.value)