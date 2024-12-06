import turtle
import random
import ball
import seven_segments_proc

class Simulator:
    def __init__(self, num_balls):
        self.radius = 0.05 * self.c_width
        self.xpos = []
        self.ypos = []
        self.vx = []
        self.vy = []
        self.ball_color = []
        self.num_balls = 5
        self.dt = 0.2
        self.c_width = turtle.screensize()[0]
        self.c_height = turtle.screensize()[1]
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)

    def draw_border(self):
        turtle.penup()
        turtle.goto(-self.c_width, -self.c_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2 * self.c_width)
            turtle.left(90)
            turtle.forward(2 * self.c_height)
            turtle.left(90)

    def draw_ball(self):
        for i in range(self.num_balls):
            self.xpos.append(random.uniform(-1 * self.c_width + self.radius, self.c_width - self.radius))
            self.ypos.append(random.uniform(-1 * self.c_height + self.radius, self.c_height - self.radius))
            self.vx.append(10 * random.uniform(-1.0, 1.0))
            self.vy.append(10 * random.uniform(-1.0, 1.0))
            self.ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    def run(self):
        while (True):
            turtle.clear()
            Simulator.draw_border(self)
            for i in range(self.num_balls):
                ball.draw_ball(self.ball_color[i], self.ball_radius, self.xpos[i], self.ypos[i])
                ball.move_ball(i, self.xpos, self.ypos, self.vx, self.vy, self.dt)
                ball.update_ball_velocity(i, self.xpos, self.ypos, self.vx, self.vy, self.canvas_width, self.canvas_height, self.ball_radius)
            turtle.update()

    def __str__(self):
        return f"{self.c_width}, {self.c_height}"

num_balls = 5
a = Simulator(num_balls)
a.run()