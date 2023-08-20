#prime factorization
num=int(input("Enter a number:"))
ctr=2
count=0
while(ctr<=num):
    while(num%ctr==0):
        if(ctr==num):
            print(ctr)
        else:
            print(ctr,end="*")
        num=num//ctr
    ctr+=1
