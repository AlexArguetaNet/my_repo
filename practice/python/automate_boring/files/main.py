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


