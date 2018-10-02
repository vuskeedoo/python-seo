import json
from restapi import Search

response = Search()

data = response.keywords_related('superman','US')

data = str(data).replace("'","\"")

data = json.loads(data)

#data = json.loads(open('batman.json').read())

#print(dicti["29771621"]["related"][1])

#print("\n\n\n\n")

#print(dicti[next(iter(dicti))]["related"][0])

#root_response = data[next(iter(data))]

#print(root_response)


#print( data )
#print(type(data))

print(json.dumps(data, indent=2, sort_keys=False))
