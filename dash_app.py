import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
import pandas as pd
import numpy as np

diabetes_untouched = pd.read_csv("data/diabetes.csv")
df = diabetes_untouched

positive = sum(diabetes_untouched["Outcome"] == 1)
negative = sum(diabetes_untouched["Outcome"] == 0)

x = ["Non-diabetic", "Diabetic"]
y = [negative, positive]

#models = ["real world w/ grid search", "Logistic Regression", "Naive Bayes"]
scoring_metrics = ["accuracy", 'precision','recall','f1']

model_performance = go.Figure()

model_performance.add_trace(go.Bar(x=scoring_metrics,
                            y=[79,76,61,68],
                            name="RFC Tuned With Grid Search",
                            marker_color= 'rgb(100, 99, 69)'
                            ))
model_performance.add_trace(go.Bar(x=scoring_metrics,
                            y=[76,65,59,62],
                            name="Real World RFC Tuned With Grid Search",
                            marker_color= 'rgb(204, 81, 39)'
                            ))
model_performance.add_trace(go.Bar(x=scoring_metrics,
                            y=[81,79,65,71],
                            name="RFC using identified important features",
                            marker_color= 'rgb(302, 105, 100)'
                            ))
model_performance.add_trace(go.Bar(x=scoring_metrics,
                            y=[75,64,53,58],
                            name="Logistic Regression",
                            marker_color= 'rgb(205, 29, 140)'
                            ))
model_performance.add_trace(go.Bar(x=scoring_metrics,
                            y=[77,67,59,62],
                            name="Naive Bayes",
                            marker_color= 'rgb(39, 180, 102)'
                            ))
model_performance.add_trace(go.Bar(x=scoring_metrics,
                            y=[73,58,61,60],
                            name="Real World Naive Bayes",
                            marker_color= 'rgb(75, 255, 75)'
                            ))
records_table = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='lightgray',
                align='left'),
    cells=dict(values=[df.Pregnancies,df.Glucose,df.BloodPressure,df.SkinThickness,df.Insulin,df.BMI,
               df.DiabetesPedigreeFunction,df.Age, df.Outcome],
               fill_color='lightskyblue',
               align='left'))
])


model_performance.update_layout(
    #title='Model Comparison',
    xaxis_tickfont_size=14,
    yaxis=dict(
        title='Score (percentages)',
        titlefont_size=18,
        tickfont_size=14,

    ),
    barmode='group',
    bargap=0.15,
    bargroupgap=0.1
)
diabetic = [""]
data_symmetry = go.Figure()
data_symmetry.add_trace(go.Bar(x=diabetic,
                            y=[negative],
                            name= "Not Diabetic",
                            marker_color= 'rgb(57, 153, 69)'
                            ))
data_symmetry.add_trace(go.Bar(x=diabetic,
                            y=[positive],
                            name= "Diabetic",
                            marker_color= 'rgb(246, 238, 91)'
                            ))
data_symmetry.update_layout(
    xaxis_tickfont_size=14,
    yaxis=dict(
        title="Number of Records",
        titlefont_size=18,
        tickfont_size=14,
    ),
    barmode='group',
    bargap=0.15,
    bargroupgap=0.1
)












def launch():
    app = dash.Dash()

    app.layout = html.Div([
        # html.Button('Return Home',id = "return_home",onclick="window.location.href='/';"),
        html.H1("Data Pre-Imputation", style={'textAlign': 'center', 'margin-left': '80px'}),
        html.Div("",
                 style={'margin-left': '80px', 'margin-right': '80px', 'font-size': '20px'}),
        dcc.Graph(figure=records_table),
        html.H1("Data Symmetry", style={'textAlign': 'center', 'margin-left' : '80px'}),

        html.Div("Important to notice that the data of the records is not symmetrical."
                 "  This plays an important role in deciding how to score or classification model"
                 " and demonstrates that an accuracy score will not be a particularly good indicator for how"
                 " well the model is performing.  In these cases, a precision score is also important.",
                 style={'margin-left' : '80px', 'margin-right' : '80px', 'font-size' : '20px'}),
        dcc.Graph(figure=data_symmetry),
        html.H1("Model Comparison",style={'textAlign': 'center', 'margin-left' : '80px'}),
        dcc.Graph(figure=model_performance),
        html.Div("Best performers were Random Forest Classifier (RFC) and Naive Bayes (Guassian)."
                 " We can see that the best performer is RFC which uses only the identified important features, however"
                 " this was not the chosen winning model.  This model required the following features: number of pregnancies,"
                 " triceps skin-fold thickness, insulin levels, BMI, and diabetes pedigree function. "
                 " We do not feel these qualify as readily available biometrics for the average user and therefore concluded"
                 " this model to be unsable at this time.   Secondly, we can see Naive Bayes as a strong contender, however"
                 " it suffered a drastic decrease in prediction quality after reducing the available biometrics.  In the end,"
                 " the tuned RFC (via grid search) performed the best after working with reduced biometrics. ",
                 style={'margin-left': '80px', 'margin-right': '80px', 'font-size': '20px'}
                 )


    ])

    if __name__ == '__main__':
        app.run_server(debug=True)
    return app.layout
