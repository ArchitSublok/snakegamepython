from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.penup()
        # x_cor=random.randint(-400,400)
        # y_cor=random.randint(-400,400)
        # self.goto(x_cor,y_cor)
        self.refresh()

    def refresh(self):
        x_cor=random.randint(-380,380)
        y_cor=random.randint(-380,380)
        self.goto(x_cor,y_cor)
