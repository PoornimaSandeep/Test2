import random

Suites=["heart","clubs","Spade","Diamonds"]
ranks=["2","3","4","5","6","7","8","9","10","jack","Queen","King","aec"]
cards=[]
card_value={}

for i in Suites:
    for j in ranks:
        cards.append(f"{i} of {j}")

print(cards)

start=2

for i in cards:
    card_value[i]=start
    start+=1
    if(start>=14):
        start=2

play_card=random.sample(cards,len(cards))

player1=input("Enter player1 name")
player2=input("Enter player2 game")
play1_card=[]
play2_card=[]

for i in range(len(play_card)):
    if(i%2 != 0):
        play1_card.append(play_card[i])
    else:
        play2_card.append(play_card[i])
Score_play1=0
Score_play2=2
for i in play1_card:
    if i in card_value:
        Score_play1 +=card_value[i]

for i in play1_card:
    if i in card_value:
        Score_play2 +=card_value[i]

print(Score_play1)
print(Score_play2)
if(Score_play1>Score_play2):
    print(f"{player1} you are the winner")
else:
    print(f"{player2} you are the winner")




