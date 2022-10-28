#! /usr/bin/python3

# Functions with outputs

def format_name(f_name, l_name):
    format_n = f_name.title() + " " + l_name.title()
    print(f"{format_n}")

# format_name("mujor", "bright")

# Functions returning an output and using docstring in functions
def format_name(f_name, l_name):
    """
    Takes in a string of f_name representing first name and l_name representing last name in any format and returns a clean title format of both f_name and l_name.
    """
    format_n = f_name.title() + " " + l_name.title()
    return format_n

formatted_names = format_name("mujor", "bright")
print(formatted_names)
