#Hocam bilerek şifreyi inputla istedim abc123 le yapınca kolay oluyordu :D
define_your_password = input("Enter your password : ")
enter_password = input("Enter your password : ")

while enter_password != define_your_password:
    print('Wrong')
    enter_password = input("Please Enter Your Password Again : ")
    if enter_password == 'help':
        print(define_your_password[0])
        break
if enter_password == define_your_password:
    print("Welcome ")
