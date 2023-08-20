#perfect number
num=int(input("Enter a number"))
ctr=1
count=0
while(ctr<=num):
    if(num%ctr==0):
        count=count+ctr
    ctr+=1      
print("sum of factor of %d is %d"%(num,count))
if(count==2*num):
    print(num,"Is a perfect number.")
else:
    print(num,"Is not a perfect number.")