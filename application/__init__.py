from flask import Flask,session
from flask_session import Session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret key'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

from application.controllers import dashboardController
from application.controllers import homeController
from application.controllers import testimoniController
from application.controllers import userController