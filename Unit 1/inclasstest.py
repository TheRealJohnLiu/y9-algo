import turtle

win_width, win_height, bg_color = 2000, 2000, 'yellow'

turtle.setup()
turtle.screensize(win_width, win_height, bg_color)
 
t = turtle.Turtle()
t.fillcolor('blue')
t.begin_fill()
for i in range(4):
  t.forward(150)
  t.right(90)
t.end_fill()

turtle.done()