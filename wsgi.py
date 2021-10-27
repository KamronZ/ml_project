from werkzeug.middleware.dispatcher import DispatcherMiddleware

from dash_app import dash_app as dash_app
from flask_app import flask_app


application = DispatcherMiddleware(flask_app, {
    '/dash_app': dash_app.server})