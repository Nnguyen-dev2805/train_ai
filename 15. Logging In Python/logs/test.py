from logger import logging

def add(a,b):
    logging.debug("The addition operation is taking place")
    return a + b

logging.debug("This is a debug message from the test module")
add(10,15)
