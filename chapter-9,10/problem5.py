words = ["Donkey", "bad", "ganda"]

with open("main.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("main.txt", "w") as f:
    f.write(content)