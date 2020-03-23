import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth
import logging as log
from datetime import datetime

def setupDatabase():
    cred = credentials.Certificate('key.json')              #file with API-key and more
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://jolyu-a8615.firebaseio.com/',
        'databaseAuthVariableOverride': {
        'uid': 'KMz9EwJ5egn5hjAKXd5m7bydVffwnjUz'           #uid is used as a 'password' to database
        }})                                                 #only this uid can write, but all can read
    ref = db.reference()        #reference to the database we are using
    return ref

def transmit(db_ref, numBlobs, sensorStuff):
        try:
            
            data = {
                'time': datetime.timestamp(datetime.now()),     #data to add to database
                'birds': numBlobs,
            }
            timestampStr = str(datetime.timestamp(datetime.now()))  #use timestamp as database key
            db_ref.child(timestampStr).set(data)                    #add data to database
            log.info('Uploaded to database')
        except:
            log.critical('Could not upload to database')