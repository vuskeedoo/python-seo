import json

data = json.loads(open('spiderman.json').read())

#print(dicti["29771621"]["related"][1])

#print("\n\n\n\n")

#print(dicti[next(iter(dicti))]["related"][0])

#root_response = data[next(iter(data))]

#print(root_response)

print(json.dumps(data, indent=2, sort_keys=False))
