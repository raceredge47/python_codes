# n odd number
terms=int(input("Enter number of trems"))
num=1
count=0
while(True):
    if(num%2!=0):
       print(num,end=" ")
       count+=1
       
    num+=1
    if(count==terms):
        break