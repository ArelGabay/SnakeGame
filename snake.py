from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_snake(position)

    def add_snake(self, position):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.snake_body.append(snake)

    def extend(self):
        self.add_snake(self.snake_body[-1].position())

    def move(self):
        for snake_index in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[snake_index - 1].xcor()
            new_y = self.snake_body[snake_index - 1].ycor()
            self.snake_body[snake_index].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for snake in self.snake_body:
            snake.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]