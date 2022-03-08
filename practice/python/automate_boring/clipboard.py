#! python3

# This is a python script. THis means this program is
# is meant to run in a terminal where commandline arguments
# can be used. Running the program itself outside of a terminal
# will throw an error.

import pyperclip
import sys

# Adding 'Hello World' to the computer clipboard
# pyperclip.copy('Hello World')
# pyperclip.paste()

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

# sys.argv is a list of commandline arguments
# the name of the .py file is always index 0
if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] # First commandline argument


if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard')
else:
    print('There is no text for ' + keyphrase)

