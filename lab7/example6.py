numbers1 = [2,3,4,20,5,5,15]
numbers2 = [10,20,20,15,30,40]
set1 = set(numbers1)
set2 = set(numbers2)
subone = set1-set2
subtwo = set2-set1
set1.update(set2)
subone.update(subtwo)
print(set1)
c = set1-subone
print(c)
