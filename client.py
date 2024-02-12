import requests

login_data = {"username": "kuba2", "password": "12345"}
token = requests.post("http://127.0.0.1:8000/login", login_data).json()["token"]
headers = {"Authorization": f"Token {token}"}
animals = requests.get("http://127.0.0.1:8000/animals", headers=headers)
print(animals.json())
animal = {"id": 2, "name": "asd", "kind": "l", "additionalInfo": "asdas", "cage": 1}
requests.post("http://127.0.0.1:8000/animals", data=animal, headers=headers)
animals = requests.get("http://127.0.0.1:8000/animals", headers=headers)
print(animals.json())
