import os
os.system("cls" if os.name == "nt" else "clear")
import requests
try:
    response = requests.get('http://randomuser.me/api/?results=5')

    if response.status_code == 200:
        data = response.json()

        for user in data["results"]:
            first_name = user["name"]["first"]

            print(first_name)

    else:
        print("Request failed")

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)