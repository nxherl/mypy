import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(u_score, o_score):
    if u_score == o_score:
        return "it's a draw 🙃"
    elif o_score == 0:
        return "You lose! Opponent got a BlackJack! 😱"
    elif u_score == 0:
        return "You win with a BlackJack! 😎"
    elif u_score > 21:
        return "You went over 21..You lose! 😭"
    elif o_score > 21:
        return "Opponent went over 21..You win! 😁"
    elif u_score > o_score:
        return "You win! 😃"
    else:
        return "You lose! 😭"

def play_game():
    print(logo)
    user_cards = []
    opponent_cards = []
    game_over = False
    user_score = -1
    opponent_score = -1

    for i in range(2):
        user_cards.append(deal_card())
        opponent_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        opponent_score = calculate_score(opponent_cards)

        print(f"Your cards: {user_cards}, current_score: {user_score}")
        print(f"Opponent's first card: {opponent_cards[0]}")

        if user_score == 0 or opponent_score == 0 or user_score > 21:
            game_over = True
        else:
            redeal = input("Type 'y' to get another card, type 'n' to pass: \n")
            if redeal == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while opponent_score != 0 and opponent_score < 17:
        opponent_cards.append(deal_card())
        opponent_score = calculate_score(opponent_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Opponent final hand: {opponent_cards}, final score: {opponent_score}")
    print(compare(user_score, opponent_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()




















