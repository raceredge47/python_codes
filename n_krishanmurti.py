#first n krishanmurti number
terms=int(input("Enter a size"))
num=1
n=num
count=0
while(True):
    sum1=0
    while(num>0):
        rem=num%10
        fact=1
        while(rem>0):
            fact=fact*rem
            rem=rem-1
        sum1=sum1+fact
        num=num//10
    if(sum1==n):
        print(n,end=" ")
        count+=1
            
    if(count==terms):
        break
    num=n
    n+=1
    num+=1