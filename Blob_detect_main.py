import cv2
import numpy as np
import extra_greyscaling
import logging_setup as log
import time

def initBlobDetector():
     # Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()

    # Change thresholds
    params.minThreshold = 5
    params.maxThreshold = 70

    # Filter by Area.
    params.filterByArea = True
    params.minArea = 30

    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.01

    # Filter by Convexity
    params.filterByConvexity = True
    params.minConvexity = 0.7

    # Filter by Inertia
    params.filterByInertia = False
    params.minInertiaRatio = 0.05


    #determine cv version
    print(cv2.__version__)
    if cv2.__version__.startswith('2'):
        detector = cv2.SimpleBlobDetector(params)
    else:
        detector = cv2.SimpleBlobDetector_create(params)
    
    return detector

def readImage(img):
    # read image
    img = cv2.imread(img, cv2.IMREAD_COLOR)
    img = 255-img
    log.info('Reading image...')
    return img
    
def detect(img, detector):
    # detect suff
    keypoints = detector.detect(img)
    log.info('Detecting keypoints...')
    return keypoints

def initImgProsessing():
    detector = initBlobDetector()
    log.info('Initilizing detector....')
    return detector

if __name__ == "__main__":
    print('not main')
    
        