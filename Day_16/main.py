# This is a blueprint for creating objects. In this case, the object
# This blueprint contains the color of the car, milage, the year of the car etc.
# which as it functionlity which is the ability to start, stop, drive, honk etc.
# This blueprint is known as the class and  objects are created from this class.
""" blueprint = CAR 
    - attributes: color, model, year
    - methods: start, stop, honk
"""
from turtle import Turtle, Screen

# sloppy = Turtle()
# print(sloppy)
# sloppy.shape("turtle")
# sloppy.color("coral")
# sloppy.forward(100)
# sloppy.goto(100, 100)


# just_screen = Screen()
# print(just_screen.canvheight)
# just_screen.exitonclick()

from prettytable import PrettyTable


table = PrettyTable()
# table.add_column("No", ["1", "2", "3"])
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)

print(table.get_string(border=True, padding_width=5))
