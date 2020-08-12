from flask import Flask
from extractor import Extractor
import json
app = Flask(__name__)

@app.route('/')
def home():
    return "HELLO WORLD"

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