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

def yes_no():
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
		while True:
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
				# informationGatheringMenu()
				pass
			elif choice == "11":
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
			self.__init__()
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
 > [ 10 ]: Information Gathering
 > [ 11 ]: Credits and Mentions
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -''')








def informationGatheringPrompt():
	print('''       __________   _________________ 
       /_  _/__  | / /__  ____/_  __ \
        / / __   |/ /__  /_   _  / / /
      _/ /  _  /|  / _  __/   / /_/ / 
     /___/  /_/ |_/  /_/      \\____/  
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
 > [ 1 ]: Get Site Headers
 > [ 2 ]: Ping
 > [ 3 ]: Port Scan
 > [ 4 ]: DNS Lookup
 > [ 5 ]: Reverse DNS 
 > [ 6 ]: Host to IP
 > [ 7 ]: NMAP
 > [ 8 ]: XSStrike
 > [ 9 ]: SEToolkit
 > [ 10 ]: WPScan
 > [ 11 ]: Main Menu
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -''')








class informationGatheringMenu():
	def __init__(self):
		try:
			choice = raw_input(blackSun_CLIPrompt)
		except NameError:
			choice = input(blackSun_CLIPrompt)
		if choice == "1":
			sendHEAD()
		elif choice == "2":
			
		elif choice == "3":
			pass
		elif choice == "4":
			pass
		elif choice == "5":
			pass
		elif choice == "6":
			pass
		elif choice == "7":
			pass
		elif choice == "8":
			pass
		elif choice == "9":
			pass
		elif choice == "10":
			pass
		elif choice == "11":
			pass
		else:
			self.__init__()






def ping(): # using system-installed ping because I am lazy and don't feel like making my own with socket ¯\_(ツ)_/¯
	ClearScreen()
	try:
		host_IP = raw_input("Enter the IP Address to ping: ")
	except NameError:
		host_IP = input("Enter the IP Address to ping: ")
	try:
		indefinitePing = raw_input("Would you like to ping indefinitely? [Y/n]: ")
	except NameError:
		indefinitePing = input("Would you like to ping indefinitely? [Y/n]: ")
	if "y" in indefinitePing or "y" in indefinitePing:
		os.system('ping {} -4 -t'.format(host_IP))
	else:
		os.system('ping {} -4'.format(host_IP))



def sendHEAD():
	ClearScreen()
	try:
		host_IP = raw_input("Enter the IP Address of the domain to send the HEAD request: ")
	except NameError:
		host_IP = input("Enter the IP Address of the domain to send the HEAD request: ")
	ClearScreen()
	os.system('curl {} -I'.format(host_IP))



if __name__ == "__main__":
	try:
		agreementPrompt()
		main_BlackSun()
	except KeyboardInterrupt:
		print("\nExiting...")
		time.sleep(0.01)
		ClearScreen()
		os.system('exit')
