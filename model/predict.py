import requests

res = requests.post('http://localhost:12345/predict', json={"Age": 85, "Sex": "male", "Embarked": "S"})
if res.ok:
    print(res.json())