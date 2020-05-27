import turtle, random

w=turtle.Screen()
w.bgcolor("black")



def starFILL(n, dlina):
  joe.begin_fill()
  if n %2!=0:
    for i in range (n):
      joe.forward(dlina)
      angle=n//2*360/n
      joe.left(angle)
  joe.end_fill()

joe=turtle.Turtle()
joe.color('yellow')
for i in range (15):
  x=random.randint(-320,320)
  y=random.randint(-220,220)
  joe.up()
  joe.setposition(x,y)
  joe.down()
  starFILL(3,100)
