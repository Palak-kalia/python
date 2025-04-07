import random
n=random.randint(0,9)
print("******************GUESS THE RIGHT NUMBER*******************")
for i in range(0,9):
    m=int(input("guess any number from 0-9 ="))
    if(n==m):
        print("you have guessed the right number")
        break
    elif(m!=n):
        print("try again")
    else:
        print("default")
