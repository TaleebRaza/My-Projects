import json, os


class DataLoader:
    def __init__(self):
        self.file_path = "user_data.json"
        self.username = ""
        self.data = {self.username: {"password": "",
                                "graphDetails": {
                                    "id": "",
                                    "name": "",
                                    "unit": "",
                                    "type": "",
                                    "color": ""
                                }}}

    def load_data(self):
        if os.path.exists(self.file_path):
            with open(file=self.file_path, mode="r") as file:
                return json.load(file)
        else:
            return {}

    def save_data(self):
        try:
            user_data = self.load_data()
        except json.decoder.JSONDecodeError:
            user_data = {}

        user_data[self.username] = {
            "password": self.data[self.username]["password"],
            "graphDetails": self.data[self.username]["graphDetails"]
        }

        with open(file=self.file_path, mode="w") as file:
            json.dump(user_data, file, indent=4)

    def load_user_data(self, username):
        data = self.load_data()
        if username in data: return data[username]
        else: return None
