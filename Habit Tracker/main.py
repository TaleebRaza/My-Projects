# ➖➖➖➖➖➖➖➖➖➖➖ Importing Modules ➖➖➖➖➖➖➖➖➖➖➖
import requests


# ➖➖➖➖➖➖➖➖➖➖➖ Constants ➖➖➖➖➖➖➖➖➖➖➖
PIXELA_USER_API_ENDPOINT = "https://pixe.la/v1/users"

USER_PARAMETERS = {
    "token": "randomAPIkey",
    "username": "randomusername1",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# ➖➖➖➖➖➖➖➖➖➖➖ Post Request To Create User ➖➖➖➖➖➖➖➖➖➖➖
# response = requests.post(url=PIXELA_USER_API_ENDPOINT, json=USER_PARAMETERS)
# print(response.text)

# Use the above two lines to create an account "once"
