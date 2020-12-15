def sumsquarelist(mylist):
  sumlist = []
  limit = int(input('Enter the number : '))
  for i in range(limit):
      a = int(input('Enter the elements of list : '))
      sumlist.append(a*a)
  return sum(sumlist)
mylist = []
print(sumsquarelist(mylist))