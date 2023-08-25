import turtle

t = turtle.Turtle()
sc = turtle.Screen()

length = int(input("Insert your length here: "))
angle = int(input("Now insert you angle: "))

if length > 100:
    t.penup()
    t.goto(-200, -200)
    t.pendown()

t.shape('turtle')
sc.bgcolor("black")
t.pencolor('green')
t.width(6)
t.forward(length)
t.left(90)

t.forward(length)
t.backward(length)
t.right(90)

t.left(angle)
t.forward(length)
t.left(90 - angle)

t.forward(length)
t.backward(length)

t.left(90)
t.forward(length)


t.right(90)
t.forward(length)
t.backward(length)


t.left(90 + angle)
t.forward(length)
t.right(90 + angle)
t.forward(length)

t.right(90)
t.forward(length)


t.left(angle)
t.forward(length)
t.left(90 - angle)

t.left(90)
t.forward(length)

t.left(angle)
t.forward(length)

#ssss

#bh
turtle.done()

