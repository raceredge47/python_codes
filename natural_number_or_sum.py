# detect first n natural number
n=int(input("Enter a size"))
for i in range(1,n+1):
    print(i,end=" ")
    

#sum of n natural number0
n=int(input("\nEnter size"))
sum=0
for i in range(1,n+1):
    print(i,end=" ")
    sum+=i
print("\n sum of %d natural number is %d"%(n,sum))
