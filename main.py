import cv2
from image_prosessing import blob_detection as ip
from image_prosessing import filters
from logging_framework import logging_setup as log
import time
import Tracking as track
import trackerFunc as tf
import multitracker as mt

def setup():                                            #setup function
    log.initLogging()                                   #setUpLogFile()sets up log file
    log.info('Initializing....')                        #log message
   
    return

def main():
    setup()
    
    #declaring some useful variables
    trackerType = "CSRT" 
    multiTracker = mt.NewTracker()                      #make multitacker
    birds = 0                                           #total number of birds

    log.info('Setup completed. \n Now running main:')

    vc = cv2.VideoCapture(1)                            #start video camera
    #vc = cv2.VideoCapture("video2.avi")     
    if vc.isOpened():                                   #try to get the first frame
        rval, frame = vc.read()   
        frame = cv2.resize(frame, (650,500))            #frame contains image
        
        filters.check2D(frame)                          # image doesn't have 3rd dimension - proceed

    else:
        rval = False                                    #camera not working

    while rval:
        rval, frame = vc.read()                         #read new frame
        cv2.imshow("preview", frame)                    #show image
        #frame = cv2.resize(frame, (650,500))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
         
        filteredFrame = filters.filterImg(frame, filters.CV_OTZU_FILTER, filters.MORPHOLOGY_ON) #se globale variabler i image_prosessing.py. midterste er type filter som skal brukes, og siste avgjør om man skal ha morphology operasjoner
        cv2.imshow("filt", filteredFrame)
        boxes = multiTracker.update(filteredFrame)                  #update multitracker
        keypoints = ip.blobDetection(filteredFrame) 
        newKeypoints = track.removeTrackedBlobs(keypoints,boxes)    #make list of all new blobs
        if len(newKeypoints)>0:                                     #if new blobs
            birds = birds + len(newKeypoints)                       #new bird(s) detected
            newBoxes = track.KeypointsToBoxes(newKeypoints)         #Get square box around all new blobs
            for box in newBoxes:
                multiTracker.add(tf.createTrackerByName(trackerType))   #add tracker
                ok = multiTracker.trackers[len(multiTracker.trackers)-1].init(filteredFrame, box) #initialize tracker
        #birds=len(keypoints)
        print(birds)
        #birds=0
        if cv2.waitKey(30) == 27: # exit on ESC                     #avslutter programmet og lukker alle viduer dersom man trykker ESC
            break

        
    cv2.destroyAllWindows()
    vc.release()

if __name__=="__main__":
    main()