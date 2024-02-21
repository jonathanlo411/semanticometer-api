# Imports
import os
from flask import Flask, request, render_template

# Setup
app = Flask(__name__)

# Page Render
@app.route('/', methods=['GET'])
def page():
    return render_template('index.html')

