num=int(input("Enter a number:"))
temp=num
rev=0

while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10

if(temp==rev):
    print(temp,"is palindrome!")
else:
    print(temp,"is not a palindrome!")



string=input("Enter a string:")
if (string==string[::-1]):
    print(string,"is palindrome")
else:
    print(string,"is not a palindrome")