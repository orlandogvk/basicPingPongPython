import turtle



# Window
wn = turtle.Screen()
wn.cv._rootwindow.resizable(False, False)
wn.title("Pong by Orlando")
wn.bgcolor("black")
wn.setup(width=800, height=600, startx = None, starty = None)
wn.tracer(0)


# Score
A_score=0
B_score=0

# Player A
playerA= turtle.Turtle()
playerA.speed(0)
playerA.shape("square")
playerA.color("white")
playerA.penup()
playerA.goto(-350,0)
playerA.shapesize(stretch_wid=5, stretch_len=1)

# Player B
playerB= turtle.Turtle()
playerB.speed(0)
playerB.shape("square")
playerB.color("white")
playerB.penup()
playerB.goto(350,0)
playerB.shapesize(stretch_wid=5, stretch_len=1)

# Ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = .5
ball.dy = .5

# Middle line
divline=turtle.Turtle()
divline.color("white")
divline.goto(0,400)
divline.goto(0,-400)


# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)

# board score
pen.write("PlayerA: 0        PlayerB: 0", align="center", font=("courier", 24 , "normal"))


# Motions using functions

def playerA_up():
    if playerA.ycor() < 241:
        y = playerA.ycor()
        y +=20
        playerA.sety(y)

def playerA_down():    
    if playerA.ycor() > -241:
        y = playerA.ycor()
        y -=20
        playerA.sety(y)

def playerB_up():
    if playerB.ycor() < 241:
        y = playerB.ycor()
        y +=20
        playerB.sety(y)

def playerB_down():
    if playerB.ycor() > -241:
        y = playerB.ycor()
        y -=20
        playerB.sety(y)

# keyboard controls
wn.listen()
wn.onkeypress(playerA_up, "w")
wn.onkeypress(playerA_down, "s")
wn.onkeypress(playerB_up, "Up")
wn.onkeypress(playerB_down, "Down")
    


while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # edges up/down
    if ball.ycor() > 290:
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.dy *= -1

    # edges right/left
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        A_score += 1
        pen.clear()
        pen.write("PlayerA: {}        PlayerB: {}".format(A_score,B_score), align="center", font=("courier", 24 , "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        B_score += 1 
        pen.clear()   
        pen.write("PlayerA: {}        PlayerB: {}".format(A_score,B_score), align="center", font=("courier", 24 , "normal"))


    # racket collitions
    if ((ball.xcor() > 340 and ball.xcor() < 350)
            and (ball.ycor() < playerB.ycor() + 50)
            and ball.ycor() > playerB.ycor() -50):
        ball.dx *=-1
    
    if ((ball.xcor() < -340 and ball.xcor() > -350)
            and (ball.ycor() < playerA.ycor() + 50)
            and ball.ycor() > playerA.ycor() -50):
        ball.dx *=-1
        

input("Press any key to exit ...")