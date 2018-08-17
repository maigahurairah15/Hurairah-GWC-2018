import json
from pprint import pprint

# Open a json file and append entries to the file.
f = open("allanswers.json", "r")
data = json.load(f)
print(type(data))
print(data)
f.close()

count = 0
oppcount = 0
count_2 = 0
for d in data:
    if d['color'] == "red":
        count += 1
    elif d['color'] == "blue":
        count_2 += 1
    else:
        oppcount += 1
print("number of red:" + str(count))
print("number of blue:" + str(count_2))
print("number of others:" + str(oppcount))
