import turtle

class Seven_segments:
    def __init__(self, color, my_turtle):
        self.color = color
        self.my_turtle = my_turtle
        self.delay_in_seconds = 0.2

    def draw(self, digit):
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)

        self.my_turtle.color(color)
        self.my_turtle.penup()
        self.my_turtle.setheading(0)
        self.my_turtle.goto(0, 0)
        self.my_turtle.pensize(10)

        if digit == 0:
            self.my_turtle.goto(-50, 100)
            self.my_turtle.pendown()
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.penup()

        if digit == 1:
            self.my_turtle.goto(50, 100)
            self.my_turtle.pendown()
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.penup()

        if digit == 2:
            self.my_turtle.goto(-50, 100)
            self.my_turtle.pendown()
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.forward(100)
            self.my_turtle.penup()

        if digit == 3:
            self.my_turtle.goto(-50, 100)
            self.my_turtle.pendown()
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.forward(-100)
            self.my_turtle.left(90)
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.left(90)
            self.my_turtle.penup()

        if digit == 4:
            self.my_turtle.goto(-50, 100)
            self.my_turtle.pendown()
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.forward(100)
            self.my_turtle.forward(-100)
            self.my_turtle.forward(-100)
            self.my_turtle.right(90)
            self.my_turtle.penup()

        if digit == 5:
            self.my_turtle.goto(-50, 100)
            self.my_turtle.pendown()
            self.my_turtle.forward(100)
            self.my_turtle.forward(-100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.left(90)
            self.my_turtle.penup()

        if digit == 6:
            Seven_segments.draw(self,5)
            self.my_turtle.goto(-50, 0)
            self.my_turtle.pendown()
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.penup()

        if digit == 7:
            self.my_turtle.goto(-50, 100)
            self.my_turtle.pendown()
            self.my_turtle.forward(100)
            self.my_turtle.forward(-100)
            Seven_segments.draw(self, 1)

        if digit == 8:
            Seven_segments.draw(self, 0)
            self.my_turtle.goto(-50, 0)
            self.my_turtle.pendown()
            self.my_turtle.forward(100)
            self.my_turtle.penup()

        if digit == 9:
            Seven_segments.draw(self, 5)
            self.my_turtle.goto(50, 100)
            self.my_turtle.pendown()
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.penup()

    def clear(self):
        self.my_turtle.clear()

    def my_delay(self, dt):
        import time
        start = time.time()
        while time.time() - start < dt:
            pass

    def run(self):
        while True:
            for i in range(0, 10):
                Tom.clear()
                Tom.draw(i)
                Tom.my_delay(self.delay_in_seconds)
                turtle.update()

color = (255, 0, 0)
Tom = Seven_segments(color, turtle)
Tom.my_turtle.Turtle()
Tom.run()



