num = int(input("Enter a Number: "))
sum = 0

if num == sum:
     print(num,"is an Armstrong Number")
else:
     print(num,"is not an Armstrong Number")

temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

