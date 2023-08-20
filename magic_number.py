#magic number
num=int(input("Enter a number"))
rem=0
n=0
while(num<0):
	n=num%10
	rem=rem+n
    num=num//10
print(rem)