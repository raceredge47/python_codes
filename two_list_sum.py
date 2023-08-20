#list two items sum  
#list1=[234,56,25,2345,3456,450]
list1=[234,56,25,2345,3456,450]
sum=[]
i=0
while(i<=len(list1)-2):
    val=list1[i]+list1[i+1]
    sum.append(val)
    i=i+2
print(sum)