# ➖➖➖➖➖➖➖➖➖➖➖ Importing Modules ➖➖➖➖➖➖➖➖➖➖➖
from http.client import responses
from logging import exception

import requests
from datetime import datetime

class WorkoutTracker:
    APP_ID = "API ID"
    API_KEY = "API KEY"
    ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
    SHEET_ENDPOINT = "https://api.sheety.co/username/projectName/sheetName"

    ENDPOINT_HEADER = {
        "Content-Type": "application/json",
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
        # "Authorization": "Token" optional
    }

    def __init__(self):
        self.data = None

    def get_exercise_data(self, query:dict):
        try:
            response = requests.post(url=self.ENDPOINT, json=query, headers=self.ENDPOINT_HEADER)
            response.raise_for_status()
            self.data = response.json()["exercises"]

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.ConnectionError:
            print("Connection error. Check your network or endpoint.")
        except requests.exceptions.Timeout:
            print("Request timed out.")
        except requests.exceptions.RequestException as e:
            print(f"An unexpected error occurred: {e}")

    def main_loop(self):
        while True:
            query = input("Enter (q to exit): ").lower()
            if query == "q":
                break
            else:
                self.get_exercise_data(query={"query": query})
                self.sheet_update()

    def sheet_update(self):
        for exercise in self.data:
            sheet_data = {
                "workout":{
                    "date": datetime.now().strftime("%a, %B %d, %Y"),
                    "time": datetime.now().strftime("%I %P").upper(),
                    "exercise": exercise["name"],
                    "duration": exercise["duration_min"],
                    "calories": exercise["nf_calories"]
                }
            }

            try:
                response = requests.post(url=self.SHEET_ENDPOINT, json=sheet_data, headers=self.ENDPOINT_HEADER)
            except exception as e:
                print("something went wrong")
            else:
                print(response.text)


tracker = WorkoutTracker()
tracker.main_loop()

