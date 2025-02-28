d = {}# empty dictionary
marks = {
    "Jimin":100,
    "Srishti":76,
    "khushi":40,

}

print(marks.items()) #method

marks = {
    "Jimin":100,
    "Srishti":76,
    "khushi":40

}
print(marks.keys()) # method

marks = {
    "Jimin":100,
    "Srishti":76,
    "khushi":40

}
print(marks.values()) # method

marks = {
    "Jimin":100,
    "Srishti":76,
    "khushi":40

}

marks.update({"Jimin":99, "Nisha":100}) # method
print(marks)


marks = {
    "Jimin":100,
    "Srishti":76,
    "khushi":40

}
print(marks.get("Shivika")) # prints none
print(marks["Jimin2"]) # returns an error

marks = {
    "Jimin":100,
    "Srishti":76,
    "khushi":40

}
print(marks.pop("khushi")) # method
print(marks)