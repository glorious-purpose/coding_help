from random import choice

pws = []
with open("test/passwords.txt", "r", encoding="utf8") as file:
    for line in file.readlines():
        pws.extend(line.split(" "))
print(choice(pws))
