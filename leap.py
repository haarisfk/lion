year = int(input("Enter a year: "))

def checkleap(year):
    if ((year % 400 == 0) or
        (year % 100 != 0) and
        (year % 4 == 0)):
        print(year,"is leap year")
    else:
        print(year,"is not a leap year")

checkleap(year)