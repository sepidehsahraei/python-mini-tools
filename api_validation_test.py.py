import os
os.system("cls")
import requests
try:
    response= requests.get('https://randomuser.me/api/?results=5')
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    data = response.json()
    for user in data["results"]:
        first_name = user["name"]["first"]
        email= user["email"]
        assert first_name, "First name is missing for a user."
        assert "@" in email, f"Invalid email format for a user: {email}"
        print(f"Name: {first_name}\nEmail: {email}")
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
print("\nAll tests passed successfully.\n")
