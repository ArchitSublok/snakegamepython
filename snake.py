from turtle import *
STARTING=[(0,0),(-20,0),(-40,0)]
MOVE=20
LEFT=[-1,0]
RIGHT=[1,0]
UP=[0,-1]
DOWN=[0,1]

class Snake:
    def __init__(self):
        self.segments=[]
        # self.create_snake()

    def create_snake(self):
        for position in STARTING:
            new_seg=Turtle()
            new_seg.color("white")
            new_seg.shape("square")
            new_seg.penup()
            new_seg.goto(position)
            self.segments.append(new_seg)

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(MOVE)

    def heading(self):
        head=self.segments[0].heading()
        print(head)

    def up(self):
        head=self.segments[0].heading()
        if head!=270:    
            self.segments[0].setheading(90)

    def right(self):
        head=self.segments[0].heading()
        if head!=180:
            self.segments[0].setheading(0)

    def left(self):
        head=self.segments[0].heading()
        if head!=0:
            self.segments[0].setheading(180)

    def down(self):
        head=self.segments[0].heading()
        if head!=90:
            self.segments[0].setheading(270)