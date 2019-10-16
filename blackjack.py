#Doug Gryboski
#BlackJack_graphics.py

from graphics import *
import random

def gifname(card):
    gif = str(card[0])[0] + card[2][0]
    gif = gif.lower()
    if gif[0] == "1":
        gif = "t"+gif[1]
    gif = gif + ".gif"
    return gif

suits = ["Clubs","Hearts","Diamonds","Spades"]
ranks = [[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],[10,10],
         ["Jack",10],["Queen",10],["King",10],["Ace",11]]
cards = []
for suit in suits:
    for rank in ranks:
        cards.append([rank[0],rank[1],suit])

win = GraphWin("BlackJack",700,600)
win.setBackground("green")

ptext = Text(Point(250,550),"Player's Hand")
ptext.setFill(color_rgb(255, 255, 255))
ptext.draw(win)

dtext = Text(Point(250,75),"Dealer's Hand")
dtext.setFill(color_rgb(255, 255, 255))
dtext.draw(win)

x = 0
play = "go"
while play != "s":
    random.shuffle(cards)
    
    print ('______________THE DECK HAS BEEN SHUFFLED__________________')
    str(input('Hit enter to deal the cards.'))
    x = 0
    pcard1 = cards[x]
    dcard1 = cards[x+1]
    pcard2 = cards[x+2]
    dcard2 = cards[x+3]
    playerlist = [] #this establishes an empty list named playerlist
    dealerlist = [] #this establishes an empty list named dealerlist
    playerlist.append(pcard1[1]) #this append() method adds an item to the list
    playerlist.append(pcard2[1])
    dealerlist.append(dcard1[1])
    dealerlist.append(dcard2[1])
    playertotal = sum(playerlist)
    dealertotal = sum(dealerlist)
    x += 4
    print ('You have a ',pcard1[0],'of ',pcard1[2],'and a ',pcard2[0],'of ',pcard2[2])
    print ('for a total of ', playertotal)
    print ('Dealer is showing a ', dcard1[0], 'of ', dcard1[2])

    #graphics - player card #1
    i = Image(Point(200,450),"cards/"+gifname(pcard1))
    i.draw(win)

    #graphics - player card #2
    ii = Image(Point(300,450),"cards/"+gifname(pcard2))
    ii.draw(win)

    #playertotal on screen
    ptotaltext = Text(Point(330,550),playertotal)
    ptotaltext.setFill(color_rgb(255, 255, 255))
    ptotaltext.draw(win)

    #graphics - 1st Dealer card
    j = Image(Point(200,150),"cards/"+gifname(dcard1))
    j.draw(win)
   
    hit = str(input('Would you like to hit or stand? (type h or s)'))
    xposnextcard = 400
    counter = 0
    while hit == "h":
        print ('Ok, you chose to hit.')
        pcardnext = cards[x]
        counter = str(counter)
        drawname = "next"+counter
        counter = int(counter)
        counter+=1
        x += 1
        playerlist.append(pcardnext[1])
        playertotal = sum(playerlist)
        #graphics - player card hit
        drawname = Image(Point(xposnextcard,450),"cards/"+gifname(pcardnext))
        drawname.draw(win)
        #playertotal on screen
        ptotaltext.undraw()
        ptotaltext = Text(Point(330,550),playertotal)
        ptotaltext.setFill(color_rgb(255, 255, 255))
        ptotaltext.draw(win)
        
        xposnextcard +=100
        print ('Your next card is a ', pcardnext[0], 'of', pcardnext[2])
        aces = playerlist.count(11)
        if playertotal > 21 and aces > 0:
            playerlist.remove(11)
            playerlist.append(1)               
            playertotal = sum(playerlist)
            print ('An ace value has been changed to 1 point. ')
            print ('Your new total is ', playertotal)
            #ace change text in win
            acechangetext = Text(Point(300,580),"An ace value has been changed to 1 point.")
            acechangetext.setFill(color_rgb(255, 255, 255))
            acechangetext.draw(win)
            #playertotal on screen
            ptotaltext.undraw()
            ptotaltext = Text(Point(330,550),playertotal)
            ptotaltext.setFill(color_rgb(255, 255, 255))
            ptotaltext.draw(win)
            hit = str(input('Would you like to hit or stand? (type h or s)'))
        elif playertotal > 21:
            print ('Your new total is ', playertotal)
            print ('You busted!  Dealer Wins this one.')
            #bust text in win
            busttext = Text(Point(350,350),"You busted!  Dealer Wins this one.")
            busttext.setFill(color_rgb(255, 255, 255))
            busttext.draw(win)
            hit = "s"
        else:
            print ('Your new total is ', playertotal)
            hit = str(input('Would you like to hit or stand? (type h or s)'))
        
    if playertotal > 21:
        print ()
    else:
        print ('Ok! You stand on ',playertotal, "Now it's the Dealer's turn.")
        print ('Dealer has a ',dcard1[0], 'of ',dcard1[2],'and a ',dcard2[0],'of ',dcard2[2])
        print ('for a total of ', dealertotal)
        while dealertotal < 17:
            print ('Dealer must hit.')
            dcardnext = cards[x]
            x += 1
            dealerlist.append(dcardnext[1])
            dealertotal = sum(dealerlist)
            print ("Dealer's next card is a ", dcardnext[0], 'of', dcardnext[2])
            aces = dealerlist.count(11)
            if dealertotal > 21 and aces > 0:
                dealerlist.remove(11)
                dealerlist.append(1)               
                dealertotal = sum(dealerlist)
                print ("A dealer's ace value has been changed to 1 point. ")
                print ("Dealer's new total is ", dealertotal )
            elif dealertotal > 21:
                print ("Dealer's new total is ", dealertotal)
                print ('Dealer busted!  You WIN!!!.')
            else:
                print ("Dealer's new total is ", dealertotal)
                    
        if dealertotal > 21:
            print()
        else:
            print ('Dealer must stand on', dealertotal)
            if playertotal > dealertotal:
                print ('Congratulations!!!!!!!! You Win!!!!!!')
            elif dealertotal > playertotal:
                print ('The Dealer wins this ocounter+=1ne.')
            else:
                print ("That's a push!  No one wins.")

    play = str(input('Type s to stop playing or press enter to play again '))
    ptotaltext.undraw()
    i.undraw() #undraw playercard1
    ii.undraw()  #undraw playercard2
    for i in range(counter-1):
        counter = str(i)
        drawname = "next"+counter
        print(drawname)
        drawname.undraw()
    j.undraw()   #undraw dealercard1







    
