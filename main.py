import turtle

myScreen = turtle.getscreen()

myTurtle = turtle.Turtle()




def drawDottedLine():
  myTurtle.forward(40)
  myTurtle.penup()
  myTurtle.forward(40)
  myTurtle.pendown()
  myTurtle.forward(40)
  myTurtle.penup()
  myTurtle.forward(40)
  myTurtle.pendown()

drawDottedLine()
