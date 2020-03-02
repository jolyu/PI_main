import logging

def initLogging(): 
    logging.basicConfig(filename='logFile.log', format='%(levelname)s %(asctime)s %(message)s', level=logging.INFO)     #oppretter logfil
    info('Program started')                                                                                             #første melding

def info(streng):                                                                                                       #for å kunne bruke log.info() fremfor log.logging.info() i main.py
    logging.info(streng)

def warning(streng):
    logging.warning(streng)

def critical(streng):
    logging.critical(streng)

def debug(streng):
    logging.debug(streng)

if __name__=="__main__":
    '''initLogging()
    info('info message')
    debug('debug message')
    warning('warning message')
    critical('error message')'''
    print('not main')
