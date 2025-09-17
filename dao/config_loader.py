import json
import os

class ConfigLoader:

    def __init__(self, config_path="../dao/config.json"):
        print(os.getcwd())
        self.config_path = config_path
        if (os.path.exists(self.config_path) == False):
            raise FileNotFoundError(f"Error! Config file not found: {self.config_path}")
        with open(config_path, "r") as f:
            self.config = json.load(f)

    def get_config(self):
        return self.config
