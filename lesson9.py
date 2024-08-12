# write a program that find area of circle

print("---------circle area------------")
r = float(input("enter radius : "))

area = 3.14 * r * r
print("circle area : ",area)

print("\n----------triangle area------------")
b=float(input("enter base : "))
h=float(input("enter height : "))

area = b*h*0.5
print("triangle area : ",area)

print("\n--------------square area----------------")

a = float(input("enter lenth : "))
area = a * a
print("square area : ",area)

print("\n---------------rectangle area-----------------")

w = float(input("enter width : "))
h = float(input("enter height : "))
area = w*h
print("rectangle area : ",area)

print("\n-----------------cylinder area---------------------")

r = float(input("enter radius : "))
h = float(input("enter height : "))
pi = 3.14

area = (2 * pi * r * h)  +  (2 * pi * r * r)
print("cylinder area : ",area)
