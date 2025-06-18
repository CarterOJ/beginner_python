def fizzbuzz(n):
    lines = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            lines.append("FizzBuzz")
        elif i % 3 == 0:
            lines.append("Fizz")
        elif i % 5 == 0:
            lines.append("Buzz")
        else:
            lines.append(f"{i}")
    return "\n".join(lines)

def main():
    while True:
        iters = input("Please enter the iteration amount to fizzbuzz. Type 'Q' to quit: ")
        trimmed = iters.strip()
        if trimmed.lower() == "q":
            print("Exiting fizzbuzz")
            break
        elif " " in trimmed:
            print("Can only accept one argument!")
        elif not trimmed.isdigit():
            print("Input must be a positive integer!")
        else:
            print(fizzbuzz(int(iters)))

if __name__ == "__main__":
    main()