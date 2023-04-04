from turtle import *
speed(8)
for i in range(3, 0, -1):
    if i == 1:
        color('black', 'white')
        begin_fill()
    elif i == 2:
        color('black', 'red')
        begin_fill()
    elif i == 3:
        color('black', 'green')
        begin_fill()
    forward(150)
    right(90)
    forward(50*i)
    right(90)
    forward(150)
    right(90)
    forward(50*i)
    right(90)
    end_fill()
done()
