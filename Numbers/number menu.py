def is_palindrome_string(s):
    s = str(s).lower()
    s = ''.join(s.split())
    return s == s[::-1]

def is_palindrome_number(number):
    return str(number) == str(number)[::-1]

def reverse_number(number):
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10
    return reversed_number
def main():
    while True:
        print("Number Menu:\n")
        print("1. Palindrome of a string\n")
        print("2. Palindrome of a number\n")
        print("3. Reverse of a number\n")
        print("4. Exit\n")

        choice = input("Enter your selection:\n")
        if choice == '1':
            input_string = input("Enter prefered string:\n")
            if is_palindrome_string(input_string):
                print("The given string is a palindrome!")
            else:
                print("The given string is not a palindrome!")
        elif choice == '2':
            input_number = input("Enter the prefered number:\n")
            if is_palindrome_number(input_number):
                print("The given number is a palindrome!")
            else:
                print("The given number is not a palindrome!")
        elif choice == '3':
            input_number = int(input("Enter the number:"))
            result = reverse_number(input_number)
            print("The reversed number is:",result)
        elif choice == '4':
            print("Exiting program.....\n")
            break
        else :
            print("INVALID INPUT! ENTER AGAIN.\n")
if __name__ == "__main__":
    main()
