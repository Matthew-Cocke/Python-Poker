from card import *
import numpy as np

class deck:

	def __init__(self):
		# This program generates its deck of cards using an array of integers, there are 52 cards in a deck, so num_array is declared as [1:52]
		# the range(a, b) funciton return [a : b-1], which is why there is a plus 1
		cards_in_standard_deck = 52
		self.num_array = range(1, cards_in_standard_deck + 1)
		self.card_array = self.generate_card_array()



	def shuffle_num_array(self):
		# this funciton shuffles the array of integers that is used to generate the deck of cards
		shuffled_array = np.random.permutation(self.num_array)
		self.num_array = shuffled_array



	def get_deck_length(self):
		return len(self.card_array)



	def is_empty(self):
		# returns if the deck is empty, used to stop program from dealing a card from an empty deck without an error.
		if self.get_deck_length() == 0:
			return True
		else:
			return False



	def shuffle_deck(self):
		# this function shuffles the deck, by first shuffling the num array, and then generating a new 52 card deck based off that shuffled array
		print("shuffling the deck")
		self.shuffle_num_array()
		self.card_array = self.generate_card_array()



	def generate_card_array(self):
		# this function shuffles the deck, by first shuffling the num array, and then generating a new 52 card deck based off that shuffled array
		array_of_cards = []

		for i in range(len(self.num_array)):
			array_of_cards.append(card(self.num_array[i]))

		return array_of_cards



	def deal_card(self):
		# rempoves a card from the end of the deck, and returns that card. if the deck is empty it returns None
		if self.is_empty():
			print("Error: Deck has no more cards, cant deal another card!")
			return None
		else:
			dealt_card = self.card_array.pop()
			return dealt_card



	def print_deck(self):
		# prints every card in the deck in order that they appear.
		for i in range(len(self.card_array)):
			self.card_array[i].print_card_as_string()



	def print_num_array(self):
		# prints the number array that is used to generate the card objects
		for i in range(len(self.num_array)):
			print(self.num_array[i])
