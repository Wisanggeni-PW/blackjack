import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def cardPoint(dealt_card):
    if 'A' in dealt_card:
        value = 11
    elif 'K' in dealt_card or 'Q' in dealt_card or 'J' in dealt_card or '10' in dealt_card:
        value = 10
    elif '9' in dealt_card:
        value = 9
    elif '8' in dealt_card:
        value = 8
    elif '7' in dealt_card:
        value = 7
    elif '6' in dealt_card:
        value = 6
    elif '5' in dealt_card:
        value = 5
    elif '4' in dealt_card:
        value = 4
    elif '3' in dealt_card:
        value = 3
    elif '2' in dealt_card:
        value = 2
    else:
        value = 0
    return value


while True:
    deck = []
    score = 0
    joseph_score = 0
    player_turn = 'ongoing'
    for suit in suits:
        for rank in ranks:
            deck.append(f'{rank} of {suit}')
    random.shuffle(deck)
    
    print(('-'*22))
    print("WELCOME TO THE CASINO")
    print(('-'*22))
    if input('Would you like to play? (y/n)') == 'n':
        break
    dealt_card = deck.pop()
    print(f'\n\nYou drew {dealt_card}')
    score += cardPoint(dealt_card)
    print(f'Your Score: {score}')

    while True:
        if score > 21:
            print('You Busted!')
            break
        elif joseph_score > 21:
            print('Joseph Busted')
            break
        if player_turn == 'ongoing':
            if input('Would you like to hit or stand? (hit/stand)') == 'hit':
                dealt_card = deck.pop()
                print(f'\n\nYou drew {dealt_card}')
                score += cardPoint(dealt_card)
                print(f'Your Score: {score}')
            else:
                player_turn = 'end'
        elif player_turn == 'end_game':
            break
        else:
            print("\n\nJoseph's turn")
            dealt_card = deck.pop()
            print(f'Joseph drew {dealt_card}')
            joseph_score += cardPoint(dealt_card)
            print(f"Joseph's Score: {joseph_score}")
            if joseph_score > score and joseph_score < 22:
                print('Joseph Wins!')
                break
            else:
                input()
    break
