from enum import IntEnum
from random import *

full_deck = []
partial_deck= []

class Card(IntEnum):
	ONE = 1
	TWO = 2
	THREE = 3
	FOUR = 4
	FIVE = 5
	SEVEN = 7
	EIGHT = 8
	TEN = 10
	ELEVEN = 11
	TWELVE = 12
	SORRY = 13

class PlayingCard:
	def __init__(self, value):
		self.value = value
		#self.img = png_images[f'{value}']

#Function to deal deck
def create_deck():
	full_deck.append(PlayingCard(Card(1)))
	for value in Card:
		full_deck.append(PlayingCard(Card(value)))
		full_deck.append(PlayingCard(Card(value)))
		full_deck.append(PlayingCard(Card(value)))
		full_deck.append(PlayingCard(Card(value)))
	return full_deck

def draw_card(deck):
	rand_card = randint(0, len(deck) - 1)
	return deck.pop(rand_card)

# def turn_cycle():
# 	while(len(partial_deck) > 0):


create_deck()
partial_deck = list(full_deck)

for i in range(0, len(full_deck)):
 	print("Card: ", full_deck[i].value)

# test_card = draw_card(partial_deck)
# print("you drew", test_card.value)