#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_first_part_of_name(name):
	name = name.capitalize()
	nom = name.split('-')
	return "Bonjour " + nom[0]

def get_random_sentence(animals, adjectives, fruits):
	animaux = list(animals)
	adjectifs = list(adjectives)
	fruitss = list(fruits)


	return "Aujourd'hui, j'ai vu un " + random.choice(animaux) + ' s\'emparer d\'un panier ' + random.choice(adjectifs) + ' plein de ' + random.choice(fruitss) + '.'

def encrypt(text, shift):
	text
	return ""

def decrypt(encrypted_text, shift):
	return ""


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))
	
	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
