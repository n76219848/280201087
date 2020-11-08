import math
a = float(input("Enter a :"))
b = float(input("Enter b : "))
c = float(input("Enter c : "))

delta = b*b - 4*a*c

if delta > 0:
  x1 = (-b + math.sqrt(delta))/2*a
  x2 = (-b - math.sqrt(delta))/2*a
  print("There are two real roots : \nx1 = ",x1,"\n x2 = ",x2)
elif delta == 0:
  x = -b/2*a
  print("There is one real root : ",x)
elif delta < 0:
  print("There are two complex roots.")
