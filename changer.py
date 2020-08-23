from colorama import Fore, Back, Style, init
import os
init(autoreset=True)
workning = True
while workning:
	os.system('cls')
	print(Fore.YELLOW + 'Hello from P.M.C console v1.0...(Press any key)')
	input()
	os.system('cls')
	command = input('MacAChanger>')
	if(command == 'exit'):
		workning = False
	if(command == 'clear'):
		os.system('cls')
	if(command == 'start macchange'):
		print('The P.M.C Macchanger...')
		interface = input(Fore.YELLOW + 'Enter your interface:')
		print(Fore.YELLOW + 'Your interface ' + interface)
		MAC_ADDR = input(Fore.YELLOW + 'Enter your new mac:')
		print(Fore.YELLOW + 'Your MAC address ' + MAC_ADDR)
		os.system('ifconfig ' + interface + ' hw' + ' ether ' + MAC_ADDR)
		os.system('ifconfig ' + interface + ' up')
		close()	