from Interpreter import Interpreter

def main():
    interpreter = Interpreter()
    with open("program.expr", mode="r", encoding="utf-8") as f:
        program = f.read()
    result = interpreter.interpret(program)
    print(result)

if __name__ == "__main__":
    main()
