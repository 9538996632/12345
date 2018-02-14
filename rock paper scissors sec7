from random import randint
c=1
while(c==1):
    s= ["Rock", "Paper", "Scissors"]
    computer = s[randint(0,2)]
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
        
    b=int(input("enter 1 to play again or exit to any number"))
    if(b==1):
          print("ok")
    else:
          c=c-2
          print("thank u")
