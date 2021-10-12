from flask import Flask, request, render_template, request
import numpy as np
import pickle



app = Flask(__name__)

def ValuePredictor(prediction_list):
    to_predict = np.array(prediction_list).reshape(1,5)
    model = pickle.load(open('models/winning_model', 'rb'))
    result = model.predict(to_predict)
    return result[0]
def ProbabilityPredictor(prediction_list):
    to_predict = np.array(prediction_list).reshape(1, 5)
    model = pickle.load(open('models/winning_model', 'rb'))
    result = model.predict_proba(to_predict)
    return result[0]


@app.route("/predict", methods =['POST'])
def predict():
    if request.method == 'POST':

        to_predict = request.form.to_dict() # pull information from forms as dict entries
        to_predict = list(to_predict.values()) # put values as list
        to_predict = list(map(float, to_predict))
        result = ValuePredictor(to_predict)

        prediction = int(result)
        probability = ProbabilityPredictor(to_predict)

        return render_template("predict.html", prediction=prediction, probability=probability)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods =['GET', 'POST'])
def login():
    if request.method == 'POST':

        return "you are using POST"
    else:
        return "you are using get"
# @app.route("/profile/<name>")



@app.route("/diabetes_notebook")
def diabetes_notebook():
    return render_template("diabetes_notebook.html")

# def profile(name):
#     return render_template("profile.html", name =name)

# @app.route("/shopping")
# def shopping():
#     food = ["Cheese", "Tuna", "Beef"]
#     return render_template("shopping.html", food=food)

# @app.route("/profile/<name>")
# # routing/mapping
# #This will map a url to a return value of function
# @app.route('/')
# @app.route("/<user>")
# def index(user = None):
#     return render_template("user.html", user=user)

if __name__ == "__main__":
    app.run(debug =True)