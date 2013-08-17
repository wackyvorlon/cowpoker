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
aggravation=0

f=open("nouns.txt",'r')

words=f.readlines()

def cowpoke():
	#Step 1: Did we succeed in poking the cow?
	#random.seed()
	global moos
	global coins 
	global words
	global aggravation
	poked = random.randrange(0,10)
	#print poked
	if poked<=4:
		print(Fore.RED+'The cow mooed!'+Fore.WHITE)
		moos=moos+1
	else:
	    print('\nThe cow glances over at you,\nthen returns to chewing his cud and contemplating {noun}.').format(noun=random.choice(words).rstrip())
	    print('\nHe briefly wonders if you have nothing better to do.')
	    aggravation=aggravation+1
	    if aggravation>10:
	    	print("\nNow you've done it!")
	    	print(Fore.RED+'The cow looks at you, then charges, flattening you on top\nof a large pile of manure.'+Fore.WHITE)
	    	if coins>0:
	    		print('You dropped your coins, now the cow is standing on them!')
	    		coins=0
	if moos>5:
		print('\nThe cow gives an unamused stare,\nand promptly coughs up a coin.')
		print(Fore.BLUE+"\nIt's a golden Roman aureus of the Julio-Claudians,\nminted in 8 BC!"+Fore.WHITE)
		if coins==0:
			print('\nSomeone has been using this cow to smuggle antiquities!')
		print('\nI wonder if he has more?')
		moos=0
		coins=coins+1

def feed():
	#Handles feeding the cow.
	global aggravation
	if aggravation>0:
		aggravation=aggravation-1
		print(Fore.CYAN+"\nHe's starting to calm down now.")

while x:
	if coins!=0:
		print(Style.DIM+'\nYou have '+str(coins)+' coins!'+Style.RESET_ALL)
	if aggravation!=0:
		print(Style.DIM+Fore.RED+'\nThe cow has an aggravation level of '+str(aggravation)+'! Be careful!'+Style.RESET_ALL)
	cmd = raw_input(Fore.GREEN +'Do you want to poke or feed the cow? (p/f) '+Fore.WHITE)
	if cmd =='p':
		print('Poked!')
		cowpoke()
	elif cmd == 'f':
		print('You give the cow a hand-full of hay.\nHe grunts approvingly then drools on your hand.')
		feed()
	elif cmd == 'x':
		x=0

print('\nYay! You collected '+str(coins)+' coins! Go buy a coke!')






