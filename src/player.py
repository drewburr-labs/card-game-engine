# player.py
"""
Used to handle all player logic.
"""

import random


class Player():
    def __init__(self, name):
        # The name of the player
        self.name = name
        # The player's hand. This is a private variable.
        self._hand = list()
        # A list of names of the opposing players.
        self.other_players = list()

    @property
    def hand(self):
        """
        Provides a read-only view of the player's hand.
        """
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
        Returns: list[int]
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

    def respond_to_player(self, requested_value):
        """
        Used to respond to card requests from other players.
        Returned cards are removed from the player's hand.
        Returns: list[int]
        """
        count = self._hand.count(requested_value)

        for _ in range(count):
            self._hand.remove(requested_value)

        return [requested_value] * count

    def start_turn(self, data=None):
        """
        Called to start the player's turn.
        This is where any/all game logic should be implemented.
        Returns tuple(str, int):
            The first element is the name of a player to request cards from
            The second element is the card value being requested
        """

        # Ask a random player for a card
        from_player = random.choice(self.other_players)
        # Ask for a random card value
        card_value = random.choice(self._hand)

        return from_player, card_value
