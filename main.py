import cv2
import image_prosessing_main as ip
import logging_setup as log
import telemetry as tel
import time
import Tracking as track
import trackerFunc as tf
def setup():                                   #setup function
    log.initLogging()                                #setUpLogFile()sets up log file
    log.info('Initializing....')                     #log message
    detector = ip.initImgProsessing()                #initialize blob detector
    db_ref = tel.setupDatabase()                      #setup database
    
    return detector, db_ref

def main():
    detector, db_ref = setup()                       #setup function
    
    #declaring some useful variables
    trackerType = "KCF"
    multiTracker = cv2.MultiTracker_create()        #make multitacker
    birds = 0                                       #total number of birds

    log.info('Setup completed.')
    log.info('Now running main.')
    tel.transmit(db_ref, 1000, 200)                 #test of transmit
    vc = cv2.VideoCapture(0)                        #start video camera

    if vc.isOpened():                               #try to get the first frame
        rval, frame = vc.read()                     #frame contains image
    else:
        rval = False                                #camera not working

    while rval:
        img = img[40:180, 30:300]                   #crop image
        cv2.imshow("preview", frame)                #show image
        rval, frame = vc.read()                     #read new frame
        success, boxes = multiTracker.update(frame) #update multitracker
        keypoints = ip.detectBirds(frame, detector) #detect blobs
        newKeypoints = track.removeTrackedBlobs(keypoints,boxes) #make list of all new blobs
        if(not len(newKeypoints==0)):               #if new blobs
            birds = birds + len(newKeypoints)       #new bird(s) detected
            newBoxes = track.KeypointsToBoxes(newKeypoints)     #Get square box around all new blobs
            for box in newBoxes:
                multiTracker.add(tf.createTrackerByName(trackerType), frame, box)   #add tracker
        print(birds)

        
    cv2.destroyAllWindow()
    vc.release()

    
if __name__=="__main__":
    main()