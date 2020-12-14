numberOfElements = int(input('Enter number of elements : '))
numList = []
for _ in range(numberOfElements):
    numList.append(int(input('Enter an int value: ')))
uniqueList = []
for item in numList:
    if item not in uniqueList:
        uniqueList.append(item)
uniqueList.sort(reverse=True)
print(uniqueList)
