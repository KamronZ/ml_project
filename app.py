import flask
from flask import Flask, request, render_template, request
import numpy as np
import pickle
import dash
from dash import html

import dash_app

server = Flask(__name__)
app = dash.Dash(__name__, server=server, url_base_pathname='/dash_app/')
app.layout = dash_app.launch()


def ValuePredictor(prediction_list):
    to_predict = np.array(prediction_list).reshape(1, 5)
    model = pickle.load(open('models/winning_model', 'rb'))
    result = model.predict(to_predict)
    return result[0]


def ProbabilityPredictor(prediction_list):
    to_predict = np.array(prediction_list).reshape(1, 5)
    model = pickle.load(open('models/winning_model', 'rb'))
    result = model.predict_proba(to_predict)
    return result[0]




@server.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        to_predict = request.form.to_dict()  # pull information from forms as dict entries
        to_predict = list(to_predict.values())  # put values as list
        to_predict = list(map(float, to_predict))
        result = ValuePredictor(to_predict)

        prediction = int(result)
        probability = ProbabilityPredictor(to_predict)

        return render_template("predict.html", prediction=prediction, probability=probability)


@server.route("/")
def index():
    return render_template("index.html")


@server.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        return "you are using POST"
    else:
        return "you are using get"





@server.route("/diabetes_notebook")
def diabetes_notebook():
    return render_template("diabetes_notebook.html")


@server.route("/data_visualization")
def dash_chart():
    return flask.redirect('/dash_app')


if __name__ == "__main__":
    server.run(debug=True)
