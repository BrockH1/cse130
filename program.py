try:
    file = open("name.txt", "w")
    file.write("Brock")
    file.close()
except OSError:
    print("You suck")

    with open("name.txt", "w") as file:
        file.write("Brock")

try:
    file = open("name.txt", "r")
    name = file.readline()
    print("The name is:", name)
    file.close()
except OSError:
    print("You suck")

data = {
    "name":"python",
    "designer":"Something weird",
    "paadigm":["Item1", "Item2", "Item3"],
    "year": 2000
}

import json
# text = json.dumps(data)
# with open("lab02.json", "w") as file:
#     file.write(text)

with open("lab02.json", "r") as file:
    text2 = file.read()
    data2 = json.loads(text2)
    
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in list:
    print(number)

print(list[:3])
print(list[-3:])
print(list[4:7])

tuple_one = 1, 1.1
print("tuple_one =", tuple_one)
print("tuple_one[0] =", tuple_one[0])
print("tuple_one[1] =", tuple_one[1], '\n')