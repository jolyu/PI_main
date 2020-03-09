import cv2

def KeypointsToBoxes(keypoints):
    boxes = []
    for keypoint in keypoints:
        point = keypoint.pt
        size = int(keypoint.size())
        box = (int(point[0])- (size/2),int(point[1]) - (size/2),size,size)
        boxes.append(box)
    return boxes

