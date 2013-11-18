from flask import render_template
from yose import APP as app

@app.route('/primeFactors/ui', methods=['GET'])
def display_form():
    return render_template('primeFactorsForm.jade')
