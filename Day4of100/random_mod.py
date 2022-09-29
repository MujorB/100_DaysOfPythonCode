#! /usr/bin/python3

import random
import my_module

"""
This randint function from the random module help produce a random whole number from and including the parameters given. randint(a, b)
"""
random_integer = random.randint(1, 10)
print(random_integer)

"""
We can create a module ourselves and use in another just like the one used above.
spoiler alert, the random module used above is owned by the python team.
We are going to use a variable gotten from another module to be printed in this current module
"""
print(my_module.PI)


"""
Another function up the random module sleeves is the random(), which helps print random floating point values between 0.0 - 1.0 and not including 1.0, the function takes in no argument's'.
"""
random_float = random.random()
print(random_float)

"""
------------ A quick task create a random floating point value between 0 nd 5 ----------
using what we've learned above.
"""
rand_int = random.randint(0, 4)
random_float = random.random()
random_num = rand_int + random_float
print(random_num)
