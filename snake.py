import turtle as t

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            snake_segment = t.Turtle(shape="square")
            snake_segment.penup()
            snake_segment.color("white")
            snake_segment.speed(1)
            snake_segment.setposition(position)
            self.segments.append(snake_segment)

    def get_tail(self):
        snake_segment = t.Turtle(shape="square")
        snake_segment.penup()
        snake_segment.color("white")
        snake_segment.speed(1)
        # print(self.segments[len(self.segments)-1].position())
        snake_segment.setposition(self.segments[-1].position())
        self.segments.append(snake_segment)

    def move(self):

        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].xcor(), self.segments[seg_num - 1].ycor())
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() == 0 or self.segments[0].heading() == 180:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() == 0 or self.segments[0].heading() == 180:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() == 90 or self.segments[0].heading() == 270:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() == 90 or self.segments[0].heading() == 270:
            self.segments[0].setheading(0)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
