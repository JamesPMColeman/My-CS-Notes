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

    logging.info("Main: before creating the thread")
    yello_yarn = threading.Thread(target=practice_thread, args=(1,),
                                  daemon=True)
    logging.info("Main: before running thread")
    yello_yarn.start()
    logging.info("Main: wait for the thread to finish")
    yello_yarn.join()
    logging.info("Main: all done")
