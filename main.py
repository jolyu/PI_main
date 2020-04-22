import cv2
from image_prosessing import blob_detection as ip
from image_prosessing import filters
from logging_framework import logging_setup as log
from tracking import trackerFunc as tf
from tracking import multitracker as mt
from tracking import Tracking as track
import time

def setup():                                            #setup function
    log.init_logging()                                   #setUpLogFile()sets up log file
    log.info('Initializing....')                        #log message
   
    return

def main():
    setup()
    
    #declaring some useful variables
    trackerType = "CSRT" 
    multiTracker = mt.NewTracker()                      #make multitacker
    birds = 0                                           #total number of birds

    log.info('Setup completed. Now running main')

    #vc = cv2.VideoCapture(0)                            #start video camera
    vc = cv2.VideoCapture("test_video/video9_edit1.mp4")     


    if vc.isOpened():                                   #try to get the first frame
        rval, frame = vc.read()   
        
        filters.check_2D(frame)                          # image doesn't have 3rd dimension - proceed

    else:
        rval = False                                    #camera not working

    while rval:

        rval, frame = vc.read()                         #read new frame
        cv2.imshow("preview", frame)                    #show image
        
         
        #filters
        #filteredFrame = filters.filter_img(frame, filters.MANUAL_OTZU_FILTER, filters.MORPHOLOGY_ON) #se globale variabler i image_prosessing.py. midterste er type filter som skal brukes, og siste avgjør om man skal ha morphology operasjoner
        filteredFrame = filters.filter_img2(frame)
        cv2.imshow("filt", filteredFrame)

        #tracking
        boxes = multiTracker.update(filteredFrame)                  #update multitracker
        keypoints = ip.blob_detection(filteredFrame) 
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
        '''if cv2.waitKey(10) == ord('p'): # exit on ESC                     #avslutter programmet og lukker alle viduer dersom man trykker ESC
                while True:
                    if cv2.waitKey(10) == ord('p'):
                        break'''
        
        '''while True:
                if cv2.waitKey(10) == ord('a'):
                    break
                '''
        if cv2.waitKey(30) == 27: # exit on ESC                     #avslutter programmet og lukker alle viduer dersom man trykker ESC
            break

        
    cv2.destroyAllWindows()
    vc.release()

if __name__=="__main__":
    main()