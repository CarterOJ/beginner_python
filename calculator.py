import re

def binary_operation(op_one, op_two, operator):
    if operator == "+":
        return op_one + op_two
    elif operator == "-":
        return op_one - op_two
    elif operator == "*":
        return op_one * op_two
    else:
        return op_one / op_two

def main():
    print("To use the calculator, please adhere to the following format: [int] '+'||'-'||'*'||'/' [int].")
    while True:
        user_in = input("Enter an expression or type 'Q' to quit:\n")
        if user_in.lower().strip() == "q":
            print("Exiting calculator")
            break
        params: list[str] = re.findall(r'(?:^|(?<=[+\-*/]))-?\w+(?:\.\w+)?|[+\-*/]', user_in.replace(" ", ""))
        if len(params) != 3:
            print("There must be exactly three arguments!")
        elif not params[0].lstrip('-').isdigit():
            print(f"{params[0]} is not an integer!")
        elif not params[2].lstrip('-').isdigit():
            print(f"{params[2]} is not an integer!")
        elif params[1] not in "+-*/":
            print(f"{params[1]} is not a valid operator!")
        elif int(params[2]) == 0 and params[1] == "/":
            print("Undefined")
        else:
            result = binary_operation(int(params[0]), int(params[2]), params[1])
            print(f"Result: {int(result) if result.is_integer() else result}")

if __name__ == "__main__":
    main()