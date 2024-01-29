import random

# # Set the seed for reproducibility
# random.seed(42)

# # Get the current state of the random number generator
# state_before = random.getstate()

# # Generate some random numbers
# random_number_1 = random.random()
# random_number_2 = random.random()

# print("Before setting state:")
# print(random_number_1)
# print(random_number_2)
# print(state_before)

# # Change the internal state (for demonstration purposes)
# no = random.setstate(state_before)

# # Generate random numbers again using the restored state
# random_number_3 = random.random()
# random_number_4 = random.random()

# print("\nAfter setting state:")
# print(random_number_3)
# print(random_number_4)
# print(no)


# random_int = random.randint(1, 10)
# print(random_int)

# # 0.000000 - 0.999999
# random_float = random.random()
# print(random_float)


# m = random.uniform(0, 5)
# print(m)


# states_of_nigeria = ['Lagos', 'Ogun', 'Abuja]',
#                      'Osun', 'Oyo', 'Kastina',
#                      'Kano', 'Edo', 'Kogi',
#                      'Abia', 'Delta', 'Enugu']
# print(states_of_nigeria[-1])

# states_of_nigeria[1] = "Kebbi" # Indexing of list.
# print(states_of_nigeria[1])
# states_of_nigeria.append("Lady Bug") # Add to the list by adding the new argument as the last element of the list.
# states_of_nigeria.extend(['Goose land', 'Chicken Bug', 'Ass wipe']) # Extends the list. 
# states_of_nigeria.pop(2) # Takes one argument(int) or no argument. 
# states_of_nigeria.remove('Chicken Bug') # Take one argument (string)
# print(states_of_nigeria)

# states_of_nigeria.append("Lady")
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])