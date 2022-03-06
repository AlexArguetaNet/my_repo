import pprint

# Dictionaries (hash table) uses key-value pairs instead
# of indeces to location values inside this
# data structure

birthdays = {'Alice': 'April 1', 'Bob': 'Dec 12', \
                'Carol': 'March 4'}

# Prompts to look update datum in the hash table
# while True:

#     print('Enter a name: (blank to quit)')
#     name = input()

#     if name == '':
#         break
        
#     if name in birthdays:
#          print(birthdays[name] + ' is the birthday of ' + name)
#     else:
#          print('I do not have birthday information for ' + name)
#          print('What is their birthday?')

#          bday = input()

#          birthdays[name] = bday

#          print('Birthday database updated')



# Using hash table functions

# Loop over keys
for i in birthdays:
    print(i)

# Loop over value
for i in birthdays:
    print(birthdays[i])

# Loop over keys and values
for i, j in birthdays.items():
    print(i, j)


# Checking if a key or value exists in a hash table
spam = {'name': 'Zophie', 'age': 7}
print('name' in spam.keys())
print('Zophie' in spam.values())

# Using the get() method to retreive an element
# get() takes two arguments: the key and a value
# to return if the key is not found
picnincItems = {'apples': 5, 'cups': 2}

print('I am bringing ' + str(picnincItems.get('cups', 0)) + ' cups')

# Using setDefault() to add a new value to the
# hash table
spam = {'name': 'Pooka', 'age': 5}

spam.setdefault('color', 'black')
print(spam.get('color', 0))


# Using pprint() to print a formatted
# key-value pair
pprint.pprint(spam)

# Represnting a tic-tac-toe board using a hash table
# [O][O][O]
# [X][X][ ]
# [ ][ ][X]
board = {'topL': 'O', 'topM': 'O', 'topR': 'O',
         'midL': 'X', 'midM': 'X', 'midR': ' ',
         'lowL': ' ', 'lowM': ' ', 'lowR': 'X'}





