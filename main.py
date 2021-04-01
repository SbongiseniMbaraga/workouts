import requests

APPLICATION_ID = "794c5190"
APPLICATION_KEY = "1f8f2020094011c7a80069b8cb34f2a2"

GENDER = "male"
WEIGHT_KG = 82
HEIGHT_CM = 163
AGE = 24

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

user_exercise = input("Tell me which exercise did you do?")

headers = {
    "x-app-id": APPLICATION_ID,
    "x-app-key": APPLICATION_KEY
}

parameters = {
    "query": user_exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=nutritionix_endpoint, json=parameters, headers=headers)
results = response.json()
print(results)