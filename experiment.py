import random
options = ['r','p','s']
playerPoints=0
botPoints=0

print("Hello, welcome to rock paper scissors. We are going to be playng to 3")
print("Type:")
print("r - rock")
print("p - paper")
print("s - scissors")


def printPoints():
    print('New score is:')
    print('you - ', str(playerPoints))
    print('me - ', str(botPoints))


while playerPoints<3 and botPoints<3:
    botOption=random.choice(options)
    print('Tell me your pick.')
    playerOption=input()
    if botOption == playerOption:
        print('It is a draw.')
        printPoints()
        
    if botOption==options[0]:
        if playerOption=='p':
            print('You won!')
            playerPoints=playerPoints+1
            printPoints()
        elif playerOption=='s':
            print('You lost.')
            botPoints=botPoints+1
            printPoints()
    if botOption==options[1]:
        if playerOption=='r':
            print('You won!')
            playerPoints=playerPoints+1
            printPoints()
        elif playerOption=='s':
            print('You lost.')
            botPoints=botPoints+1
            printPoints()
    if botOption==options[2]:
        if playerOption=='r':
            print('You won!')
            playerPoints=playerPoints+1
            printPoints()
        elif playerOption=='p':
            print('You lost.')
            botPoints=botPoints+1
            printPoints()
            
if playerPoints==3:
    print('Game over. YOU WON!')
if botPoints==3:
    print('Game over. YOU LOST!')
       





