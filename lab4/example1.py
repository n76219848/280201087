a = int(input('Enter the number pls : '))
if a<10:
  print(a)
elif 10 < a < 100:
  print("Enter the digits of number one by one pls")
  a1 = int(input('Enter the number pls : '))
  a2 = int(input('Enter the number pls : '))
  print("The sum of the digits : ", a1+a2)
elif 100 < a <1000:
  print("Enter the digits of number one by one pls : ")
  a1 = int(input('Enter the number pls : '))
  a2 = int(input('Enter the number pls : '))
  a3 = int(input('Enter the number pls : '))
  print("The sum of the digits : ", a1+a2+a3)
