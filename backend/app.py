from flask import Flask, request
import flask
import json
from flask_cors import CORS
import cohere
import numpy as np
import re
import pandas as pd
from tqdm import tqdm
from datasets import load_dataset
import umap
import altair as alt
from sklearn.metrics.pairwise import cosine_similarity
from annoy import AnnoyIndex
import warnings
warnings.filterwarnings('ignore')
pd.set_option('display.max_colwidth', None)
import random
import math

app = Flask(__name__)
CORS(app)

arr = []

@app.route('/users', methods=["GET", "POST"])
def users():
    print("users endpoint reached")
    if request.method == "GET":
        print("get request")
        with open("users.json", "r") as f:
            data = json.load(f)
            data.append({
                "username": "user4",
                "pets": ["hamster"]
            })
            return flask.jsonify(data)
    if request.method == "POST":
        print("post request")
        received_data = request.get_json()
        print(f"received data: {received_data}")
        message = received_data['data']
        arr.append(message)
        print(arr)
        return_data = {"status": "success", "message": f"received: {message}"}
        return flask.Response(response=json.dumps(return_data), status=201)

if __name__ == "__main__":
    app.run("localhost", 6969)

