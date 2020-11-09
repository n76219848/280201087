a = int(input("Enter a pls : "))
b = int(input("Enter the power pls : "))
# we have to find a^b.
power = a
for i in range(1,b):
  power = power*a
print(power)

