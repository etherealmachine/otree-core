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
import time


logger = logging.getLogger(__name__)

_FIREBASE_URL = 'https://otree.firebaseio.com'
_FIREBASE_SECRET = 'uXop5iUjKkGfH20sFmdCMenX7QnUWmnWDde76WQR'


_emitters = {}


def start_emitter(waitPage, period_length, num_subperiods):
    path = '/session/%s/app/%s/subsession/%s/round/%s/group/%s/page/%s/subperiods' % (
        waitPage.session.code,
        waitPage.subsession.app_name,
        waitPage.subsession.id,
        waitPage.round_number,
        waitPage.group.id_in_subsession,
        'tmp')
    if path not in _emitters:
        _emitters[path] = Emitter(path, period_length, num_subperiods)
        _emitters[path].start()


class Emitter(threading.Thread):

    def __init__(self, path, period_length, num_subperiods):
        super(Emitter, self).__init__()
        self.path = path
        self.period_length = period_length
        self.num_subperiods = num_subperiods
        self.subperiod_length = period_length / num_subperiods
        self.firebase = firebase.FirebaseApplication(_FIREBASE_URL)

    def run(self):
        self.subperiod = 0
        while self.subperiod < self.num_subperiods:
            time.sleep(self.subperiod_length)
            self.subperiod += 1
            event = {
                'id': self.subperiod,
                'decisions': [] # TODO: Aggregated decision vectors.
            }
            self.firebase.put(self.path, self.subperiod, event)
        return
