from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message("Hello body! < - _ - >")

         return []


class ActionChonDoAn(Action):

    def name(self) -> Text:
        return "action_chon_do_an"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        image_only_message = {"image": "https://i.imgur.com/nGF1K8f.jpg"}

        dispatcher.utter_attachment(image_only_message)

        return []