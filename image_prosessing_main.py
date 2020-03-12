import cv2
import numpy as np
import extra_greyscaling
import logging_setup as log
import time

def initBlobDetector():
    # Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()

    # Change thresholds
    params.minThreshold = 0
    params.maxThreshold = 40


    # Filter by Area.
    params.filterByArea = True
    params.minArea = 100

    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.1

    # Filter by Convexity
    params.filterByConvexity = True
    params.minConvexity = 0.87

    # Filter by Inertia
    params.filterByInertia = True
    params.minInertiaRatio = 0.01


    #determine cv version
    print(cv2.__version__)
    if cv2.__version__.startswith('2'):
        detector = cv2.SimpleBlobDetector(params)
    else:
        detector = cv2.SimpleBlobDetector_create(params)
    
    return detector

def readImage(img):
    # read image in greyscale 
    img = cv2.imread(img,cv2.IMREAD_GRAYSCALE)            
                                                    #put fancy G2B algorithm here 
    img = cv2.resize(img, (650,500))
    img = 255-img
    log.info('Reading image...')
    #img = img[40:470, 0:610]
    return img
    
def detectStuff(img, detector):
    # detect suff
    keyPoints = detector.detect(img)
    log.info('Detecting keypoints...')
    #draw detected keypoints as red circles
    #imgKeyPoints = cv2.drawKeypoints(img, keypoints, np.array([]),(0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS) #uncomment for testing
    return keyPoints

def initImgProsessing():
    detector = initBlobDetector()
    log.info('Initilizing detector....')
    return detector

if __name__ == "__main__":
    print("not main")
        