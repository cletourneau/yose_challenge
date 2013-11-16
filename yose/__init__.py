from flask import Flask

APP = Flask(__name__)

import endpoints.ping_challenge
import endpoints.share_challenge
import endpoints.power_of_two_challenge