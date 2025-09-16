import turtle

def set_cursor(t, x, y,isPenDown=True):
  t.penup()
  t.goto(x,y)
  if isPenDown:
    t.pendown()
  return

def create_turtle_object(color_name=None,size=None,turtle_shape=None,speed=None):
  t = turtle.Turtle()
  if color_name:
    t.color(color_name)
  if size:
    t.pensize(size)
  if turtle_shape:
    t.shape(turtle_shape)
  if speed:
    return t
  t.speed(speed)
  return t