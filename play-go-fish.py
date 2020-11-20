# play-go-fish.py
"""
Used to handle a game of go fish
"""

import random
from src.player import Player

deck_values = tuple(range(52))

pile = list(deck_values)

random.shuffle(pile)

print(f"Pile: {pile}")


class RuleError(Exception):
    """Raised when a player breaks the rules."""
    pass


players = [
    Player('player 1'),
    Player('player 2'),
    Player('player 3')
]

# value: player_name
table = {}

# Define other players
player_names = list()
for player in players:
    player_names.append(player.name)

print(player_names)

for player in players:
    player.other_players = list(player_names)
    player.other_players.remove(player.name)


# Deal cards to players
for player in players:
    # Take 7 cards from the pile
    cards = list()
    for x in range(5):
        cards.append(1 + pile.pop() % 13)

    # Pass cards to the player
    player.add_cards(cards)
    player.print_hand()


def add_books_to_table(books):
    """
    Used to add books to the table.
    Throws ValueError if book is already on the table.
    """
    # Place books on the table
    for value, count in books.items():
        # Player should have removed cards from hands. Print log
        print(f"{player.name}: Lays down a set of {count} {value}'s")

        # Check if book is already on the table
        if table.get(value):
            raise RuleError(
                f"{player.name} played an existing book! Value: {value} Count: {count}")
        else:
            # Add book to table
            table[value] = player.name


def get_player(player_name):
    """
    Used to get a player, by name.
    """

    for player in players:
        if player.name == player_name:
            return player

    return None


# Players play existing books
for player in players:
    books = player.play_books()
    add_books_to_table(books)

playing = True
while playing:

    # Reset variables
    another_turn = False
    cards = list()

    # Left-most player goes first
    player = players.pop(0)

    req_player_name, card_value = player.start_turn()

    req_player = get_player(req_player_name)

    print(f"{player.name} asked {req_player.name} for {card_value}s.")

    # Check if player requested a card in their hand
    if player.hand.count(card_value):
        cards = req_player.respond_to_player(card_value)
    else:
        raise RuleError(
            f"{player.name}: Does not have a {card_value} in-hand.")

    if cards:
        # Ensure all cards have the same value
        if len(cards) == cards.count(cards[0]):
            print(
                f"{req_player.name}: Gives {len(cards)} {cards[0]} to {player.name}")

            # Ensure req_player removed cards from hand
            if req_player.hand.count(cards[0]):
                raise RuleError(
                    f"{req_player.name} did not remove cards from their hand.")

        else:
            print(cards)  # Debugging
            raise RuleError(
                f"{req_player.name} returned multiple card values.")
    else:
        print(f"{req_player.name}: Does not have a {card_value}. Go fish.")

        # Ensure req_player did not have the card
        if req_player.hand.count(card_value):
            raise RuleError(f"{req_player.name} had a {card_value} in-hand.")

        draw_card = 1 + pile.pop() % 13
        cards.append(draw_card)
        print(f"{player.name}: Drew a {draw_card}.")

        if draw_card == card_value:
            another_turn = True
            print(f"{player.name}: Gets to take another turn.")

    player.add_cards(cards)
    books = player.play_books()
    add_books_to_table(books)

    player.print_hand()
    req_player.print_hand()

    # Check if the game is over (A player runs out of cards, or deck is empty)
    if len(player.hand) == 0 or len(req_player.hand) == 0 or len(pile) == 0:
        # Someone ran out of cards. End the game.
        playing = False
        players.append(player)
    else:
        if another_turn:
            # Add player to the left-most side, for another turn
            players.insert(0, player)
        else:
            # Add player to the right-most side
            players.append(player)

# Tally up the points
totals = dict()
for player in players:
    totals[player.name] = 0

for player_name in table.values():
    totals[player_name] += 1

# Print the scores
for player_name, score in totals.items():
    print(f"{player_name} ended with {score} points.")

    # Determine the number of players (2)

    # Global rules
    # If any player has a card the matches a set on the table, they must place it down.
    # If any player has a set of 3 or more cards, they must place it on the table.
    ##

    # Setup
    # Deal 7 cards to each player
    # Players place all 3 of a kind and 4 of a kind on the table
    # Players complete existing sets if possible

    # Start loop

    # Request number
    # Player 1 asks player 2 for a number (player 1 must have number in hand)

    # Player 2 responds to player 1 with cards
    # Player 1 draws card if no cards are received
    # Player 1 will take another turn if card drawn is the requested number

    # Player 1 places all 3 of a kind and 4 of a kind on the table

    # Turn change

    # Request number
    # Player 2 asks player 1 for a number (player 2 must have number in hand)

    # Reply with number
    # Player 1 responds to player 2 with cards
    # Player 2 draws card if no cards are received
    # Player 2 will take another turn if card drawn is the requested number

    # Place cards
    # Player 2 places all 3 of a kind and 4 of a kind on the table

    # Repeat loop

    # Loop ends when only one player has cards in their hand
    # The winning player has the most sets on the table
