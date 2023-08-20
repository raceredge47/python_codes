#Sum of digit of number
#245 = 2+4+5
num=int(input("Enter number:"))
n=num
sum1=0
while(num>0):
    rem=num%10
    sum1=rem+sum1
    num=num//10
print("sum of digit of %d is %d"%(n,sum1))