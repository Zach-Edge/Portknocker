from termcolor import colored # needed for colored print
import os



############# System Functions #############

# Print the Banner
def banner():
	print colored("""\
$$\   $$\ $$\   $$\  $$$$$$\   $$$$$$\  $$\   $$\       $$\   $$\ $$\   $$\  $$$$$$\   $$$$$$\  $$\   $$\ 
$$ | $$  |$$$\  $$ |$$  __$$\ $$  __$$\ $$ | $$  |      $$ | $$  |$$$\  $$ |$$  __$$\ $$  __$$\ $$ | $$  |
$$ |$$  / $$$$\ $$ |$$ /  $$ |$$ /  \__|$$ |$$  /       $$ |$$  / $$$$\ $$ |$$ /  $$ |$$ /  \__|$$ |$$  / 
$$$$$  /  $$ $$\$$ |$$ |  $$ |$$ |      $$$$$  /        $$$$$  /  $$ $$\$$ |$$ |  $$ |$$ |      $$$$$  /  
$$  $$<   $$ \$$$$ |$$ |  $$ |$$ |      $$  $$<         $$  $$<   $$ \$$$$ |$$ |  $$ |$$ |      $$  $$<   
$$ |\$$\  $$ |\$$$ |$$ |  $$ |$$ |  $$\ $$ |\$$\        $$ |\$$\  $$ |\$$$ |$$ |  $$ |$$ |  $$\ $$ |\$$\  
$$ | \$$\ $$ | \$$ | $$$$$$  |\$$$$$$  |$$ | \$$\       $$ | \$$\ $$ | \$$ | $$$$$$  |\$$$$$$  |$$ | \$$\ 
\__|  \__|\__|  \__| \______/  \______/ \__|  \__|      \__|  \__|\__|  \__| \______/  \______/ \__|  \__|
""",'red')
	print colored("				Automated Port Knocking Tool",'white')
	print colored("				Designed For Kali Linux",'white')              
	print colored("				https://github.com/zflemingg1",'white')



# Function to clear the screen
def system_clear():
	os.system("clear")
	return


# Function to choose a number between n-n1 and perform error checking
def user_input_integer(num_range):
	
	while True:
    		try:  
				userInput = int(raw_input('\nPlease Enter Choice [' + repr(1) + '-' + repr(num_range) + ']: '))       
    		except ValueError:
       			print("Not an integer! Try again.")
       			continue
       		except KeyboardInterrupt:
				raise
    		else:
       			if(userInput < 1 or userInput > num_range ):
				print("Error Please Select A Valid Number")
			else:
				return userInput 
       				break
