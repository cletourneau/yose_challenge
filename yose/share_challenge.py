from yose import APP as app

@app.route('/', methods=['GET'])
def share():
    return '<html><a id="repository-link" href="https://github.com/cletourneau/yose_challenge">Source code</a></html>'