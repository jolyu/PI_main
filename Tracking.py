import cv2

def KeypointsToBoxes(keypoints):
    boxes = []
    for keypoint in keypoints:
        point = keypoint.pt
        size = int(keypoint.size())
        box = (int(point[0])- (size/2),int(point[1]) - (size/2),size,size)
        boxes.append(box)
    return boxes

def removeTrackedBlobs(keypoints, boxes):
    newKeypoints = []
    try:
        for points in keypoints:
            x,y = points.pt
            for box in boxes:
                xb,yb,wb,hb = box
                if xb<x and x<xb+wb and yb<y and y<yb+hb:
                    newKeypoints.append(points)
    except:
        pass
    return newKeypoints