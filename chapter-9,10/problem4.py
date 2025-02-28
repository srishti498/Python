word = "Donkey"

with open("main.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open("main.txt", "w") as f:
    f.write(contentNew)