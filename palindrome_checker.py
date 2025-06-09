def check_palindrome(pal: str):
    if len(pal) <= 1:
        return True
    elif pal[0].lower() == pal[-1].lower():
        return check_palindrome(pal[1:-1])
    return False

def main():
    while True:
        palindrome = input("Enter any string to check if it's a palindrome. Type 'Q' to exit: ")
        if palindrome.strip().lower() == "q":
            print("Exiting palindrome checker")
            break
        print(check_palindrome(palindrome))

if __name__ == "__main__":
    main()