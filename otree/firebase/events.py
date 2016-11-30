"""
Sends subpage events to Firebase.

Want to start an emitter when the first subject connects to a page.
Then let the experiment configure events that get emitted until the
timeout runs out (timeout_seconds in the Page view object).

Problems:
Subjects will start pages at different times - we want 1 emitter per
set of subjects on the same page.
Subjects might be on different pages - need 1 emitter per page type.
"""
from firebase import firebase
import logging
import threading


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
        '''
        for tick in range(seconds):
            self.firebase.post('/events', {'tick': self.seconds})
            self.seconds -= 1
            time.sleep(1)
        '''
        return
