# write a program that check number is positive

number = float(input("enter a number : "))

if number>0:
      print(f"{number} is positive")
      
if number<0:
      print(f"{number} is negetive")
      
if number==0:
      number=int(number)
      print(f"{number} is zero")