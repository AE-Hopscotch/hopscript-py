from builder import *
from json import dumps


# Define your custom abilities below.
# They will be accessible everywhere else in your code by their function's name

def change_color(times):
    with repeat(times):
        set_color(Color.random())


