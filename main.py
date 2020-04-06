import cv2
import image_prosessing as ip
import logging_setup as log
#import telemetry as tel
import time
import Tracking as track
import trackerFunc as tf
import multitracker as mt
def setup():                                   #setup function
    log.initLogging()                                #setUpLogFile()sets up log file
    log.info('Initializing....')                     #log message
    #db_ref = tel.setupDatabase()                      #setup database
    return
    #return db_ref

def main():
    #db_ref = setup()                       #setup function
    setup()
    
    #declaring some useful variables
    trackerType = "KCF"
    multiTracker = mt.NewTracker()        #make multitacker
    birds = 0                                       #total number of birds

    log.info('Setup completed.')
    log.info('Now running main.')
    #tel.transmit(db_ref, 1000, 200)                 #test of transmit
    vc = cv2.VideoCapture(0)                        #start video camera
    
    if vc.isOpened():                               #try to get the first frame
        rval, frame = vc.read()   
        frame = cv2.resize(frame, (650,500))                  #frame contains image
        try:
            if frame.shape[2]:
            # if there is 3rd dimension
                print('otsu_binary(img) input image should be in grayscale!')
        except IndexError:
            pass  # image doesn't have 3rd dimension - proceed

    else:
        rval = False                                #camera not working

    while rval:
        rval, frame = vc.read()                     #read new frame
        cv2.imshow("preview", frame)                #show image
        frame = cv2.resize(frame, (650,500))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        filteredFrame = ip.filterImg(frame, ip.CV_OTZU_FILTER, ip.MORPHOLOGY_ON) #se globale variabler i image_prosessing.py. midterste er type filter som skal brukes, og siste avgjør om man skal ha morphology operasjoner
        cv2.imshow("filt", filteredFrame)
        boxes = multiTracker.update(filteredFrame)         #update multitracker
        keypoints = ip.blobDetection(filteredFrame)
        newKeypoints = track.removeTrackedBlobs(keypoints,boxes) #make list of all new blobs
        if not(len(newKeypoints)==0):               #if new blobs
            birds = birds + len(newKeypoints)       #new bird(s) detected
            newBoxes = track.KeypointsToBoxes(newKeypoints)     #Get square box around all new blobs
            for box in newBoxes:
                multiTracker.add(tf.createTrackerByName(trackerType))   #add tracker
                ok = multiTracker.trackers[len(multiTracker.trackers)-1].init(filteredFrame, box) #initialize tracker
        birds=len(keypoints)
        print(birds)
        birds=0
        if cv2.waitKey(30) == 27: # exit on ESC                     #avslutter programmet og lukker alle viduer dersom man trykker ESC
            break

        
    cv2.destroyAllWindows()
    vc.release()

    
if __name__=="__main__":
    main()