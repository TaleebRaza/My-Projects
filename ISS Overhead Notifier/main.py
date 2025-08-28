# Importing Modules
import requests
from datetime import datetime
import smtplib

# ************************** Constants ************************** #
MY_LATITUDE = 33.771542
MY_LONGITUDE = 72.751091
MY_EMAIL = "randommail@gmail.com"
MY_PASSWORD = "abc123()"

def is_iss_overhead():
    # Get data from ISS API
    iss_location_data = requests.get(url="http://api.open-notify.org/iss-now.json").json()

    iss_longitude = float(iss_location_data["iss_position"]["longitude"])
    iss_latitude = float(iss_location_data["iss_position"]["latitude"])

    if MY_LATITUDE-5 <= iss_latitude <= MY_LATITUDE+5 and MY_LONGITUDE-5 <= iss_longitude <= MY_LONGITUDE+5:
        return True
    return None

def is_night():
    # Get current time
    current_hour = datetime.now().hour

    # Get sunset/sunrise time
    parameters ={
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0,
        "tzid": "Asia/Karachi"
    }
    suntime_data = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters).json()

    sunrise_time = int(suntime_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_time = int(suntime_data["results"]["sunset"].split("T")[1].split(":")[0])

    if sunrise_time >= current_hour >= sunset_time:
        return True
    return None

emails_sent = 0
while emails_sent <= 10:
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look Up👆\n\nThe 🛰 is above you. Go out and find it"
            )
        emails_sent += 1