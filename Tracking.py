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
    diff = []
    try:
        for points in keypoints:
            x,y = points
            for box in boxes:
                xb,yb,wb,hb = box
                if xb<x and x<xb+wb and yb<y and y<yb+hb:
                    diff.append(points)
        for point in keypoints:
            if point not in diff:
                newKeypoints.append(point)
    except:
        pass
    return newKeypoints