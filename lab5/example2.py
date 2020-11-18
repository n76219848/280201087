count = int(input("How many numbers ? "))
countforeven = 0
for i in range(count):
  a = int(input("Enter an integer : "))
  if a % 2 == 0:
    countforeven += 1
# now we have to convert integer to the %
countforeven = (countforeven / count)*100

print(f"{countforeven} %")
