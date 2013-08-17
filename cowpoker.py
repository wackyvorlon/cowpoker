#!/usr/bin/env python

#CowPoker - released under current GPL by PVA.
# Game wherein one assaults a cow.

from colorama import init
init()

from colorama import Fore, Back, Style
print(Fore.RED + 'Welcome to CowPoker! ')
print(Fore.GREEN + '\tThe only game where you assault a cow!')

print(Fore.WHITE+'\n\nYou are standing in an open field.\nBefore you stands a generic cow.\n')
x=1 

while x:
	cmd = raw_input(Fore.GREEN +'Do you want to poke the cow? (y/n) '+Fore.WHITE)
	if cmd =='y':
		print('Poked!')
	elif cmd == 'n':
		print('Why not?')
	elif cmd == 'x':
		quit()



