books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict = {}
for i in books:
  book_dict[i] = 'value'
  value = len(i)
  unique_ch = len(set(i))
  average = (value+unique_ch)/2
  book_dict[i] = (value,unique_ch,average)
print(book_dict)