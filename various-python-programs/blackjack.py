import random

# Set up the deck of cards
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
deck = [(rank, suit) for rank in ranks for suit in suits]
random.shuffle(deck)

# Function to calculate the total value of a hand
def total(hand):
    total_value = 0
    aces = 0
    for card in hand:
        rank = card[0]
        if rank in ["Jack", "Queen", "King"]:
            total_value += 10
        elif rank == "Ace":
            aces += 1
            total_value += 11
        else:
            total_value += int(rank)
    while aces > 0 and total_value > 21:
        total_value -= 10
        aces -= 1
    return total_value

# Function to display a hand
def display(hand):
    for card in hand:
        print(card[0], "of", card[1])

# Set up the game
play_again = "yes"
while play_again.lower() in ["yes", "y"]:
    print("Let's play Blackjack!")
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    print("Your hand is:")
    display(player_hand)
    print("Dealer's hand is:")
    print(dealer_hand[0][0], "of", dealer_hand[0][1])
    if total(player_hand) == 21:
        print("Blackjack! You win!")
    else:
        while total(player_hand) < 21:
            action = input("Do you want to hit or stand? ")
            if action.lower() == "hit":
                player_hand.append(deck.pop())
                print("Your hand is now:")
                display(player_hand)
                if total(player_hand) == 21:
                    print("21! You win!")
                    break
                elif total(player_hand) > 21:
                    print("Bust! You lose!")
                    break
            elif action.lower() == "stand":
                dealer_total = total(dealer_hand)
                while dealer_total < 17:
                    dealer_hand.append(deck.pop())
                    dealer_total = total(dealer_hand)
                print("Dealer's hand is:")
                display(dealer_hand)
                if dealer_total > 21:
                    print("Dealer busts! You win!")
                elif dealer_total > total(player_hand):
                    print("Dealer wins!")
                elif dealer_total < total(player_hand):
                    print("You win!")
                else:
                    print("It's a tie!")
                break
    play_again = input("Do you want to play again? ")
print("Thanks for playing!")
