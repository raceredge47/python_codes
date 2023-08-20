#detecting teenage,oldage or young age
age = int(input("Enter your age:"))
if(age>100 or age<1):
     print("Invalid input")
else:
      if(age<20):
           print("Teen age")
      elif(age>=20 and age<=40):
           print("young age")
      else:
           print("Old age")