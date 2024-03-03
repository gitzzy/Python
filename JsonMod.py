import json

Data = {
    "Name": "Devansh",
    "Age": 21,
    "Alive": True,
    "edu":["BCA","12th","10th"]
}

json_data = json.dumps(Data,indent=4)
print(json_data)

import math

print(math.sin(90))