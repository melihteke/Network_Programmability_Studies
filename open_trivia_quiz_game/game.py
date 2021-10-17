import json
import requests
import pprint

intro = input("Please enter 'y' for starting a quiz: ")

#if intro == "y":
response = requests.get("https://opentdb.com/api.php?amount=1&category=19&difficulty=easy&type=multiple")
json2dict = json.loads(response.text)
pprint.pprint(json2dict)
#print(type(json2dict))
#print(json2dict['results'][0]['question'])

your_answer = input(json2dict['results'][0]['question'])

if your_answer == json2dict['results'][0]['correct_answer']:
    print("your answer is correct")
else:
    print("your answer is not correct. The correct answer is" , format(json2dict['results'][0]['correct_answer']))
