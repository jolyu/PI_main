import cv2
import image_prosessing_main as ip
import logging_setup as ls

def setup():
    ls.initLogging() #setUpLogFile()sets up log file


def main():
    setup()
    ls.info("test")

if __name__=="__main__":
    main()
