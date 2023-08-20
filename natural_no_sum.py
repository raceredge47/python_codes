#first n natural num sum
terms= int(input("Enter number of terms"))
num=1
sum=0
while(num<terms+1):           #we can write both while(condition) or while(True) loop int this case beacuse of if statements
        sum+=num
        num+=1
        if(num==terms+1):
           break
print(sum,end=" ")
