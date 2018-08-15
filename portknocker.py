from socket import *
import subprocess
import time
import itertools
import os
from core import functions
from termcolor import colored # needed for colored print

def main():
	functions.banner()
	print colored("\nPlease Select 1 Of The Following Options\n", 'yellow',attrs=['bold'])
	print("1. Summary Mode (Display Summary of Nmap Scan")
	print("2. Verbose Mode (Run Nmap in Verbose Mode)")
	print("3. Exit\n")
	mode = functions.user_input_integer(3)
	if mode == 3:
		exit(0)
	else:
		# Ask the user for the Target IP Address
		print colored("Please Enter The Target IP",'yellow')
		target_ip = raw_input("Target IP: ")
		
		# Ask the user for the port sequence
		print colored("\nPlease Enter The Target Ports Seperated By a Space i.e. 1234 5678",'yellow')
		ports = raw_input("Enter Ports:")
		ports = ports.split()
		
		print colored("\nPlease Enter The Number of Tries to Attempt a Given Sequence i.e.",'yellow')
		attempts = raw_input("Number of Attempts: ")
		
		all_combinations = list(itertools.permutations(ports)) # create list with all possible permutations of those sequences
		
		for combo in all_combinations:
			Knockports(combo,target_ip,mode, attempts)
			
			# create result file
			result = ''
			for port in combo:
				result = result + port + "_" 
			parse_result = "results/" + result[:-1] + ".txt"
			nmap_result = "core/results/" + result[:-1] + ".txt"
			
			if mode == 2:
				subprocess.Popen("nmap -n -v -Pn -p- -A --reason " + str(target_ip) + " -oG " + nmap_result  , shell=True).wait() 	# scan ports to see if any are new
			else:
				subprocess.call("nmap -n -v -Pn -p- -A --reason " + str(target_ip) + " -oG " + nmap_result, shell=True, stdout=open(os.devnull, 'w'), stderr=subprocess.STDOUT) 	# scan ports to see if any are new 	# scan ports to see if any are new
			
			temp = subprocess.check_output("cd core && ./nmap_parser.sh -f " + parse_result + " -i " + target_ip, shell=True)				# parse the results to check for new ports
			results = temp.splitlines()
			display_results(results)
		
def Knockports(ports, target_ip, mode, attempts):
	try:
		print colored("\n[*] Knocking with sequence:",'yellow'),
		print colored(ports,'yellow'),
		print colored("...",'yellow',attrs=['bold'])
		
		i=0
		while i < int(attempts):
			for port in ports:
				if mode == 2:
					os.system("nmap -n -v0 -Pn --max-retries 0 -p " + port + " " + target_ip)
				else:
					subprocess.call("nmap -n -v0 -Pn --max-retries 0 -p " + port + " " + target_ip, shell=True, stdout=open(os.devnull, 'w'), stderr=subprocess.STDOUT)
				print colored("[+] Knock Sent: ",'yellow'),
				print colored(port,'yellow')
			i+=1
			time.sleep(2)
	except Exception as e:
		print colored("[!!] Something Unexpected Occured",'red',attrs=['bold'])
		print e
		
def display_results(results):
	for element in results:
		if "open" in element:
			print colored(element,'cyan')
		elif "filtered" in element:
			print colored(element,'red')
		else:
			print element

main()
