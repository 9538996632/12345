
import random
count=0
while(count<=100):
    roll=input("press r to roll a dice")
    if(roll=='r'):
        r=random.randint(1,6)
        count=count+r
    print("your dice value")
    print(r)
    print("your count value")
    print(count)
    if(count==8):
        count=37
        print("you climb the ladder")
    if(count==11):
        count=2
        print("snake has bitten you")
    if(count==13):
        count=34
        print("you climb the ladder")
    if(count==25):
        count=4
        print("snake has bitten you")
    if(count==38):
        count=9
        print("snake has bitten you")
    if(count==40):
        count=68
        print("you climb the ladder")
    if(count==52):
        count=81
        print("you climb the ladder")
    if(count==65):
        count=46
        print("snake has bitten you")
    if(count==76):
        count=97
        print("you climb the ladder")
    if(count==89):
        count=70
        print("snake has bitten you")
    if(count==93):
          count=64
          print("snake has bitten you")
    if(count>=100):
        print("i won the game")
        
