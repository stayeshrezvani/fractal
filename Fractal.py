


import turtle,random,time
color=["blueviolet","darkslateblue","darkolivegreen","deeppink","darkred","darkslategray","deepskyblue"]
class Fractal:
    def __init__(self):
        print("WELCOME!")
    def MyFractal(self):
        repetition=(int(input("*ENTER THE NUMBER OF REPETITIONS*:")))
        sides=(int(input("*ENTER NUMBER OF SIDES*:")))
        length=(int(input("*ENTER THE SIDE SIZE*:")))
        MyPen=turtle.Pen()
        MyPen.speed(10)
        time1=time.time()
        for i in range(repetition):
            randomcolor=random.choice(color)           
            for k in range(sides):                
                 MyPen.pencolor(randomcolor)
                 MyPen.forward(length)
                 MyPen.left(360/sides)
            MyPen.left(10)
        time2=time.time()
        MyTime=time2-time1
        print("PERFORMANCE TIME IS %s SECOND:"%MyTime)

MyShape=Fractal()
MyShape.MyFractal()
        
    