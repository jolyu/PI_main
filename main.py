import cv2
import image_prosessing_main as ip
import logging_setup as log

def setup():                                   #setup function
    log.initLogging()                                #setUpLogFile()sets up log file
    log.info('Initializing....')                     #log message
    detector = ip.initBlobDetector()                #initialize blob detector
    return detector

def main():
    detector = setup()                          #setup function
    log.info('Setup completed')
    log.info('Now running main')
    


    

if __name__=="__main__":
    main()
