# Chatbot Using Rasa

#### A web implementation of rasa chatbot using rasa_nlu and rasa_core.

## Local Setup:
 1. Ensure that rasa_nlu, rasa_core and requirements.txt are installed (run `pip install -r requirements.txt`).
 2. Run the pre-trained chatbot server `python chatbotServer.py`.
 3. Run the demo UI `python demo.py`.
 4. Demo will be live at [http://localhost:5000/](http://localhost:5000/).

## Useful resources:
1. I've borrowed th chat UI from from [chatterbot demo] (https://github.com/chamkank/flask-chatterbot), then made some modifications on handling messages.
2. I've also built most of the chatbot logic and training based on this [tutorial](https://github.com/JustinaPetr/Weatherbot_Tutorial)
3. training dataset

## The chatbot approach:
Rasa based chatbots have some advantages. Unlike geneartive models, the dialog structure can be designed by the developer and yet it's not hard coded.

Two major components are in the chatbot learning process: Understanding of user input and the decisions regarding these intents.

In the understand component, we define the intents that we assume the user may have and deal with the input as a classification problem, to get the right intent from each sentence.  We also define some entities to recognise to help us know what's he asking or expressing about specifically.

In the response component comes a feature that I like in rasa_core module.  we define actions that are either a direct response or some scripts we need to run *like calling third party or quering database".  The sequence of actions in response the sequence of user inputs, is called a story.  Stories describing the dialogflow can be hardcoded or generated with rasa online training module.

After training the chatbot on the to main components, it's ready to be used and it's a good strategy to collect user data and use them to retrain the model.

Note: There was an option to use chatterbot with some training on dialog dataset. It works, but I found the results unreliable and un realistic to use only the sequence to sequence machine learning models to fully generate responses and direct the flow of the dialog. 

## About this chatbot:


## License
This source is free to use, with no conditions