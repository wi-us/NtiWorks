import json

array = []
jokes = []

def read_and_serialize(start):
    start = text.find('***', start) + 3
    end = text.find('***', start)
    
    serialized_text = text[start:end]
    array.append(serialized_text)
    return end

file_path = 'NtiWorks//Task5//serializeText//anekdots.txt'
with open(file_path, 'r+', encoding="UTF-8") as file:
    text = file.read()
    val = 0
    while val != -1:
        val = read_and_serialize(val)


with open('NtiWorks//Task5//serializeText//anekdots.json', 'w+', encoding="UTF-8") as file:
    file.write(json.dumps(array, ensure_ascii=False))


with open('NtiWorks//Task5//serializeText//anekdots.json', 'r', encoding="UTF-8") as file:
    jokes = json.loads(file.read())

    print(len(jokes))