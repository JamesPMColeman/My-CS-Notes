import threading
import logging
import time


def practice_thread(name):
    logging.info("Thread %s: starting", name)
    time.sleep(5)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    spool = list()
    for index in range(3):
        logging.info("Main: create and start thread %d", index)
        yellow_yarn = threading.Thread(target=practice_thread,
                                      args=(index,))
        spool.append(yellow_yarn)
        yellow_yarn.start()

    for index, thread in enumerate(spool):
        logging.info("Main: before joining thread %d", index)
        thread.join()
        logging.info("Main: thread %d done", index)
