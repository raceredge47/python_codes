#H.C.F
num=int(input("Enter a first number."))
num1=int(input("Enter a second number."))
ctr=1
count=0
while(ctr<=num or ctr<=num1):
    
    if(num%ctr==0 and num1%ctr==0):
        count=1
        print(ctr)
        count=count*ctr
    ctr+=1
print("H.C.F of %d and %d is %d"%(num,num1,count))