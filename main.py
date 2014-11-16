#!/usr/bin/env python2.7 
# -*- coding: utf-8 -*-
import random
import string

def Generer():
	password = ""
	letter = list(string.ascii_lowercase)
	LETTER = list(string.ascii_uppercase)
	number = list(string.digits)
	while(len(password) < 9):
		random_choice = random.randint(1,3)
		if(random_choice == 1):
			letter_random = random.choice(letter)
		elif(random_choice == 2):
			letter_random = random.choice(LETTER)
		else:
			letter_random = random.choice(number)
		password += letter_random
	print(password)
Generer()
