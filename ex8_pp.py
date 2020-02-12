from random import shuffle
def computer_move():
    base = ['rock', 'paper','scisors']
    shuffle(base)
    return base[0]

def player_move():
    move = input("choose rock, scisors or paper ")
    return move

def results(comp, play):
    if comp == play:
        print("it's a draw")

    elif (comp == 'rock' and play == 'scisors') or \
        (comp == 'paper' and play == 'rock') or \
        (comp == 'scisors' and play == 'paper'):
        print("you lose")
    else:
        print("you won")

playing = 1

while playing:
    games = int(input("how many games do you want to play? "))
    index = 0
    while index < games:
        comp = computer_move()
        play = player_move()
        results(comp, play)
        index +=1
    decision = input("do you want to keep playing? ").lower()
    if decision == 'yes':
        playing = 1
    else:
        playing=0

