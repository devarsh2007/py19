# write a program that find letter is vowel,consonent

string = input("enter a latter : ")
# print(len(string))

if string=="a" or string=="e" or string=="i" or string=="o" or string=="u":
      print("vowel")
      
elif len(string) > 1 or len(string)<1:
      print("invalid input")
      
else:
      print("consonat")