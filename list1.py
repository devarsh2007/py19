employee = ["devarsh",17,48.57,True] 
print(employee)

employee2 = [19,23.7,"param"]
print(employee2)

print("name : ",employee[0])
print(employee2[2])
print(employee[1])
print(employee[3])

print(employee2+employee)
print(employee[0]+" "+employee2[2])
print(employee[0]+str(employee2[0])) # type casting

print("--------------------------------------------")
numbers = [10,20,30,40,50,60,70,80,90,100]
print(len(numbers))

print(numbers[::-10])
print(numbers[5:])
print(numbers[0::2])

print(numbers*5)

print("------------------------------------------------")

city = ["Ahmedabad", "Surat", "Vadodara", "Rajkot", "Bhavnagar", "Jamnagar", "Junagadh", "Gandhinagar", "Anand", "Nadiad"]

numbers= [5,3,5,32,7,6,3,1]
print(city)

city.append("amreli")
print(city)

city.insert(5,"godhra")
print(city)

city.extend(numbers)
print(city)

city.remove("godhra")
print(city)

city.append(numbers)
print(city)

city.remove(numbers)
print(city)

city.pop(3)
city.pop(0)
print(city)

# city.clear()
# print(city)

print(city.index(5))
city.append("Surat")
city.append("Surat")
city.append("Surat")
print(city.count(4))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

new = city.copy()
print(new)
new.append(101)
print(new)
print(city)