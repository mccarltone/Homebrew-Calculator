# Detects user OS and uses proper command to clear terminal screen
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Print program name and options
print "Homebrew Calc\n"

# Defines user options
def print_options():
    print "Options:"
    print " '1' print options"
    print " '2' convert Brix to SG"
    print " '3' convert SG to Brix"
    print " '4' find ABV using OG and FG"
    print " 'q' quit the program"

# Define formula to convert Brix to Standard Gravity
def brix_to_sg(brix):
	return (brix / (258.6-((brix / 258.2)*227.1))) + 1

# Define formula to convert Standarg Gravity to Brix
def sg_to_brix(sg):
	return ((182.4601 * sg - 775.6821) * sg + 1262.7794) * sg - 669.5622

# Define formula to calculate ABV%
def findABV(og , fg):
	return (og - fg) * 131.25
	
# Print user options
choice = "1"
while choice != "q":

# Choice '2' convert Brix to SG
	if choice == "2":
		while True:
			try:
				brix = float(raw_input("Please input the wort Brix: "))
				break
			except ValueError:
				print "Please enter a number."
		print "SG = ", brix_to_sg(brix)
		choice = raw_input("Option: ")

# Choice '3' convert SG to Brix
	elif choice == "3":
		while True:
			try:
				sg = float(raw_input("Please input the wort SG: "))
				break
			except ValueError:
				print "Please enter a number."
		print "Brix = ", sg_to_brix(sg)
		choice = raw_input("Option:")

# Choice '4' find ABV using OG and FG
	elif choice == "4":
		while True:
			try:
				og = float(raw_input("Please input the OG: "))
				break
			except ValueError:
				print "Please enter a number."
		while True:
			try:
				fg = float(raw_input("Please input the FG: "))
				break
			except ValueError:
				print "Please enter a number."
		print "ABV% = ", findABV(og , fg)
		choice = raw_input("Option: ")

	else:
		choice = "1"
		print_options()
		choice = raw_input("Option: ")
	
