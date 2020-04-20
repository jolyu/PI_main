import cv2 as cv
from logging_framework import logging_setup as log
#import NewTracker as nt

class NewTracker():                     #constructor
    def __init__(self):
        self.trackers = []              #makes a list that should contain all trackers
        self.trackerFail = []           #list to see how many frames a tracker has been nonvalid

    def add(self, trackerObj):          #method for adding trackers
        self.trackers.append(trackerObj)
        self.trackerFail.append(0)      #also needs to see how many frames it has been nonvalid

    def pop(self, ind):                 #method for removing tracker
        if ind > len(self.trackers) or ind <0: 
            pass
        else:
            self.trackers.pop(ind)      #remove tracker and
            self.trackerFail.pop(ind)   #everything related to it
            
    def update(self, filteredFrame):            #method to update multitracker
        boxes = []
        if len(self.trackers) > 0:
            for idx, el in enumerate(self.trackers):
                try:
                    retval, box = el.update(filteredFrame)
                    boxes.append(box)
                    #print("all is good")
                except:
                    print("Something bad happened")
                    log.info("")

                if retval == True:              #checks if tracker managed to track
                    self.trackerFail[idx] = 0   #if track was sucsessful trackerFail is set to zero
                else:
                    self.trackerFail[idx] +=1
            for idx, fails in enumerate(self.trackerFail):  
                if fails > 5:               #needs to iterate throug list of tracker
                    self.pop(idx)           #to see how long they have been wrong
        return boxes         