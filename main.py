import cv2
import image_prosessing_main as ip
import logging_setup as log
import setup_database as db
import time

def setup():                                   #setup function
    log.initLogging()                                #setUpLogFile()sets up log file
    log.info('Initializing....')                     #log message
    detector = ip.initImgProsessing()                #initialize blob detector
    db_ref = db.setupDatabase()                      #setup database
    return detector, db_ref

def main():
    detector, db_ref = setup()                          #setup function
    log.info('Setup completed')
    log.info('Now running main')

        
if __name__=="__main__":
    main()
