def is_palindrome(text):
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]


def main():
    print("Palindrome Checker")
    print("==================")
    print("Enter 'quit' to exit\n")

    while True:
        user_input = input("Enter a word or phrase: ").strip()
        if user_input.lower() == 'quit':
            break
        if not user_input:
            continue

        if is_palindrome(user_input):
            print(f'"{user_input}" IS a palindrome\n')
        else:
            print(f'"{user_input}" is NOT a palindrome\n')


if __name__ == "__main__":
    main()
