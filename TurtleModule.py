import random
import turtle
from turtle import Turtle as t, Screen

my_turtle = t()

# this list holds the colors of each shape
colors = (
	'#2C838D', '#8748D5', '#6FDF48', '#D3A7A5', '#215EBF', '#59E599', '#6514D0', '#BBDBD5'
)


# ================Common method for closing the turtle screen
def close_screen():
	"""it closed the turtle screen when clicked the close button"""""
	screen = Screen()
	screen.exitonclick()


# this is for random_walk()
def rgb_color_picker():
	"""this function picks a random RGB color, and its used by random_walk() method"""
	turtle.colormode(255)
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	rgb = (r, g, b)
	return rgb


# ============= for Random Walk function
default_steps = 200
direction = [0, 90, 180, 270]  # angles to move


# this is for draw_shape()
def draw(angle):
	""" It draws the required shape based the angle based to it, and its used by draw_shape() method"""
	my_turtle.color(random.choice(colors))
	for _ in range(angle):
		my_turtle.forward(100)
		my_turtle.left(360 / angle)


def draw_shapes():
	"""The main function of the project which determine all the drawing in one go"""
	for sides in range(10, 2, -1):
		# my_turtle.begin_fill()
		draw(sides)
	# my_turtle.end_fill()

	# Everything to be above this line
	close_screen()


def random_walk():
	"""Rando function for making the turtle to move random directions"""
	my_turtle.speed("fastest")  # setting the speed of the turtle
	my_turtle.pensize(15)  # changing the size of the drawing pen
	# turtle.colormode(255)

	for _ in range(default_steps):  # this describes how many moves to make
		# my_turtle.color(rgb)
		my_turtle.pencolor(rgb_color_picker())
		my_turtle.setheading(random.choice(direction))
		my_turtle.forward(20)

	# Everything to be above this line
	close_screen()


def draw_circle():
	"""it draws a circle based giving radius, but currently its using 100 as deafuly"""
	my_turtle.speed("fastest")
	my_turtle.color(rgb_color_picker())
	my_turtle.circle(100)


def draw_spirograph(gap_size):
	for _ in range(int(360 / gap_size)):
		# my_turtle.begin_fill()
		draw_circle()
		# my_turtle.end_fill()
		my_turtle.setheading(my_turtle.heading() + gap_size)

	close_screen()
