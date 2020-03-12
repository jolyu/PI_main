import cv2
import numpy as np
import extra_greyscaling
import logging_setup as log
import time

def nothing(x):
    pass

def initBlobDetector():
    cv2.namedWindow('preview')
    cv2.createTrackbar('minThresh', 'preview', 0, 255, nothing)
    cv2.createTrackbar('maxThresh', 'preview', 0, 255, nothing)
    cv2.createTrackbar('minArea', 'preview', 0, 200, nothing)
    cv2.createTrackbar('minCirc', 'preview', 0, 1, nothing)
    cv2.createTrackbar('minConv', 'preview', 0, 1, nothing)
    cv2.createTrackbar('minRatio', 'preview', 0, 255, nothing)
    # Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()
    '''
    # Change thresholds
    params.minThreshold = 100
    params.maxThreshold = 255


    # Filter by Area.
    params.filterByArea = True
    params.minArea = 20

    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.1

    # Filter by Convexity
    params.filterByConvexity = True
    params.minConvexity = 0.87

    # Filter by Inertia
    params.filterByInertia = True
    params.minInertiaRatio = 0.01

    '''
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
    img = img[40:470, 0:610]
    return img
    
def detectStuff(img, detector):
    # detect suff
    
    minThresh = cv2.getTrackbarPos('minThresh', 'preview')
    maxThresh = cv2.getTrackbarPos('maxThresh', 'preview')
    minArea = cv2.getTrackbarPos('minArea', 'preview')
    minCirc = cv2.getTrackbarPos('minCirc', 'preview')
    minConv = cv2.getTrackbarPos('minConv', 'preview')
    minRatio = cv2.getTrackbarPos('minRatio', 'preview')

    params = cv2.SimpleBlobDetector_Params()
# Change thresholds
    params.minThreshold = minThresh
    params.maxThreshold = maxThresh
    # Filter by Area.
    params.filterByArea = True
    params.minArea = minArea
    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = minCirc
    # Filter by Convexity
    params.filterByConvexity = True
    params.minConvexity = minConv
    # Filter by Inertia
    params.filterByInertia = True
    params.minInertiaRatio = minRatio
    # detect suff
    detector = cv2.SimpleBlobDetector_create(params)

    keyPoints = detector.detect(img)
    log.info('Detecting keypoints...')
    #draw detected keypoints as red circles
    #imgKeyPoints = cv2.drawKeypoints(img, keyPoints, np.array([]),(33,33,33), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS) #uncomment for testing
    return keyPoints

def initImgProsessing():
    detector = initBlobDetector()
    log.info('Initilizing detector....')
    return detector

if __name__ == "__main__":
    print("not main")
        