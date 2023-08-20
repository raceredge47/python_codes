'''
Greatest number check in three numbers.
'''

a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = int(input("Enter third number"))
if(a==b and b==c):
    print("All numbers are equal")
elif(a>=b and a>=c):
    print(a,"is greater")
elif(b>=c):
    print(b,"is greater")
else:
    print(c,"is greater")    