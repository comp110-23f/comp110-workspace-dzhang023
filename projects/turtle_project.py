"""Tree drawing simulator."""

__author__ = "730630816"

from turtle import *
from random import randint


def draw_leaf():
    """Draws a randomly sized leaf at a random angle on the branch."""
    leaf_angle = randint(30, 150)
    leaf_width = randint(5, 10)
    setheading(leaf_angle)
    color("green")
    fillcolor("green")
    begin_fill()
    circle(leaf_width)
    end_fill()
    color("sienna")


def draw_trunk(length: int, start_location: int):
    """Draws the base of the tree at a set width and position."""
    penup()
    color("sienna")
    setpos(start_location, -200)
    pensize(15)
    pendown()
    setheading(90)
    forward(length)
    setpos(start_location, -200)


def draw_branch(start_location: int, start_y: int):
    """Draws a branch of the tree and returns the pen back to the trunk."""
    color("sienna")
    branch_width = randint(5, 10)
    pensize(branch_width)
    branch_length = randint(50, 100)
    forward(branch_length)
    draw_leaf()
    penup()
    goto(start_location, start_y)
    pendown()


def draw_tree(branch_cnt: int, starting_location: int) -> None:
    """Draws the trunk and then runs a loop to draw a randomized number of branches on the trunk."""
    branch_index = 0
    trunk_length = randint(300, 400)
    trunk_increment = trunk_length / branch_cnt
    draw_trunk(trunk_length, starting_location)
    while branch_index != branch_cnt:
        branch_angle = randint(25, 60)
        setheading(90)
        forward(trunk_increment)
        if branch_index % 2 == 0:
            right(branch_angle)
        else:
            left(branch_angle)
        draw_branch(starting_location, ycor())
        branch_index += 1


def main(tree_cnt) -> None:
    """Calls the tree drawing function."""
    index = 0
    while index != tree_cnt:
        branches = randint(5, 10)
        draw_tree(branches, 100 * (index) - 200)
        index += 1
    done()


if __name__ == "__main__":
    tree_cnt = randint(3, 6)
    main(tree_cnt)
