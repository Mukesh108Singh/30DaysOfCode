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

def days_in_month(myear,mmonth):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  leap_y = is_leap(year)

  if leap_y :
    month_days[1] = 29
    print(month_days[month - 1])
  elif not leap_y:
    print(month_days[month - 1])
    
''' if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]
'''

#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
