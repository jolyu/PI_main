import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth

def setupDatabase():
    cred = credentials.Certificate('key.json')
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://jolyu-a8615.firebaseio.com/',
        'databaseAuthVariableOverride': {
        'uid': 'KMz9EwJ5egn5hjAKXd5m7bydVffwnjUz'
        }})
    ref = db.reference()
    return ref

