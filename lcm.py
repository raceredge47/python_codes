#L.C.M of two numbers
num=int(input("Enter a first number."))
num1=int(input("Enter a second number."))
n=num
n1=num1
ctr=2
count=1
while(ctr<=num or ctr<=num1):
    while(num%ctr==0 and num1%ctr==0):
        print(ctr,end=" ")
        count=count*ctr
        num=num//ctr
        num1=num1//ctr
    ctr+=1
print(num,"",num1)   
print("L.C.M of %d and %d is %d"%(n,n1,count*num*num1))    