import random

# Using slices with lists
spam = ['cat', 'bat', 'rat', 'elephant']


print(spam)
print(spam[0:2]) #Prints indeces 0 through 1

# Using slices with strings
word = "Hello"
print(word)
print(word[0:2])

# Tuple unpacking
cat = ['fat', 'gray', 'loud']
size, color, disposition = cat
print(color)

# Using the enumerate function to iterate through a list
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies): #enumerate returns and index an value
    print('Index ' + str(index) + ' in supplies is: ' + item)

# Select a random element from a list
pets = ['Dog', 'Cat', 'Moose']
print(random.choice(pets))

# Sorting a list
animals = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
animals.sort(reverse=True) # Reverse list
print(animals)



