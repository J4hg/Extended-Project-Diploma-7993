import random

dealertotal = 0
playertotal = 0

spades = [1,2,3,4,5,6,7,8,9,10,0]
hearts = [1,2,3,4,5,6,7,8,9,10,0]
diamonds = [1,2,3,4,5,6,7,8,9,10,0]
clubs = [1,2,3,4,5,6,7,8,9,10,0]
deck = [spades,hearts,diamonds,clubs]

def dealersuitcheck():
    if dealersuit == spades:
        print("of Spades")
    elif dealersuit == hearts:
        print("of Hearts")
    elif dealersuit == diamonds:
        print("of Diamonds")
    else:
        print("of Clubs")

def playersuitcheck():
    if playersuit == spades:
        print("of Spades")
    elif playersuit == hearts:
        print("of Hearts")
    elif playersuit == diamonds:
        print("of Diamonds")
    else:
        print("of Clubs")

def playergetcard():
    global playersuit, playertotal
    playersuit = random.choice(deck)
    playerhand = random.choice(playersuit)
    if playerhand in range (1,10):
        print(playerhand)
        playersuit.remove(playerhand)
    else:
        playeracechoice = input("Do you want your ace to be 11 or 1")
        if playeracechoice == "1":
            playersuit.remove(playerhand)
            playertotal = playertotal + 1
            print("1")
        elif playeracechoice == "11":
            playersuit.remove(playerhand)
            playertotal = playertotal + 11
            print("11")
        else:
            print("Invalid input")
    playersuitcheck()
    playertotal = playertotal + playerhand
    return playertotal

def dealergetcard():
    global dealersuit, dealertotal
    dealersuit = random.choice(deck)
    dealerhand = random.choice(dealersuit)
    if dealerhand in range (1,10):
        print(dealerhand)
        dealersuit.remove(dealerhand)
    else:
        if dealertotal + 11 <= 21:
            dealersuit.remove(dealerhand)
            dealertotal = dealertotal + 11
        elif dealertotal + 11 >= 21:
            dealersuit.remove(dealerhand)
            dealertotal = dealertotal + 1
    dealersuitcheck()
    dealertotal = dealertotal + dealerhand
    return dealertotal


run = True
while run:
    dealergetcard()
    dealersuit = random.choice(deck)
    dealerhand = random.choice(dealersuit)
    dealersuit.remove(dealerhand)
    dealertotal = dealertotal + dealerhand

    for x in range(2):
        playergetcard()
    print(playertotal)
    hitorstand = input("Do you want to hit or stand?")
    while hitorstand == "h":
        playergetcard()
        hitorstand = input("Do you want to hit or stand?")
        if playertotal == 21:
            print("You win!")
            run = False
    if hitorstand == "s":
        while dealertotal <= playertotal:
            print("This is the dealers total:", dealertotal)
            pause = input("[PRESS]")
            dealergetcard()
            if dealertotal > 21:
                print("You win")
                run = False
        if dealertotal > playertotal and dealertotal <=21:
            print("You lose")
            run = False






