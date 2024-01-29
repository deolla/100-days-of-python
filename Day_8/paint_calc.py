import math


def paint_calc(height, width, cover):
    """This function calculates how many cans of paint needed to paint a wall"""
    num_of_can = height * width / cover
    # n = math.ceil(num_of_can)
    print(f"You'll need {round(num_of_can)} cans of paint.")


test_h = int(input())
test_w = int(input())
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
