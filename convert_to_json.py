import json
ar = []
with open('mat.txt', 'r', encoding='Utf-8') as file:
    for i in file:
        n = i.lower().split()
        if n:
            ar.extend(n)

with open('mat_json.json', 'w', encoding='Utf-8') as file:
    json.dump(ar, file, ensure_ascii=False)
