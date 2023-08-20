#Leap year checking
num = int(input("Enter year"))
if(num%4==0):
     if(num%100==0):
          if(num%400==0):
              print("Leap year")
          else:
              print("Not Leap year")
     else:
           print("Leap year")
else:
      print("Not Leap year")