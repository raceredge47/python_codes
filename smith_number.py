#Smith number
num=int(input("Enter a number:"))
ctr=2
count=0
n=num
sum1=0
while(num>0):
    rem=num%10
    sum1=rem+sum1
    num=num//10
print("sum of digit of %d is %d"%(n,sum1))
num=n
while(ctr<=num):
    while(num%ctr==0):
        count=count+ctr
        print(ctr,end="*")
        num=num//ctr
    ctr+=1
print("\nsum of prime factor is %d"%(count))
if(sum1==count):
    print("%d = %d"%(count,sum1))
    print(n,"is a smith number.")
else:
    print("%d != %d"%(count,sum1))
    print(n,"is not a smith number.")