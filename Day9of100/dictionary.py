#! /usr/bin/python3

# Python convention for writing the dictionary data type, it is almost like the list.
programming_dictionary = {
    "Bug": "An error in a piece of code.",
    "Function": "Piece of code performing a specific task.",
    "Loop": "To repeat a task by a specified number of time.",
}

# Retrieves a dictionary value using its key.
print(programming_dictionary["Bug"])

# We could as well add items to dictionary.
programming_dictionary["Test"] = "Adding item to a dictionary"
print(programming_dictionary)

# Just like list, we could create a set of empty dict so as to add items later on.
empty_dictionary = {}
print(empty_dictionary) 

# One can edit the value of a key in a dictionary
programming_dictionary["Test"] = "I can edit the value of a dictionary key"
print(programming_dictionary)

# We can aswell retrieva a dictionary key and value using a loop
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Nesting in python dictionary
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a list in a dictionary
travel_log = {
    "France": ["Paris", "Dijon", "Lille"],
    "Germany": ["Berlin", "Hamburg", "Struttgart",]
}

# Nesting dictionary in dictionary
travel_log_exp = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },

    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Struttgart"],
        "total_visits": 23
    },
}

# Nesting a dictionary inside a list
# NOTE that list is accessed by it index while dictionary by its keys
travel_log_list = [
    {
        "Country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "Country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Struttgart"],
        "total_visits": 23
    },
]
