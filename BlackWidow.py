#Libraries HERE
import sys
import time

from google.protobuf.internal.test_bad_identifiers_pb2 import message

print("Welcome Branch - Developer: Corbin Hanson")

print("\n\tWelcome to InfoTech Center V1.0")

x = 0
ellipsis = 0

while x != 20:
    x += 1
    message = ("Infotech Center System Booting" + "." * ellipsis)
    ellipsis += 1
    sys.stdout.write("\r" + message)
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\nOperating System Booted Up - Retina Scanned - Access Granted")