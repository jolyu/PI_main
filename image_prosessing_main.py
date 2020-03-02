import cv2
from extra_greyscaling import*

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
    if cv2.__version__.startswith('2'):
        detector = cv2.SimpleBlobDetector(params)
    else:
        detector = cv2.SimpleBlobDetector_create(params)
    
    return detector

def readImage(img):
    # read image IN COLOR
    img = cv2.imread('FLIR0027.jpg', cv2.IMREAD_COLOR)
    # put fancy B2G algorithm 
    img = cv2.resize(img, (650,500))
    img = 255-img
    img = img[40:470, 0:610]
    return img
    
def detectStuff(img, detector):
    # detect suff
    keypoints = detector.detect(img)
    print(len(keypoints))
    #draw detected keypoints as red circles
    imgKeyPoints = cv2.drawKeypoints(img, keypoints, np.array([]),(0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    return imgKeyPoints

def initImgProsessing():
    detector = initBlobDetector()
    return detector

if __name__ == "__main__":
    while(True):
        readImage()
        