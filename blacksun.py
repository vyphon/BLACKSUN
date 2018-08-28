# WORK IN PROGRESS
import socket
try: # <- to determine which httplib to use for Python version.
	import http.client 
except ImportError:
	import httplib
import sys
try: # <- to determine which urllib2 to use for Python version.
	import urllib2
except ImportError:
	import urllib.error
	import urllib.request
import urllib
import os
import base64
import subprocess
import random
import time

#-------------------------------------------------------------------------------------------------#

blackSun_CLIPrompt = "root@blacksun:~# "

terms = '''
I agree and confirm that I will NOT use BLACKSUN to:
(i) upload/transmit, display/distribute any
content that infringes any trademark, trade secret, copyright
or other proprietary or intellectual property rights of any
person; (ii) upload or otherwise transmit any material that contains
software viruses or any other computer code, files or programs
designed to interrupt, destroy or limit the functionality of any
computer software or hardware or telecommunications equipment;
'''

def yesOrNO():
	try:
		return (raw_input("Continue [Y/n]: ") in 'y', 'Y')
	except NameError:
		return (input("Continue [Y/n]: ") in 'y', 'Y')

def ClearScreen():
	os.system('clear')

def agreementPrompt():
	ClearScreen()
	print(terms)
	try:
		agreeToTerms = raw_input("Do you agree to the Terms? [Y/n]: ")
	except NameError:
		agreeToTerms = input("Do you agree to the Terms? [Y/n]: ")
	if 'y' in agreeToTerms or 'Y' in agreeToTerms:
		pass
	else:
		agreementPrompt()


class main_BlackSun:
	def __init__(self):
		ClearScreen()
		blackSunPrompt()
		session = 1
		while session == 1:
			try:
				choice = raw_input(blackSun_CLIPrompt)
			except NameError:
				choice = input(blackSun_CLIPrompt)
			if choice == "1":
				# vulnerabilityAnalysisMenu()
				pass
			elif choice == "2":
				# WAPP_Menu()
				pass
			elif choice == "3":
				# privateHackingMenu()
				pass
			elif choice == "4":
				# bruteForceMenu()
				pass
			elif choice == "5":
				# SE_Menu()
				pass
			elif choice == "6":
				# postExploitationMenu()
				pass
			elif choice == "7":
				# passwordAttacksMenu()
				pass
			elif choice == "8":
				# wirelessHackingMenu()
				pass
			elif choice == "9":
				# sniffingSpoofingMenu()
				pass
			elif choice == "10":
				self.credMenu()
			else:
				main_BlackSun()

	def credMenu(self):
		ClearScreen()
		print('''            ______________________________________________________
           _/  ____/__  __ \\__  ____/__  __ \\___  _/__  __/_  ___/
          _/ /    __  /_/ /_  __/  __  / / /__  / __  /  _____ \\ 
         _/ /___  _  _, _/_  /___  _  /_/ /__/ /  _  /   ____/ / 
          \\____/  /_/ |_| /_____/  /_____/ /___/  /_/    /____/
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	                 <|--------------------|>
 	                 <|-[ Coded By : NET ]-|>
 	                 <|-[ That's it...   ]-|>
	                 <|--------------------|>

 > [ 1 ]: Main Menu
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -''')	
		try:
			choice = raw_input(blackSun_CLIPrompt)
		except NameError:
			choice = input(blackSun_CLIPrompt)
		if choice == "1":
			main_BlackSun()
		else:
			self.credMenu()
			

def blackSunPrompt():
	print('''            ________________________________ _____________  ______   __
           _/ __ )__  /___    |_  ____/__  //_/_  ___/_  / / /__  | / /
          _/ __  |_  / __  /| |  /    __  ,<  _____ \_  / / /__   |/ / 
         _/ /_/ /_  /___  ___ / /___  _  /| | ____/ // /_/ / _  /|  /  
        _/_____/ /_____/_/  |_\____/  /_/ |_| /____/ \____/  /_/ |_/   
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
 > [ 1 ]:  Vulnerability Analysis
 > [ 2 ]:  Web Application Analysis
 > [ 3 ]:  Private Web Hacking
 > [ 4 ]:  Brute Force Attacks
 > [ 5 ]:  Social Engineering Attacks
 > [ 6 ]:  Post Exploitation
 > [ 7 ]:  Password Attacks
 > [ 8 ]:  Wireless Hacking
 > [ 9 ]:  Sniffing & Spoofing
 > [ 10 ]: Credits and Mentions
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -''')

if __name__ == "__main__":
	try:
		agreementPrompt()
		main_BlackSun()
	except KeyboardInterrupt:
		print("\nExiting...")
		time.sleep(0.01)
		ClearScreen()
		os.system('exit')
