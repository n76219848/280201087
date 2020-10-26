age=int(input("Enter your age : "))
ticket = 3

if(age<= 6 and age>= 60 ):
  print("Free")
elif(age>6 and age<18):
  print(" You are going to pay : ", (ticket/2), "TL" )
else:
  print("The Ticket is 3 TL")
  