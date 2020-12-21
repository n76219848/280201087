def is_valid(pw):
  valid = True
  uppercase = 0
  lowercase = 0
  number = 0
  if len(pw)<8:
      valid = False
      return valid
  for i in pw:
      if i.isalpha():
          if i.lower()==i:
              lowercase+=1
          elif i.upper()==i:
              uppercase+=1
      elif i.isnumeric():
          number+=1
  if uppercase!=0 and lowercase!=0 and number!=0:
      return True
input1 = input('Enter a password: ')
print(is_valid(input1))