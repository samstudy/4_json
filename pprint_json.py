import json
import os

def load_json_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def pprety_print(data):
	print(json.dumps(data, indent=4))


if __name__ == '__main__':
    data = load_json_data('Input the path where store json file')
    print (pprety_print(data))
   
