# ➖➖➖➖➖➖➖➖➖➖➖ Importing Modules ➖➖➖➖➖➖➖➖➖➖➖
import requests
from datetime import datetime

# ➖➖➖➖➖➖➖➖➖➖➖ Constants ➖➖➖➖➖➖➖➖➖➖➖
# Step 1 Constants
PIXELA_USER_API_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "randomusername1"
TOKEN = "randomAPIkey"
HEADER = {"X-USER-TOKEN": TOKEN}

USER_PARAMETERS = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Step 2 Constants
GRAPH_ENDPOINT = f"{PIXELA_USER_API_ENDPOINT}/{USERNAME}/graphs"
GRAPH_CONFIG = {
    "id": "testgraphid",
    "name": "Test Graph",
    "unit": "Test Unit",
    "type": "int",
    "color": "ajisai"
}

# Step 3 Constants
UPDATE_GRAPH_ENDPOINT = f"{PIXELA_USER_API_ENDPOINT}/{USERNAME}/graphs/{GRAPH_CONFIG["id"]}"

date = datetime.now().strftime("%Y%m%d")

UPDATE_CONFIG = {
    "date": date, # 2025 - 09 - 01 (September 1st, 2024)
    "quantity": "9" # +(0-9) or +(0.0-9.9)
}
# ➖➖➖➖➖➖➖➖➖➖➖ Post Request To Create User ➖➖➖➖➖➖➖➖➖➖➖
# response = requests.post(url=PIXELA_USER_API_ENDPOINT, json=USER_PARAMETERS)
# print(response.text)

# Use the above two lines to create an account "once"

# ➖➖➖➖➖➖➖➖➖➖➖ Post Request To Create Graph ➖➖➖➖➖➖➖➖➖➖➖
# response = requests.post(url=GRAPH_ENDPOINT, json=GRAPH_CONFIG, headers=HEADER)
# print(response.text)

# these lines are used once to create a graph. (To create another graph, uncomment these lines and change the graph config)

# ➖➖➖➖➖➖➖➖➖➖➖ Post Request To Update Graph ➖➖➖➖➖➖➖➖➖➖➖
response = requests.post(url=UPDATE_GRAPH_ENDPOINT, json=UPDATE_CONFIG, headers=HEADER)
print(response.text)
print(UPDATE_GRAPH_ENDPOINT)