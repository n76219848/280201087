n = int(input('Enter a num: '))
mylist = []
for i in range(n):
    a = [0]*n
    a[i] = 1
    mylist.append(a)
for row in mylist:
    print(row)