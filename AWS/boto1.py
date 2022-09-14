import json
from io import StringIO
in_json = StringIO("""[{
    "key01": "value01",
    "key02": "value02",

    "keyN": "valueN"
},
{
    "key01": "value01",
    "key02": "value02",

    "keyN": "valueN"
},
{
    "key01": "value01",
    "key02": "value02",

    "keyN": "valueN"
}
]""")
print(in_json)
result = [json.dumps(record) for record in json.load(in_json)]  # the only significant line to convert the JSON to the desired format

print('\n'.join(result))