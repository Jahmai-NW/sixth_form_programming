thisdict = {
    "name": "Jahmai",
    "age": 17,
    "school": "CFBS"
}

# print(thisdict["name"] + " is " + str(thisdict["age"]) + " years old, and goes to " + thisdict["school"])

nameHolder = thisdict.get("name")
print(nameHolder)

print(len(thisdict))

