from turtle import *
reset()
speed(0)
color("red", "yellow")
pensize(3)
begin_fill()

for i in range(5):
  fd(150)
  for j in range(5):
    fd(50)
    left(144)
  left(144)
end_fill()