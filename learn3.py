import requests
import json
response = requests.get('https://temp.163.com/special/00804KVA/cm_yaowen.js?callback=data_callback')
yaowen = response.text.replace('data_callback(','')
yaowen = yaowen.replace(')','')
json = json.loads(yaowen)
for index in json:
    print(index.get('title'),index.get('commenturl'))