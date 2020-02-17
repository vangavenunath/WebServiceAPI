from datetime import timedelta

from flask import Flask
import flask
from flask_restful import Api
from resources.routes import initialize_routes

app = Flask(__name__)
api = Api(app)

initialize_routes(api)

from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    print("Get Password is called")
    if username == 'dara':
        return 'dara'
    return None

@auth.error_handler
def unauthorized():
    return flask.Response({'error': 'Unauthorized access'}), 401

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

@app.route('/api/v1/test_auth', methods=['GET'])
@auth.login_required
def auth_task():
    print("Auth Method is called")
    return flask.Response("Success")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
