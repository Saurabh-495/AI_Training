from numpy import random

# Generate Random Number :- NumPy offers the random module to work with random numbers.
x = random.randint(1000) #Generate a random integer from 0 to 1000:
print(x)


# Generate Random Float :- The random module's rand() method returns a random float between 0 and 1.

y = random.rand()
print(y)
# Generate Random Array :- You can generate a random array using the numpy.random.rand() function.

# Generate Random Array :- In NumPy we work with arrays, and you can use the two methods from the above examples to make random arrays.

z=random.randint(100, size=(5)) #Generate a 1-D array containing 5 random integers from 0 to 100: 
print(z)


arr2=random.randint(100, size=(3,3)) #Generate a 2-D array with 3 rows containing 5 random integers from 0 to 100: 
print("The array is : ", arr2 )

# we can use random.rand method for float 

#Generate Random Number From Array

# The choice() method allows you to generate a random value based on an array of values.
# The choice() method takes an array as a parameter and randomly returns one of the values.

choice = random.choice([3, 5, 7, 9])

print(choice)
