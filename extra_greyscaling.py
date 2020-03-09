import cv2

def otsu(img,thresh,max):
    img = cv2.GaussianBlur(img,(5,5),0)
    ret, img =  cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)  
    return img 

def mean(img,thresh,max):
    img = cv2.medianBlur(img,5)
    ret, img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = cv2.adaptiveThreshold(img,max,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,201,2)
    return img

def gauss(img,thresh,max):
    img = cv2.medianBlur(img,5)
    ret, img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = cv2.adaptiveThreshold(img,max,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,201,2)
    return img

if __name__ == "__main__":
    print('wrong place')