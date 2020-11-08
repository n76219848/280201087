
day = int(input("Enter the day : "))
month = str(input("Enter the month : "))


if ( 20 <=  day <= 31 and month =='March') or ( 1 <= day <= 31 and month=='April') or (1 <= day <= 31 and month =='May') or (1 <= day <= 20 and month=='June' ):
    print("Spring!")
elif ( 21 <=  day <= 31 and month =='June') or ( 1 <= day <= 31 and month=='July') or (1 <= day <= 31 and month =='August') or (1 <= day <= 20 and month=='September' ):
    print("Summer!")
elif( 21 <=  day <= 31 and month =='September') or ( 1 <= day <= 31 and month=='October') or (1 <= day <= 31 and month =='November') or (1 <= day <= 20 and month=='December' ):
    print("Fall!")
elif( 21 <=  day <= 31 and month =='December') or ( 1 <= day <= 31 and month=='January') or (1 <= day <= 31 and month =='February') or (1 <= day <= 20 and month=='March' ):
    print("Winter!")
elif day < 0 and day > 31 :
    print("Enter valid day pls ")
else:
  print("Get out of here!!!!")
