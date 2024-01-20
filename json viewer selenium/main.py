from json_editor_file import JsonEditor
import requests

URL = "https://opentdb.com/api.php"

query = {
    "amount": 20
}
response = requests.get(url=URL, params=query)
data = response.json()
# print(data)
obj = JsonEditor(data)
