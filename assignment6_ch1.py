import json

file = open('F:\\pythone\\DS291022B\\Assignment6.py\\jsone_file.json')
data = json.load(file)

for i in data:
    print(i)

file.close( )