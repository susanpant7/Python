import random

print("******game to roll dice******")
player1=input("enter your name player1")
player2=input("enter your name player2")

a=1
b=1
while a==1:
    go1 = int(input("player1 roll the dice by pressing 1"))
    if go1 == 1:
        p1=random.randint(1,6)
        print("the number for "+player1+ " is::::: "+str(p1))
        a=2
    else:
        print("Not valid...enter again...player1 enter 1 to start")

while b==1:
    go2 = int(input("player2 roll the dice by pressing 2"))
    if go2 == 2:
        p2=random.randint(1 , 6)
        print("the number for "+player2+ " is::::: "+str(p2))
        b=2
    else:
        print("player2 enter 2 to start")

if p1>p2:
    print("player 1 won ")
elif p2>p1:
    print("player 2 won")
else:
    print("its a draw")