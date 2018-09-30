from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Well hello there'

@app.route('/api/pixel')
def singlePixel():
    return 'pixel stuff!'

@app.route('/api/pixels')
def allPixels():
    return 'all the pixel stuff!'

@app.errorhandler(404)
def page_not_found(error):
    return 'whoops', 404