import cv2

types = ['BOOSTING', 'MIL', 'KCF','TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
 
def createTrackerByName(trackerType):

    # Create a tracker based on tracker name
    if trackerType == types[0]:
        tracker = cv2.TrackerBoosting_create()
    elif trackerType == types[1]: 
        tracker = cv2.TrackerMIL_create()
    elif trackerType == types[2]:
        tracker = cv2.TrackerKCF_create()
    elif trackerType == types[3]:
        tracker = cv2.TrackerTLD_create()
    elif trackerType == types[4]:
        tracker = cv2.TrackerMedianFlow_create()
    elif trackerType == types[5]:
        tracker = cv2.TrackerGOTURN_create()
    elif trackerType == types[6]:
        tracker = cv2.TrackerMOSSE_create()
    elif trackerType == types[7]:
        tracker = cv2.TrackerCSRT_create()
    else:
        tracker = None
        print('Incorrect tracker name')
        print('Available trackers are:')
        for t in types:
            print(t)
     
    return tracker

if __name__ == "__main__":
    print("Why are you gay?")