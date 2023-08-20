#Fibonacci series
#0 1 1 2 3 5 8 . . . . . . 
a=0
b=1
ctr=0
size=int(input("Enter size of series:"))
while(ctr<size-1):
    if(ctr==0):
        print(a,b,end=" ")
    else:
        a,b=b ,a+b
        print(b,end=" ")
    ctr=ctr+1