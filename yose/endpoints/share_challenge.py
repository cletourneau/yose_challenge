from flask import render_template
from yose import APP as app

@app.route('/', methods=['GET'])
def share():
    return render_template('share.jade')
