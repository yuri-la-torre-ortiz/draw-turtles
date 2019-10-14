import turtle

def draw_big_square(some_turtle):
    for i in range(4):
        some_turtle.forward(200)
        some_turtle.right(90)

def draw_small_square(some_turtle):
    for i in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_shape():
    window = turtle.Screen()
    window.bgcolor("pink")
    #Create the turtle Brad - Draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.speed(10)
    for i in range(3):
        brad.color("blue", "brown")
        for i in range(36):
            draw_big_square(brad)
            brad.right(10)
        brad.right(5)
        brad.color("yellow", "brown")
        for i in range(36):
            draw_small_square(brad)
            brad.right(10)

    #malika = turtle.Turtle()
    #malika.shape("circle")
    #malika.color("white", "yellow")
    #malika.circle(100)

    #charmaine = turtle.Turtle()
    #charmaine.shape("circle")
    #charmaine.color("green", "yellow")
    #charmaine.speed(5)

    #charmaine.forward(100)
    #charmaine.left(60)
    #charmaine.forward(100)
    #charmaine.home()

    window.exitonclick()

draw_shape()
