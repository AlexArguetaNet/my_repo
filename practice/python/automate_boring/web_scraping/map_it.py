#! python3

# map_it.py - Launches a map in the browser using an address from
#             the command line or clipboard

import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    # Get address from the command line
    address = ' '.join(sys.argv[1:])
    print(sys.argv)
    print(address)
else:
    # Get address from clipboard
    address = pyperclip.paste()

if (len(address) > 0):
    # Open google maps with address parameter
    webbrowser.open('https://www.google.com/maps/place/' + address)
else:
    print('No address was given')


