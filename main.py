import turtle
import time
import winsound


score1=0
score2=0
close= True


paddle2 = turtle.Turtle()
ball = turtle.Turtle()


wm=turtle.Screen()
wm.title("Multiplayer-Pong (By Pradeep)")
wm.bgcolor("black")
wm.setup(width=800,height=600)
wm.tracer(0)

fscore= wm.textinput("Welcome to Pong!", "Enter winning score-")

try:
    fscore = int(fscore)
except:
    p= wm.textinput("Invalid input!","Press any key to exit and try again")
    if(p):
        exit(0)

paddle1 = turtle.Turtle()  
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid=5,stretch_len=1)
paddle1.penup()
paddle1.goto(-375,0)

paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(stretch_wid=5,stretch_len=1)
paddle2.penup()
paddle2.goto(375,0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx= 0.3
ball.dy=0.3
    

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("PONG", align='center',font=("Courier", 30, "bold"))
pen.goto(0,225)
pen.write("Player A: 0       Player B: 0", align='center',font=("Courier", 15, "normal"))

def paddle1_up():
    y= paddle1.ycor()
    y+=20
    paddle1.sety(y)

def paddle2_up():
    y= paddle2.ycor()
    y+=20
    paddle2.sety(y)

def paddle1_down():
    y= paddle1.ycor()
    y-=20
    paddle1.sety(y)

def paddle2_down():
    y= paddle2.ycor()
    y-=20
    paddle2.sety(y)

wm.listen()
wm.onkeypress(paddle1_up,'w')
wm.onkeypress(paddle2_up,'Up')
wm.onkeypress(paddle1_down,'s')
wm.onkeypress(paddle2_down,'Down')

if __name__ == "__main__":
    while True:
        wm.update()

        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        
        if(ball.ycor()>290):
            ball.sety(290)
            ball.dy*=-1
            winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

        if(ball.ycor()<(-290)):
            ball.sety(-290)
            ball.dy*=-1
            winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
            
        if(ball.xcor() >390):
            ball.goto(0,0)
            time.sleep(0.1)
            ball.dx*=-1
            pen.goto(0,250)
            score1+=1
            pen.clear()
            pen.goto(0,250)
            pen.write("PONG", align='center',font=("Courier", 30, "bold"))
            pen.goto(0,225)
            pen.write("Player A: {}       Player B: {}".format(score1,score2), align='center',font=("Courier", 15, "normal"))
            
        if(ball.xcor() <-390):
            ball.goto(0,0)
            time.sleep(0.1)
            ball.dx*=-1
            score2+=1
            pen.clear()
            pen.goto(0,250)
            pen.write("PONG", align='center',font=("Courier", 30, "bold"))
            pen.goto(0,225)
            pen.write("Player A: {}       Player B: {}".format(score1,score2), align='center',font=("Courier", 15, "normal"))

        if((ball.xcor() < -355 and ball.xcor()>-365) and (ball.ycor() < paddle1.ycor()+50 and ball.ycor() > paddle1.ycor()-50)):
            ball.dx *=-1
            winsound.PlaySound("paddle.wav",winsound.SND_ASYNC)
            
        if((ball.xcor() > 355 and ball.xcor()< 365) and (ball.ycor() < paddle2.ycor()+50 and ball.ycor() > paddle2.ycor()-50)):
            ball.dx *=-1
            winsound.PlaySound("paddle.wav",winsound.SND_ASYNC)
            

        if(score1==fscore or score2==fscore):
            if(close):
                turtle.clearscreen()
                wm=turtle.Screen()
                wm.title("Multiplayer-Pong (By Pradeep)")
                wm.bgcolor("black")
                wm.setup(width=800,height=600)
                wm.tracer(0)
            pen.goto(0,0)
            pen.write("GAME OVER", align='center',font=("Courier", 60, "bold"))
            pen.goto(0,-100)
            winner = "A" if score1 > score2 else "B"
            pen.write("Player {} wins!".format(winner), align='center',font=("Courier", 30, "normal"))

            close = False

turtle.done()