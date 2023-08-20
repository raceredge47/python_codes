#Swastik pattern
size=int(input("Enter a size"))
if(size%2==0):
    print("For better result please enter odd number")
else:
    for i in range(size):
        for j in range(size):
            if(i==0 and (j==0 or j>=size//2)):
                print("*",end=" ")
            elif(i>0 and i<size//2):
                if(j==0 or j==size//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            elif(i==size//2):
                print("*",end=" ")
            elif(i>size//2 and i<size-1):
                if(j==size//2 or j==size-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            elif(i==size-1):
                if((j>=0 and j<=size//2) or j==size-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            else:
                print(" ",end=" ")
        print()