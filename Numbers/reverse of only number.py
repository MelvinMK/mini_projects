def reversed_num(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num
input_num = int(input("Enter the number:"))
result = reversed_num(input_num)
print("The reversed number is:",result)