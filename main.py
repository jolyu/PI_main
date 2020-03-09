import cv2
import image_prosessing_main as ip
import logging_setup as log
#import telemetry as tel
import time
import Tracking as track

def setup():                                   #setup function
    log.initLogging()                                #setUpLogFile()sets up log file
    log.info('Initializing....')                     #log message
    detector = ip.initImgProsessing()                #initialize blob detector
    #db_ref = tel.setupDatabase()                      #setup database
    return detector
    #return detector, db_ref

def main():
    #detector, db_ref = setup()                       #setup function
    detector = setup()
    #declaring some useful variables
    trackerType = "KCF"
    multiTracker = cv2.MultiTracker_create()
    birds = 0

    log.info('Setup completed.')
    log.info('Now running main.')
    vc = cv2.VideoCapture(0)

    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        frame = frame[40:180, 30:300]
        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        keypoints = ip.detectStuff(frame, detector)
        print(len(keypoints))

        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break

    cv2.destroyAllWindow()
    vc.release()

    
if __name__=="__main__":
    main()