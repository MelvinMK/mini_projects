def isPalindrome(str):
    rev = ''.join(reversed(str))
    if (str == rev):
        return True
    return False
str = input("What is the string?\n")
if (isPalindrome(str)):
    print("Yes, it is a palindrome!")
else:
    print("No, it is not a palindrome!")