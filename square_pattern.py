#pattern 
'''
* * * * *
*       *
*       *
*       *
* * * * *
'''
size=int(input("Enter a size"))
for i in range(size):
    for j in range(size):
        if(i>0 and i<size-1):
            if(j>0 and j<size-1):
                print(" ",end=" ")
            else:
                print("*",end=" ")
        else:
            print("*",end=" ")
    print()
           
       