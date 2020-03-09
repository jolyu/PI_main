import cv2
import image_prosessing_main as ip
import logging_setup as log
import telemetry as tel
import time
import Tracking as track

def setup():                                   #setup function
    log.initLogging()                                #setUpLogFile()sets up log file
    log.info('Initializing....')                     #log message
    detector = ip.initImgProsessing()                #initialize blob detector
    db_ref = tel.setupDatabase()                      #setup database
    trackerType = "KCF"
    multiTracker = cv2.MultiTracker_create()
    birds = 0
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
        rval, frame = vc.read()
        success, boxes = multiTracker.update(frame)
        keypoints = ip.detectStuff(frame, detector)
        newKeypoints = track.removeTrackedBlobs(keypoints,boxes)
        if(not len(newKeypoints==0)):
            birds = birds + len(newKeypoints)
            newBoxes = track.KeypointsToBoxes(newKeypoints)
            for box in newKeypoints:
                multiTracker.add(tf.createTrackerByName(trackerType), frame, newBox)
        print(birds)

        
    cv2.destroyAllWindow()
    vc.release()

    
if __name__=="__main__":
    main()