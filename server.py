# Imports
import os
from flask import Flask, request, render_template
from modelCollection import ModelCollection
from json import load

# Setup
SECRETS = load(open('config.json', 'r'))
MODELS = ['vs', 'tbp', 'tbo', 'pr']
MODEL_COLLECTION = ModelCollection(
    gcp_api_key=SECRETS['PerspectiveAPIKey'],
    rate_limit_timeout=1 # 1 is default
)
app = Flask(__name__)

# Page Render
@app.route('/', methods=['GET'])
def page():
    return render_template('index.html')

# --- API ---

@app.route('/api/single', methods=['POST'])
def api_single():
    # Validate Request
    args = request.args
    body = request.json
    if ('model' not in args) or (args.get('model') not in MODELS):
        return { "message": "Invalid Model"}, 400
    if ('sentence' not in body) or (not isinstance(body['sentence'], str)):
        return { "message": "Invalid Body"}, 400

    # Query Model
    requested_model = args.get('model')
    sentence = body['sentence']
    if requested_model == 'vs':
        res = MODEL_COLLECTION.queryVaderSentiment(sentence)
    elif requested_model == 'tbp':
        res = MODEL_COLLECTION.queryTextBlobPolairty(sentence)
    elif requested_model == 'tbo':
        res = MODEL_COLLECTION.queryTextBlobObjectivity(sentence)
    elif requested_model == 'pr':
        res = MODEL_COLLECTION.queryPerspective(sentence)
    else:
        return { "message": "Something went wrong!"}, 400

    return { "results": res }, 200

@app.route('/api/bulk', methods=['POST'])
def api_bulk():
    # Validate Request
    body = request.json
    if ('sentences' not in body) or (not isinstance(body['sentences'], list)):
        return { "message": "Invalid Body"}, 400

    # Query Model
    sentences = body['sentences']
    res = MODEL_COLLECTION.queryAllModelsBulk(sentences)

    return { "results": res }, 200

