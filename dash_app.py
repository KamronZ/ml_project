import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go

import pandas as pd

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
                            y=[76,65,59,62],
                            name="real world w/ grid search",
                            marker_color= 'rgb(204, 81, 39)'
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

data_symmetry = go.Figure(data=[go.Bar(
    x=x, y=y,
    text=y,
    textposition='auto',
    marker_color= 'rgb(39, 110, 102)'
)])
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
        html.H1("Data Symmetry", style={'textAlign': 'center', 'margin-left' : '80px'}),

        html.Div("Important to notice that the data of the records is not symmetrical."
                 "  This plays an important role in deciding how to score or classification model"
                 " and demonstrates that an accuracy score will not be a particularly good indicator for how"
                 " well the model is performing.  In these cases, a precision score is also important.",
                 style={'margin-left' : '80px', 'margin-right' : '80px', 'font-size' : '20px'}),
        dcc.Graph(figure=data_symmetry),
        html.H1("Model Comparison",style={'textAlign': 'center', 'margin-left' : '80px'}),
        dcc.Graph(figure=model_performance)


    ])

    if __name__ == '__main__':
        app.run_server(debug=True)
    return app.layout
