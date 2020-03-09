import cv2


def KeypointsToBoxes(keypoints):
    Boxes = []
    for keypoint in keypoints:
        Point = keypoint.pt
        size = keypoint.size()
        Box = (Point[0],Point[1],size,size)
        Boxes.append(Box)
    return Boxes
