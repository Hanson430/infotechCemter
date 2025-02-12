#Importing necesary libraries
import sys # provides access to system-specific parameters and functions
import time # Allows for time-related functions like delays 


print("\nWelcome Branch - Developer: Corbin Hanson")

print("\nWelcome to InfoTech Center V1.0\n")

x = 0
ellipsis = 0
 
# loop to simulate a system booting animation
while x != 20:
    x += 1 # increment counter

    message = ("Infotech Center System Booting" + "." * ellipsis)  # Creates loading message with increasing dots

    ellipsis += 1 # Increase ellipsis count

    sys.stdout.write("\r" + message)  # Overwrites the current line in the terminal

    time.sleep(.5) # pause for half a secong to have a efffect
# Reset ellipsis after reaching 3 dots to loop back
    if ellipsis == 4:
        ellipsis = 0
# WHen the loop completes it has a final message
    if x == 20:
        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted")