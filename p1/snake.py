from turtle import Turtle

start_posi = [(0,0), (-20,0), (-40,0)]
move_dis = 20
UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270

class Snake:
    def __init__(self):
        self.seg = []
        self.create_snake()
        
    def create_snake(self):
        for i in start_posi:
            self.extend(i)
            
    def extend(self, i):
        seg_1 = Turtle("square")
        seg_1.color("white")
        seg_1.penup()
        seg_1.goto(i)
        self.seg.append(seg_1)
    
    def get_long(self):
        self.extend(self.seg[-1].position())
    
    def move(self):
        for seg_num in range(len(self.seg)-1,0,-1):
            new_x = self.seg[seg_num - 1].xcor()
            new_y = self.seg[seg_num - 1].ycor()
            self.seg[seg_num].goto(new_x,new_y)
        self.seg[0].forward(move_dis)   
        
    def left(self):
        if self.seg[0].heading() != RIGHT:
            self.seg[0].setheading(LEFT)
            
    def up(self):
        if self.seg[0].heading() != DOWN:
            self.seg[0].setheading(UP)
        
    def right(self):
        if self.seg[0].heading() != LEFT:
            self.seg[0].setheading(RIGHT)
        
    def down(self):
        if self.seg[0].heading() != UP:
            self.seg[0].setheading(DOWN)
        