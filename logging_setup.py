import logging

def initLogging(): 
    logging.basicConfig(filename='test.log', format='%(levelname)s %(asctime)s %(message)s', level=logging.INFO)