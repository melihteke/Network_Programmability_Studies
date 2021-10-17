import requests
import json
import pprint

#get request is initiated
response = requests.get("https://opentdb.com/api.php?amount=1&category=27&difficulty=easy&type=multiple")


#print(response.status_code)
#print(response.text)
print(type(response.text))

#the response is json string. Now lets convert it to python dict.
response_dict = json.loads(response.text)
pprint.pprint(response_dict)
print(type(response_dict))

#now convert the dictionary back to json string and compare
reconvert_response_dict = json.dumps(response_dict)
pprint.pprint(reconvert_response_dict)
print(type(reconvert_response_dict))

print(response.text == reconvert_response_dict)


