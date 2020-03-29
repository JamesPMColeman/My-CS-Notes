import time
import random
import logging
import threading
import concurrent.futures
from threading_practice.pipeline_queue import PipelineQueue


def producer(pl, event):
    """This method pretends to receive messages from the network
    at random intervals.
    """
    while not event.is_set():
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        pl.set_message(message, "Producer")

    # producer will loop until the event causes it to exit
    logging.info("Producer received EXIT event. Exiting")


def consumer(pl, event):
    """ This method pretends to save the numer in a database """
    while not event.is_set() or not pl.empty():
        message = pl.get_message("Consumer")
        logging.info("Consumer storing message: %s (queue size = %s",
                     message,
                     pl.qsize(),
                     )
    logging.info("Consumer received EXIT event. Exiting")


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    # logging.getLogger().setLevel(logging.DEBUG)

    pipeline = PipelineQueue()
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as spool:
        spool.submit(producer, pipeline, event)
        spool.submit(consumer, pipeline, event)

        time.sleep(0.1)
        logging.info("Main: about to set event")
        event.set()
