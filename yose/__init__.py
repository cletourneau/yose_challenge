from flask import Flask
from yose.jade_support import add_jade_support

APP = Flask(__name__)

add_jade_support(APP)

import endpoints.ping_challenge
import endpoints.share_challenge
import endpoints.power_of_two_challenge
import endpoints.prime_factors_ui