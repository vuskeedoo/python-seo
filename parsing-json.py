import json

dicti = json.load(open('spiderman.json'))

print(dicti["29771621"]["related"][1])

print("\n\n\n\n")

print(dicti[next(iter(dicti))]["related"][0])
