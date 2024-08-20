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
print(city)

city.append("amreli")
print(city)

city.insert(5,"godhra")
print(city)
