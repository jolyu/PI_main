import cv2

def KeypointsToBoxes(keypoints):
    boxes = []
    for keypoint in keypoints:
        point = keypoint.pt
        size = keypoint.size()
        box = (point[0],point[1],size,size)
        boxes.append(box)
    return boxes
