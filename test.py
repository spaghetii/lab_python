import ndjson
import requests
import json

"""
you should have some ndjson file and change
1. file_info => filename     # input filename
2. append_name               # add string to rename 
3. output_filename           # output filename
"""

file_info = {
    "file_dir"        : "./",
    "file_name"       :"20200114skb",
    "file_extension"  : ".ndjson"
}

output_info = {
    "file_dir"        : "./",
    "file_name"       :"git_output",
    "file_extension"  : ".json"
}

append_name = 'dpv-skb-'
output_filename = 'dpv-skb.ndjson'

# get ndjson 
NDJSON_FILE_Path = f"{file_info['file_dir']}{file_info['file_name']}{file_info['file_extension']}"
file_content = open(NDJSON_FILE_Path, "r", encoding="utf-8").readlines()
json_list = [json.loads(line) for line in file_content]

# output json
JSON_FILE_Path = f"{output_info['file_dir']}{output_info['file_name']}{output_info['file_extension']}"
with open(JSON_FILE_Path, "w+", encoding="utf-8") as json_file:
    json.dump(json_list, json_file)

print("converting ndjson file to json file done!!.")

# revise json
input_file = open ('git_output.json', encoding="utf-8")
json_array = json.load(input_file)
for index,item in enumerate(json_array):
    """print(index)
    print(json_array[index]['attributes']['title'])"""
    if json_array[index]['type'] == 'visualization':
        json_array[index]['attributes']['title'] = append_name+json_array[index]['attributes']['title']
        temp = json.loads(json_array[index]['attributes']['visState'])
        temp['title'] = append_name+temp['title']
        """print(temp['title'])"""
        json_array[index]['attributes']['visState'] = json.dumps(temp)
        "print(json_array[index]['attributes']['visState'])"

# output ndjson    
text = ndjson.dumps(json_array)
data = ndjson.loads(text)
with open(output_filename, 'w') as f:
    ndjson.dump(data, f)