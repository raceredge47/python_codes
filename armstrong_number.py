'''
Armstrong number is a number that is equal to the sum of cubes of its digits
'''

num =int(input("Enter Number"))
n=num
count=0
sum1=0
while(num>0):
    count+=1
    num=num//10
print(count)
num=n
while(num>0):
    rem=num%10
    sum1=sum1+rem**count
    num=num//10
print(sum1)
if(n==sum1):
    print(n,"is an armstrong number.")
else:
    print(n,"is not an armstrong number.")