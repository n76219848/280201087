year = int(input('Enter the year pls : '))

if year % 100 == 0 and year %400 != 0:
  print('This is not leap year')
elif year % 4 == 0 or year%400 == 0:
  print('This year is  leap')
elif year %4  != 0:
  print("This Year is not  leap")