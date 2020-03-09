import cv2
import Blob_detect_main as ip
import logging_setup as log
import telemetry as tel
import time


def setup():                                   #setup function
    log.initLogging()                                #setUpLogFile()sets up log file
    log.info('Initializing....')                     #log message
    detector = ip.initImgProsessing()                #initialize blob detector
    db_ref = tel.setupDatabase()                      #setup database
    return detector, db_ref

def main():
    detector, db_ref = setup()                       #setup function
    log.info('Setup completed.')
    log.info('Now running main.')
    tel.transmit(db_ref, 1000, 200)

    
if __name__=="__main__":
    main()
