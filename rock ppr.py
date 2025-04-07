import random
print("****************GAME******************")
game=["rock","paper","scissor"]
# computer=random.choice(game)
for i in range (5):
    computer=random.choice(game)
    player=input("enter rock or paper or scissor =")
    if(computer=="rock"):
        if(player=="rock"):
            print("its a tie")
        elif(player=="paper"):
            print("you won")
        else:
            print("you lose")
    elif(computer=="paper"):
        if(player=="rock"):
            print("you loose")
        elif(player=="paper"):
            print("you tie")
        else:
            print("you win")
    else:
        if(player=="rock"):
            print("you won")
        elif(player=="paper"):
            print("youn lose")
        else:
            print("its tie")
