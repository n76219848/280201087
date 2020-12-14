check = 'ceng113@example.com'
email = input('Enter an e-mail').lower()
items = email.split('@')
items[0] = items[0].replace('.','')
mystring = items[0]+'@'+items[1]
if mystring==check:
    print('true')
else:
    print('false')