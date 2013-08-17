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

moos=0
coins=0

def cowpoke():
	#Step 1: Did we succeed in poking the cow?
	#random.seed()
	global moos
	global coins 
	poked = random.randrange(0,10)
	print poked
	if poked<=4:
		print('The cow mooed!')
		moos=moos+1
	else:
	    print('The cow glances over at you, then returns to chewing his cud.')
	    print('He briefly wonders if you have nothing better to do.')
	if moos>5:
		print('The cow gives an unamused stare,\nand promptly coughs up a coin.')
		print(Fore.BLUE+"It's a golden Roman aureus of the Julio-Claudians,\nminted in 8 BC!"+Fore.WHITE)
		if coins==0:
			print('Someone has been using this cow to smuggle antiquities!')
		print('I wonder if he has more?')
		coins=coins+1


while x:
	cmd = raw_input(Fore.GREEN +'Do you want to poke the cow? (y/n) '+Fore.WHITE)
	if cmd =='y':
		print('Poked!')
		cowpoke()
	elif cmd == 'n':
		print('Why not?')
	elif cmd == 'x':
		quit()






