import json
import re

class ScoringEngine:
    """A class made to process the data received from the AW API
       and calculate the score of an activity depending on the multiplier
       in config.json """

    def __init__(self, config_path='config.json'):
        self.categories = {}

        with open(config_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        #We fetch every rule in the config.json and assign it to a class variable
        for item in data["categories"]:
            name = item["name"]
            self.categories[name] = {
                "regex": item.get("regex", ""),
                "multiplier": item.get("multiplier", 1),
                "parent": item.get("parent", None)
            }

    #####The scoring logic#####
    # Here, we go through every event passed to the method
    # to get it's category and then give it a score depending 
    # on it's multiplier and the duration of that event


    def score(self, input_text: str, base_value: float) -> float:
        for cat, data in self.categories.items():
            pattern = data["regex"]
            if pattern and re.search(pattern, input_text, re.IGNORECASE):
                return base_value * data["multiplier"]

        uncategorized = self.categories.get("uncategorized")
        return base_value * (uncategorized["multiplier"] if uncategorized else 1)
