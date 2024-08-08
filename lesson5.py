# string slicing-

name = "bhavnagar123"
# age="12.9"
print(len(name))
# print(len(age))

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7])
print(name[8])

print("\n--------------------------------------")
# print(name[start : end : size])
size = len(name)
print(name[0:12:1])

print(size)
print(name[0:size:1])

print(name[0:2:1])

text = " this is some text"
l = len(text)
print(text[0:7:1])

print(text[5:7:1])

print(text[8:12:1])
print("length : ",l)
a=0
print(text[l:0:-1])
# print(text[l:-1+1:-1])

data = "devarsh"
print(data[2::1])
print(data[:3:1])
print(data[0:7])
print(data[0:])
print(data[:])
print(data[::])
print(data[::-1])