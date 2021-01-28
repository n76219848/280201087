def selection_sort(numbers):
  n = len(numbers)
  for i in range(n-1):
    smallest = i
    for bottom_index in range(i+1,n):
        if numbers[bottom_index]<numbers[smallest]:
            smallest = bottom_index
    numbers[i],numbers[smallest] = numbers[smallest],numbers[i]
  return numbers

print(selection_sort([1,4,2,3]))

