my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
print("Choose:")
print("\n1. ODD")
print("\n2. EVEN")
choice = input("\nEnter selection: ")

if choice == '1':
    odd_numbers = {number for number in my_set if number % 2 != 0}
    print("\nOdd numbers are:", odd_numbers)
elif choice == '2':
    even_numbers = {number for number in my_set if number % 2 == 0}
    print("\nEven numbers are:", even_numbers)
else:
    print("\nInvalid choice. Please enter '1' for ODD or '2' for EVEN.")
