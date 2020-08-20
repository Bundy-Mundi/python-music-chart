from flask import Flask, jsonify
from extractor import Extractor
import json
app = Flask(__name__)

@app.route('/')
def home():
    response = {}
    response["MESSAGE"] = f"Welcome to our awesome platform!!"
    return jsonify(response)

# Melon
@app.route('/melon')
def melon():
    e = Extractor()
    chart = e.Chart
    return chart.melon_chart()

@app.route('/bugs')
def bugs():
    e = Extractor()
    chart = e.Chart
    return chart.bugs_chart()

@app.route('/billboard')
def billboard():
    e = Extractor()
    chart = e.Chart
    return chart.billboard_chart()

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)