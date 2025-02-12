# Importing necessary libraries
import sys  # provides access to system-specific parameters and functions
import time  # Allows for time-related functions like delays 

# ANSI escape sequences for color
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"  # Resets color back to default

# Adding color to the initial welcome messages
print(f"\n{CYAN}Welcome Branch - Developer: Corbin Hanson{RESET}")

print(f"\n{GREEN}Welcome to InfoTech Center V1.0{RESET}\n")

x = 0
ellipsis = 0

# Loop to simulate a system booting animation
while x != 20:
    x += 1  # increment counter

    # Creates loading message with increasing dots
    message = f"{YELLOW}Infotech Center System Booting{RESET}" + "." * ellipsis  

    ellipsis += 1  # Increase ellipsis count

    # Overwrites the current line in the terminal
    sys.stdout.write("\r" + message)

    time.sleep(.5)  # pause for half a second to have an effect

    # Reset ellipsis after reaching 3 dots to loop back
    if ellipsis == 4:
        ellipsis = 0

# When the loop completes, it has a final message
if x == 20:
    print(f"\n\n{RED}Operating System Booted Up - Retina Scanned - Access Granted{RESET}")
