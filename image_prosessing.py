import cv2
import numpy as np
from logging_framework import logging_setup as log
import time

#global variables
SIMPLE_THRESHOLD_FILTER = 0
CV_OTZU_FILTER = 1
MANUAL_OTZU_FILTER = 2

MORPHOLOGY_ON = True
MORPHOLOGY_OFF = False

def readImageFromPath(path, name, ext, amount):
    #Function for reading images from folder. Example: image_5.jpg -> read_image('path', 'image_', 'jpg', 50)
    
    images = []
    for i in range(amount):
        # try:
        log.info(path + '/' + name + str(i) + ext)
        img = cv2.imread(path + '/' + name + str(i) + ext, 1)
        # check if image was read
        try:
            if img.shape[0]:
                images.append(img)
        except AttributeError:
            pass
    return images

def readImage(img):
    # read image in greyscale 
    img = cv2.imread(img,cv2.IMREAD_GRAYSCALE)            

    #img = img[40:470, 0:610]
    return img

def invertImage(img):
    #Return inversion of an image.
    return cv2.bitwise_not(img)

def manual_otsu_binary(img):
    # Otsu binarization function by calculating threshold

    # check if input image is in grayscale (2D)
    try:
        if img.shape[2]:
            # if there is 3rd dimension
            print('otsu_binary(img) input image should be in grayscale!')
    except IndexError:
        pass  # image doesn't have 3rd dimension - proceed

    #gausian blur
    blur = cv2.GaussianBlur(img, (5, 5), 0)

    # find normalized_histogram, and its cumulative distribution function
    hist = cv2.calcHist([blur], [0], None, [256], [0, 256])
    hist_norm = hist.ravel() / hist.max()
    Q = hist_norm.cumsum()
    bins = np.arange(256)
    fn_min = np.inf
    thresh = -1

    for i in range(1, 255):
        p1, p2 = np.hsplit(hist_norm, [i])  # probabilities
        q1 = Q[i]
        q2 = Q[255] - q1  # cum sum of classes
        b1, b2 = np.hsplit(bins, [i])  # weights
        # finding means and variances
        m1 = np.sum(p1 * b1) / q1
        m2 = np.sum(p2 * b2) / q2
        v1, v2 = np.sum(((b1 - m1) ** 2) * p1) / q1, np.sum(((b2 - m2) ** 2) * p2) / q2
        # calculates the minimization function
        fn = v1 * q1 + v2 * q2
        if fn < fn_min:
            fn_min = fn
            thresh = i

    _, img_thresh1 = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)
    return img_thresh1

def otsu_binary(img):
    # Otsu binarization function.

    #gausian blur
    blur = cv2.GaussianBlur(img, (5, 5), 0)

    # find otsu's threshold value with OpenCV function
    _, otsuImg = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
   
    return otsuImg

def morphologyFilter(img, kernelSize):
    #morphology filter

    # check if input image is in grayscale (2D)
    try:
        if img.shape[2]:
            # if there is 3rd dimension
            print('otsu_binary(img) input image should be in grayscale!')
    except IndexError:
        pass  # image doesn't have 3rd dimension - proceed
    

    morphImgOpen = cv2.morphologyEx(img, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernelSize,kernelSize)))
    morphImgClose = cv2.morphologyEx(morphImgOpen, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernelSize,kernelSize)))
    
    return morphImgClose

def filterImg(img, filterType=0, morphology=False):
    # check if input image is in grayscale (2D)
    # check if input image is in grayscale (2D)
    try:
        if img.shape[2]:
            # if there is 3rd dimension
            print('otsu_binary(img) input image should be in grayscale!')
    except IndexError:
        pass  # image doesn't have 3rd dimension - proceed

    invImg = invertImage(img) #some functions are created to work this way

    #make function to crop img, or make function to remove flir bullshit (do the last)
    invImg = invImg[20:200, 0:300] #temp

    if filterType == SIMPLE_THRESHOLD_FILTER: #regular binary threshold
        _, threshImg = cv2.threshold(invImg, 60, 255, cv2.THRESH_BINARY) #just regular thresholding with random threshold
    elif filterType == CV_OTZU_FILTER: #openCV otzu threshold
        threshImg = otsu_binary(invImg)
    elif filterType == MANUAL_OTZU_FILTER: #manual calculation of otzu threshold value
        threshImg = manual_otsu_binary(invImg)
        
    else:
        #log.critical('HAHAHA! Function input scuffed')
        raise AttributeError('Good luck debugging! Gotta love good error messages ;)')
        
    if morphology:
        morphImg = morphologyFilter(threshImg, 5)
        return morphImg
    return threshImg

def initBlobDetector():
    # Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()

    # Change thresholds
    #params.minThreshold = 65
    #params.maxThreshold = 93

    params.filterByColor = False
    #params.blobColor = False
    # Filter by Area.
    params.filterByArea = False
    params.minArea = 10
    #params.maxArea = 5000

    # Filter by Circularity
    params.filterByCircularity = False
    #params.minCircularity = 0.4
    #params.maxCircularity = 1

    # Filter by Convexity
    params.filterByConvexity = False
    #params.minConvexity = 0.0

    # Filter by Inertia
    params.filterByInertia = False
    params.minInertiaRatio = 0.0

    detector = cv2.SimpleBlobDetector_create(params)

    return detector

def blobDetection(img):
    #function to detect blobs. Returns list of keypoints

    detector = initBlobDetector()

    keyPoints = detector.detect(img)

    #draw detected keypoints as red circles
    #imgKeyPoints = cv2.drawKeypoints(img, keyPoints, np.array([]),(0,0,255), cv2.DRAW_MATCHES_FLAGS_DEFAULT) #uncomment for testing
    #cv2.imshow('blobs', imgKeyPoints)
    return keyPoints

if __name__ == "__main__":
    pass 
'''
    print('Lets have a look at all cases of filter func')
    img = readImage('FLIR0027.jpg')
    cv2.imshow('org',img)

    img1 = filterImg(img, 0, True)
    cv2.imshow('0M', img1)

    img2 = filterImg(img, 1, True)
    cv2.imshow('1M', img2)

    img3 = filterImg(img, 2, True)
    cv2.imshow('2M', img3)

    img4 = filterImg(img, 0, False)
    cv2.imshow('0', img4)

    img5 = filterImg(img, 1, False)
    cv2.imshow('1', img5)

    img6 = filterImg(img, 2, False)
    cv2.imshow('2', img6)

    while True:
        if cv2.waitKey(30) == 27: # exit on ESC                     #avslutter programmet og lukker alle viduer dersom man trykker ESC
            break
    cv2.destroyAllWindows()
'''

        