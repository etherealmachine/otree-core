"""
Sends subsession events to Firebase.
"""
from firebase import firebase
import logging
import threading
import time


logger = logging.getLogger(__name__)

_FIREBASE_URL = 'https://otree.firebaseio.com'
_FIREBASE_SECRET = 'uXop5iUjKkGfH20sFmdCMenX7QnUWmnWDde76WQR'


class EventEmitter(threading.Thread):

    def __init__(self, seconds):
        super(EventEmitter, self).__init__()
        self.seconds = seconds
        self.firebase = firebase.FirebaseApplication(
        	_FIREBASE_URL,
        	authentication=firebase.Authentication(_FIREBASE_SECRET, 'otree'))

    def run(self):
    	for tick in range(seconds):
	    	self.firebase.post('/events', {'tick': self.seconds})
    		self.seconds -= 1
    		time.sleep(1)