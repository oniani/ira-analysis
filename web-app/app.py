#!/usr/bin/env python3
import pyjokes
from flask import Flask, request, render_template
from predict import predict

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("ira.html")

    # POST
    text = request.form.get("textarea")
    conclusion = predict(text)
    return render_template("ira.html", conclusion=conclusion)
