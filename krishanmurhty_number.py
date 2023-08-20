#krishanmurhty number
num=int(input("Enter a number"))
count=0
sum1=0
n=num
while(num>0):
    rem=num%10
    fact=1
    while(rem>0):
        fact=fact*rem
        rem=rem-1
    sum1=sum1+fact
    num=num//10
if(sum1==n):
    print(n,"is a krishanmurti number.")
else:
    print(n,"is not a krishanmurti number.")