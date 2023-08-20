#Factorial of a number
num=int(input("Enter a number:"))
n=num
fact=1
while(num>0):
    fact=fact*num
    num=num-1
print("factorial of %d is %d"%(n,fact))