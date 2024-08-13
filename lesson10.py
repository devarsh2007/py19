# write a program that find simle interest

p = int(input("enter amout : "))
r = float(input("enter rate : "))
t = int(input("enter time : "))

si = (p*r*t) / 100

# fstring
print(f"simple interest : ₹{si}")
