#!/usr/bin/env python2.7 
# -*- coding: utf-8 -*-
import random
import string
import sys

if(len(sys.argv) != 2):
	print('TAILLE DU MDP PAR DEFAUT')
	taille = 9
else:
	try:
		taille = int(sys.argv[1])
		print "Taille du mdp : " + str(taille)
	except:
		taille = 9
		print("ERREUR LORS DE LA CONVERSION")
		print('TAILLE DU MDP PAR DEFAUT')

def Generer(t):
	password = ""
	letter = list(string.ascii_lowercase)
	LETTER = list(string.ascii_uppercase)
	number = list(string.digits)
	while(len(password) < t):
		random_choice = random.randint(1,3)
		if(random_choice == 1):
			letter_random = random.choice(letter)
		elif(random_choice == 2):
			letter_random = random.choice(LETTER)
		else:
			letter_random = random.choice(number)
		password += letter_random
	print(password)
Generer(taille)
