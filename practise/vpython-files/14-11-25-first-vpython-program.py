from vpython import *
from numpy import *

ball1 = sphere(pos=vector(0,0,0), radius=1, color=color.green)
ball2 = sphere(pos=vector(-3,4,0), radius=1, color=color.red)
pointer = arrow(pos=vector(0,0,0), axis =  ball2.pos, color=color.blue)

position = vector(-3,4,0)
ball2.pos = position

starting_point = position.x
end_point = starting_point + 10

velocity = 1

while True:
    rate(10)

    position.x += velocity * 0.5
    ball2.pos = position

    pointer.axis = ball2.pos - ball1.pos

    if position.x >= end_point:
        velocity = -1
    elif position.x <= starting_point:
        velocity = 1