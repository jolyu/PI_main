import cv2
import image_prosessing_main as ip
import logging_setup as log
import time

def setup():                                   #setup function
    log.initLogging()                                #setUpLogFile()sets up log file
    log.info('Initializing....')                     #log message
    detector = ip.initImgProsessing()                #initialize blob detector
    return detector

def main():
    detector = setup()                          #setup function
    log.info('Setup completed')
    log.info('Now running main')

    print('main')

    while True:
                    
        i=18
        while i<40:
            i=i+1
            try:
                imStr = 'FLIR00' + str(i) + '.jpg'
                img = ip.readImage(imStr)
                points = ip.detectStuff(img, detector)
                numBlobs = len(points)
                print(imStr, ' ', numBlobs)
                logString = imStr + ': ''' + str(numBlobs) + ' blobs detected'
                log.info(logString)
                cv2.imshow("preview", img)
                while cv2.waitKey() != 27:
                    break  
                cv2.destroyAllWindows()
            except:
                logString = imStr + ': blob detection failed'
                log.warning(logString)
                pass

if __name__=="__main__":
    main()
