import socket

from flask import Flask, request, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import AppConfig

app = Flask(__name__)
app.config.from_object(AppConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# required for migrations (since this is a test project we do not bother with proper locations of objects)
from models import User


@app.route("/")
def hello_world():
    hostname = socket.gethostname()

    return """
    <!DOCTYPE html>
    <head>
        <title>Kubernetes Workshop Test App</title>
        <style>
            body {{
                background-color: #2D2D2D;
            }}       
    
            h1 {{
                color: #C26356;
                font-size: 30px;
                font-family: Menlo, Monaco, fixed-width;
            }}
    
            p {{
                color: white;
                font-family: "Source Code Pro", Menlo, Monaco, fixed-width;
            }}       
        </style>
    </head>
    <body>
        <h1>Hello World!</h1>
        <p>Can you make this run in a container?</p>
        <p>What about in Kubernetes?</p>
        <p>My hostname is: {0}</p>
    </body>
    </html>
""".format(hostname)


@app.route('/users', methods=["GET", "POST"])
def record_my_user_to_db():
    message = ''
    if request.method == "POST":
        # getting input with name = fname in HTML form
        user_name = request.form.get("username")
        message = f"Your username {user_name} was recorded to database."
    return render_template("form.html", message=message)
