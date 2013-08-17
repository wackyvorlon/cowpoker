#!/usr/bin/env python

#CowPoker - released under current GPL by PVA.
# Game wherein one assaults a cow.

from colorama import init
init()

from colorama import Fore, Back, Style
import random
print(Fore.RED + 'Welcome to CowPoker! ')
print(Fore.GREEN + '\tThe only game where you assault a cow!')
random.seed()

print(Fore.WHITE+'\n\nYou are standing in an open field.\nBefore you stands a generic cow.\n')
x=1 

def cowpoke():
	#Step 1: Did we succeed in poking the cow?
	#random.seed() 
	poked = random.randrange(0,10)
	print poked
	if poked<=4:
		print('The cow mooed!')
	else:
	    print('The cow glances over at you, then returns to chewing his cud.')
	    print('He briefly wonders if you have nothing better to do.')


while x:
	cmd = raw_input(Fore.GREEN +'Do you want to poke the cow? (y/n) '+Fore.WHITE)
	if cmd =='y':
		print('Poked!')
		cowpoke()
	elif cmd == 'n':
		print('Why not?')
	elif cmd == 'x':
		quit()






