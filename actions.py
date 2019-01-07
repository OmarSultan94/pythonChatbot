from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionOrderPizza(Action):
    def name(self):
        return 'action_order_pizza'
    def run(self, dispatcher, tracker, domain):
        print('Ordering Pizza is completed! It should be with you soon :)')
        return [SlotSet("size", [])]