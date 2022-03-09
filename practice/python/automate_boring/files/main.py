from pathlib import Path
import os

print("Current path", Path.cwd())

# Creates a new directory
# os.makedirs('C:\\walnut\\waffles')

# Creates and writes to a file named spam.txt using the Path module
p = Path('spam.txt')
p.write_text('Hello there')

# Reads froma file using the Path module
print(p.read_text())


# Using file object to perform I/O operations

baconFile = open('practice\\python\\automate_boring\\files\\bacon.txt', 'w') # Writing to file
baconFile.write('Hello bacon!')
baconFile.write('Bacon is not a vegtable.')

baconFile.close()

baconFile = open('practice\\python\\automate_boring\\files\\bacon.txt')
content = baconFile.read() # Reading from a file

baconFile.close()

print(content)





