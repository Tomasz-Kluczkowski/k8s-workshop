import socket

from flask import Flask

app = Flask(__name__)


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
