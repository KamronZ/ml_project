from flask import Flask, request, render_template, request
import numpy as np
import pickle

flask_app = Flask(__name__)


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


@flask_app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        to_predict = request.form.to_dict()  # pull information from forms as dict entries
        to_predict = list(to_predict.values())  # put values as list
        to_predict = list(map(float, to_predict))
        result = ValuePredictor(to_predict)

        prediction = int(result)
        probability = ProbabilityPredictor(to_predict)

        return render_template("predict.html", prediction=prediction, probability=probability)


@flask_app.route("/")
def index():
    return render_template("index.html")


@flask_app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        return "you are using POST"
    else:
        return "you are using get"





@flask_app.route("/diabetes_notebook")
def diabetes_notebook():
    return render_template("diabetes_notebook.html")


@flask_app.route("/data_visualization")
def data_visualization():
    return render_template("data_visualization.html")


if __name__ == "__main__":
    flask_app.run(debug=True)
