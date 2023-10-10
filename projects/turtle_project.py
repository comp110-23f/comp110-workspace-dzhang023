"""Tree drawing simulator."""

__author__ = "730630816"

from turtle import *
from random import randint, randrange


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


def draw_top_tree():
    """Draws the top of the tree."""
    color("green")
    fillcolor("green")
    begin_fill()
    setheading(0)
    circle(50)
    end_fill()
    color("sienna")


def draw_tree(branch_cnt: int, starting_location: int) -> None:
    """Draws the trunk and then runs a loop to draw a randomized number of branches on the trunk."""
    branch_index: int = 0
    trunk_length: int = randint(300, 400)
    trunk_increment: float = trunk_length / branch_cnt
    draw_trunk(trunk_length, starting_location)
    while branch_index != branch_cnt:
        branch_angle: int = randint(25, 60)
        setheading(90)
        forward(trunk_increment)
        if branch_index == branch_cnt - 1:
            draw_top_tree()
        else:
            if branch_index % 2 == 0:
                right(branch_angle)
            else:
                left(branch_angle)
            draw_branch(starting_location, ycor())
        branch_index += 1


def draw_plaid_box(block_color: str, girth: int, box_length):
    fillcolor(block_color)
    begin_fill()
    setheading(0)
    forward(girth / 2)
    setheading(90)
    forward(box_length)
    setheading(180)
    forward(girth / 2)
    return_x = xcor()
    return_y = ycor()
    forward(girth / 2)
    setheading(270)
    forward(box_length)
    setheading(0)
    forward(girth / 2)
    end_fill()
    penup()
    setpos(return_x, return_y)
    pendown()


def draw_neck_and_head(neck_len: int, head_rad: int):
    color('black')
    setheading(90)
    forward(neck_len)
    setheading(0)
    circle(head_rad)


def draw_axe(length: int, holding_angle: int):
    fillcolor('red')
    begin_fill()
    axe_width: int = randint(15, 30)
    breadth = axe_width * 2 / 3
    setheading(holding_angle)
    backward(length / 3)
    forward(length)
    setheading(holding_angle - 90)
    forward(axe_width)
    setheading(holding_angle)
    forward(breadth)
    setheading(holding_angle - 90)
    backward(axe_width)
    setheading(holding_angle)
    backward(breadth)
    end_fill()


def draw_arms(arm_len: int, axe_len: int, torso_size: int):
    color("black")
    arm_angle: int = randint(-75, 0)
    return_pos_x = xcor()
    return_pos_y = ycor()
    penup()
    setheading(0)
    forward(torso_size / 2)
    setheading(arm_angle)
    pendown()
    forward(arm_len)
    draw_axe(axe_len, arm_angle + 90)
    penup()
    setpos(return_pos_x, return_pos_y)
    setheading(180)
    forward(torso_size / 2)
    pendown()
    setheading(180 - arm_angle)
    forward(arm_len)
    penup()
    setpos(return_pos_x, return_pos_y)
    pendown()


def draw_lumberjack():
    """Draws a randomly sized lumberjack."""
    penup()
    color("black")
    setpos(-300, -200)
    number_of_plaid_boxes: int = randrange(5, 11, 2)
    leg_length: int = randint(50, 100)
    arm_length: int = randint(35, 75)
    torso_length: int = randint(75, 150)
    torso_girth: int = randint(25, 50)
    torso_increment_size: float = torso_length / number_of_plaid_boxes
    axe_length: int = randint(75, 150)
    neck_length: int = randint(10, 25)
    head_size: int = randint(15, 35)
    pendown()
    setheading(60)
    forward(leg_length)
    leg_base_x: int = xcor()
    leg_base_y: int = ycor()
    setheading(-60)
    forward(leg_length)
    setpos(leg_base_x, leg_base_y)
    setheading(90)
    index: int = 0
    while index != number_of_plaid_boxes:
        if index == number_of_plaid_boxes - 1:
            draw_arms(arm_length, axe_length, torso_girth)
        if index % 2 == 1:
            draw_plaid_box("red", torso_girth, torso_increment_size)
        else:
            draw_plaid_box("black", torso_girth, torso_increment_size)
        index += 1
    draw_neck_and_head(neck_length, head_size)


def main(tree_count: int) -> None:
    """Calls the tree drawing function."""
    index = 0
    while index != tree_count:
        if index == 0:
            draw_lumberjack()
        else:
            branches = randint(5, 10)
            draw_tree(branches, 100 * index - 200)
        index += 1
    done()


if __name__ == "__main__":
    tree_cnt = randint(3, 6)
    main(tree_cnt)
