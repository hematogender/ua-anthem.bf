import brainfuck

interpreter = brainfuck.NiceInterpreter()

with open("anthem.bf", "r") as file:
    interpreter.execute(file.read())
