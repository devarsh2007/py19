# and,or,not  logical operator

age = int(input("enter age : "))

if age>0 and age<100:
      print("valid age")
      
print("-"*50)

vowel = (input("enter vowel : "))

if vowel=="a" or vowel=="o" or vowel=="e" or vowel=="i" or vowel=="u":
      print(vowel)
      
print("-"*50)

# a=10
# print(not(a==10))

if not(vowel=="a" or vowel=="o" or vowel=="e" or vowel=="i" or vowel=="u"):
      print(vowel)