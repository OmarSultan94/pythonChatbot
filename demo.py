from flask import Flask, render_template, request
from flask_socketio import SocketIO, send

app = Flask(__name__)

app.config['SECRET_KEY'] = "theSecret"
socketio = SocketIO(app)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    #app.run()
    socketio.run(app)