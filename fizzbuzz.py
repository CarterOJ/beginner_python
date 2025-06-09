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
        if iters.strip().lower() == "q":
            print("Exiting fizzbuzz")
            break
        elif " " in iters.strip():
            print("Can only accept one argument!")
        elif not iters.strip().isdigit():
            print("Input must be an integer!")
        else:
            print(fizzbuzz(int(iters)))

if __name__ == "__main__":
    main()