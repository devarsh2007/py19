# write a program that find average of 3 numbers

num1 = float(input("enter number1 : "))
num2 = float(input("enter number2 : "))
num3 = float(input("enter number3 : "))

average = (num1+num2+num3)/3
# print("average of",num1,num2,num3,":",average)

# f string
print(f"average of {num1},{num2},{num3} : {average}")