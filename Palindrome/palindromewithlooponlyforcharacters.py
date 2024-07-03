def isPalindrome(str):
    for i in range(0, int(len(str)/2)):
        if str[i] == str[len(str)-i-1]:
            return True
        return False
str = input("What is the string?\n")
if str.isdigit():
        print("Error: Input should be a string, not an integer.")
elif (isPalindrome(str)):
    print("Yes, it is a palindrome!")
else:
    print("No, it is not a palindrome!")
