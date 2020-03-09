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

    #cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:

    cv2.imshow("preview", frame)

    rval, frame = vc.read()
    keypoints = ip.detectStuff(frame, detector)
    print('number of blobs ', len(keypoints))
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

cv2.destroyAllWindow()
vc.release()

    
if __name__=="__main__":
    main()
