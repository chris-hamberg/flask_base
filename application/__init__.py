# do database
from flask import Flask

app = Flask(__name__)

from application.mvc.views import view
app.register_blueprint(view)
