import random

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
DECK = [f"{rank}{suit}" for suit in SUITS for rank in RANKS]

def deal(deck: list, n: int) -> list:
    """Deal n cards from the deck"""
    return [deck.pop() for _ in range(n)]
    

def main():
    print("Bienvenido al juego de Texas Holdem\n" + "-" * len("Bienvenido al juego de Texas Holdem"))

    shuffle_deck = random.shuffle(DECK)
    
    # Distribution of cards
    player = deal(shuffle_deck, 2)
    

