import json
import pprint
with open ('input.json') as json_data:
	data = json.load(json_data)

#print (data)
pprint.pprint(data, depth=5)