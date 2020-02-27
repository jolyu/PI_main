import cv2
import image_prosessing_main as ip
import logging_setup as ls

def setup():
    ls.initLogging() #setUpLogFile()
    #willYouBeWifi()  set up telemetry link
    #setupSensors()   set up sensor stuff
    #setUpCamera()    set up camera link?
    blobDetector = ip.initImgProsessing() #init img prosessing, returning blobDetector = trash


def main():
    print("main")
    #camera()?
    #prosessFrame()? slå sammen med den over?
    #sensorStuff() 
    #transmitData()? 
    #reciveveData()? (slå sammen med den over?)

if __name__=="__main__":
    setup()
    main()
