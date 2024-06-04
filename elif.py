# write a program to display days

day = int(input("enter a number from 1 to 7 : "))

if day==1:
      print("sunday")
      
elif day==2:
      print("monday")
      
elif day==3:
      print("tuesday")
      
elif day==4:
      print("wednesday")
      
elif day==5:
      print("thursday")
      
elif day==6:
      print("friday")
      
elif day==7:
      print("saturday")
      
elif day>7:
      print("invalid input")
      
elif day<1:
      print("out of range")