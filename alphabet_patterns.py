#Alphabet pattern
'''
A
B C
D E F
G H I J 
K L M N O
'''
ch=65

for i in range(5):
    for j in range(i+1):
        var=chr(ch)
        print(var,end=" ")
        ch+=1
    print()
print("\n new code here \n")   
'''
A
A B 
A B C
A B C D
'''

size=int(input("Enter a size"))
for i in range(size):
    for j in range(65,65+i):
        ch=chr(j)
        print(ch,end=" ")
    print()


    

   

