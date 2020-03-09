import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth
import logging as log
from datetime import datetime

def setupDatabase():
    cred = credentials.Certificate('key.json')
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://jolyu-a8615.firebaseio.com/',
        'databaseAuthVariableOverride': {
        'uid': 'KMz9EwJ5egn5hjAKXd5m7bydVffwnjUz'
        }})
    ref = db.reference()
    return ref

def transmit(db_ref, numBlobs, sensorStuff):
        try:
            
            data = {
                'time': datetime.timestamp(datetime.now()),
                'birds': numBlobs,
            }
            dateTimeObj = datetime.now()
            timestampStr = dateTimeObj.strftime("%H%M%S%f%b%d%Y")
            db_ref.child(timestampStr).set(data)
            log.info('Uploaded to database')
        except:
            log.critical('Could not upload to database')