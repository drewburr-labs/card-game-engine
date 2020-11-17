# card-game-engine

A Python program meant to handle the logic behind dealing and managing rules for a card game.

The idea is for this program to be the dealer of a card game. The dealer sets up and shuffles the desk(s), and deals the appropriate number of cards to players.

## Definitions

### Card

A single card. The base object has a name and an integer value. High-level objects such as suits and colors will need to be handled externally.

### Deck

A tuple of card values, meant to represent an unopened box of cards. This should be used purely to define what a "deck" means to the game.

### Draw pile

A list of cards, instantiated from the Deck. These are the valid, playable cards. This should be reinstantiated every time a shuffle is performed.

### Discard pile

A list of cards that have been discarded.

### Dealer

The top-level object used to access all the cards, piles, etc.
