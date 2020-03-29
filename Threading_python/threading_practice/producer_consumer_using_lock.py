import random
import logging
from threading_practice.pipeline import Pipeline
import concurrent.futures

SENTINEL = object


def producer(pipeline):
    """This method pretends to receive messages from the network
    at random intervals.
    """
    for index in range(10):
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        pipeline.set_message(message, "Producer")

    # Send a sentinel message to tell the consumer we're done
    pipeline.set_message(SENTINEL, "Producer")


def consumer(pipeline):
    """ This method pretends to save the numer in a database """
    message = 0
    while message is not SENTINEL:
        message = pipeline.get_message("Consumer")
        if message is not SENTINEL:
            logging.info("Consumer storing message: %s", message)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    # logging.getLogger().setLevel(logging.DEBUG)

    pipeline = Pipeline()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as spool:
        spool.submit(producer, pipeline)
        spool.submit(consumer, pipeline)

