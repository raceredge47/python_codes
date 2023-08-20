#stone paper scissor
import random as r
c=r.choice(['paper','stone','scissor'])
print("Press 1 for select paper.")
print("Press 2 for select stone.")
print("Press 3 for select scissor.")
choice=input("Enter your choice")
if(choice=='1'):
    user='paper'
elif(choice=='2'):
    user='stone'
elif(choice=='3'):
    user='scissor'
else:
    print("Invalid choice")
print("Computer choice is ",c)
print("User choice is ",user)
if(c==user):
    print("Match tie")
elif((user=='paper' and c=='stone') or (user=='stone' and c=='scissor') or (user=='scissor' and c=='paper')):
    print("User won the match")
else:
    print("computer won the match")