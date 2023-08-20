#Prime number
num = int(input("Enter a number:"))
ctr = 2
flag = 0
while(ctr<num):
    if(num%ctr == 0):
        flag = 1
        break
    ctr = ctr + 1
if(flag == 0 and num>=2):
    print(num,"is a prime number.")
else:
    print(num,"is not a prime number.")