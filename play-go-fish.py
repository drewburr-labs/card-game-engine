# play-go-fish.py
"""
Used to handle a game of go fish
"""

import random

deck_values = tuple(range(52))

pile = list(deck_values)

random.shuffle(pile)

print(f"Pile: {pile}")


class Player():
    def __init__(self, name):
        self.name = name
        self._hand = list()

    # Provide a way to get the player's hand
    @property
    def hand(self):
        return list(self._hand)

    def print_hand(self):
        print(f"{self.name}'s hand: {self._hand}")

    def add_cards(self, cards):
        """
        Adds cards to the player's hand.
        Hand is always re-sorted.
        """
        for value in cards:
            self._hand.append(value)

        self._hand.sort()

    def play_books(self):
        """
        Returns a list of books in-hand.
        The returned cards are removed from the player's hand.
        """
        # {value: count}
        books = dict()
        for value in self._hand:
            # Get the number of times the value appears
            count = self._hand.count(value)

            # If value appears 4 times, the player has a book
            if count == 4:
                # Remove each value found
                for _ in range(count):
                    self._hand.remove(value)

                books[value] = count

        return books


players = [
    Player('player 1'),
    Player('player 2'),
    Player('player 3')
]

# value: player_name
table = {}

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
        player.print_hand()

        # Check if book is already on the table
        if table.get(value):
            raise ValueError(
                f"{player.name} played an existing book! Value: {value} Count: {count}")
        else:
            # Add book to table
            table[value] = player.name


# Players play existing books
for player in players:
    books = player.play_books()
    add_books_to_table(books)

playing = True
while playing:

    # Reset variables
    another_turn = False

    # Left-most player goes first
    player = players.pop(0)

    # And always asks the next player for a card
    next_player = players[0]

    # Ask next player for a card
    ask_card = player.hand[0]

    card_count = next_player.hand.count(ask_card)
    print(f"{player.name}: Asked {next_player.name} for a {ask_card}.")

    if card_count > 0:
        for x in range(card_count):
            next_player.hand.remove(ask_card)
            player.hand.append(ask_card)

        player.hand.sort()
        print(
            f"{player.name}: Took {card_count} {ask_card}(s) from {next_player.name}")
        player.print_hand()
        next_player.print_hand()
    else:
        print(f"{next_player.name}: Does not have a {ask_card}. Go fish.")
        draw_card = 1 + pile.pop() % 13
        player.hand.append(draw_card)
        player.hand.sort()

        print(f"{player.name}: Drew a {draw_card}.")
        player.print_hand()

        if draw_card == ask_card:
            another_turn = True
            print(f"{player.name}: Gets to take another turn.")

    # Player places down sets of 3 or more
    books = player.play_books()
    add_books_to_table(books)

    # Check if the game is over (A player runs out of cards, or deck is empty)
    if len(player.hand) == 0 or len(next_player.hand) == 0 or len(pile) == 0:
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
