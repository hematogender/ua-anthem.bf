with open("anthem.txt", "r") as file:
    anthem = file.read()

sourcecode = ""

for symbol in anthem:
    sourcecode += "+" * ord(symbol) + ".>"

    # for readability 😜
    if symbol == " ":
        sourcecode += "\n"
    elif symbol == "\n":
        sourcecode += "\n\n"

with open("anthem.bf", "w") as file:
    file.write(sourcecode)
