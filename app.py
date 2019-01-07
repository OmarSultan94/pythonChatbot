from rasa_core.channels.socketio import SocketIOInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RegexInterpreter
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig

# load your trained agent
interpreter = RasaNLUInterpreter('./models/nlu/default/chat')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('./models/dialogue', interpreter=interpreter, action_endpoint=action_endpoint)

input_channel = SocketIOInput(
        # event name for messages sent from the user
        user_message_evt="user_uttered",
        # event name for messages sent from the bot
        bot_message_evt="bot_uttered",
        # socket.io namespace to use for the messages
        namespace=None
)

from time import sleep
def run_agent():
        # set serve_forever=True if you want to keep the server running
        s = agent.handle_channels([input_channel], 5004, serve_forever=True)
#        sleep(5)
#        print("hey")
        return 1

from flask import Flask, render_template, request
from flask_socketio import SocketIO, send

app = Flask(__name__)

app.config['SECRET_KEY'] = "theSecret"
socketio = SocketIO(app)

@app.route("/")
def home():
    return render_template("index.html")

#app.run('0.0.0.0',5000,False,)
import _thread
try:
        _thread.start_new_thread( app.run, (True) )
        _thread.start_new_thread( run_agent)
except:
   print ("Error: unable to start thread")