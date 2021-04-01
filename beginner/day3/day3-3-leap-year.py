# We want to write a program that works out whether a given year is a leap year 
# a particular year is a leap year if:
# - the year number it is divisible by 4
# - it is not a year that is divisible by 100, unless it is also divisible by 400 

year = int(input("Enter any year: "))

if year % 4 == 0:
    if year % 400 == 0 or year % 100 != 0 :
        print(f"{year} is a leap year!")
    else:
        print(f"{year} is not a leap year!")
else:
    print(f"{year} is not a leap year!")

#elongated version:
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0: 
#             print(f"{year} is a leap year!")
#         else:
#             print(f"{year} is not a leap year!")
#     else:
#         print(f"{year} is a leap year!")
# else:
#     print(f"{year} is not a leap year!")
