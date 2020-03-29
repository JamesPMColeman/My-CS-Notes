import concurrent.futures
import threading
import logging
import time


def practice_thread(name):
    logging.info("Thread %s: starting", name)
    time.sleep(5)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format,
                        level=logging.INFO,
                        datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(practice_thread, range(3))
