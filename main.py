import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 82
HEIGHT_CM = 160
AGE = 25

APP_ID = os.environ["794c5190"]
API_KEY = os.environ["1f8f2020094011c7a80069b8cb34f2a2"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["https://api.sheety.co/0e301b17f69ae725c48c9d15742f3f0e/workouts/workouts"]

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    #No Auth
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    #Basic Auth
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(
            os.environ["sbo"],
            os.environ["Englishdub1"],
        )
    )

    # #Bearer Token
    # bearer_headers = {
    # "Authorization": f"Bearer {os.environ['TOKEN']}"
    # }
    # sheet_response = requests.post(
    #     sheet_endpoint,
    #     json=sheet_inputs,
    #     headers=bearer_headers
    # )

    print(sheet_response.text)