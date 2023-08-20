#First n prime numbers
term = int(input("Enter a terms:"))
count=0
num=1
while(True):
    ctr = 2
    flag = 0
    while(ctr<num):
        if(num%ctr == 0):
            flag = 1
            break
        ctr = ctr + 1
    if(flag == 0 and num>=2):
        print(num,end=" ")
        count+=1
    if(count==term):
       break
    num+=1