# modify leap year function to return true if it is a leap year

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

# return how many days are in the month specified
# inputs: year, month

def days_in_month(year, month):
     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
     if is_leap(year) and month == 2:
          return month_days[month-1]+1
     return month_days[month-1]
     