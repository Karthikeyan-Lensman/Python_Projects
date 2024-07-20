# NANDHA ENGINEERING COLLEGE LOGO 
# created by N.KARTHIKEYAN (20.07.2024)
import turtle as t
t.speed(5)  # 0->Fastest 1->Slowest
t.pensize(4)
t.color('blue')

t.fd(170)
t.left(30)
t.fd(100)
t.left(60)
t.fd(100)
t.left(60)
t.fd(100)
t.left(30)
t.fd(170)
t.left(30)
t.fd(100)
t.left(60)
t.fd(100)
t.left(60)
t.fd(100)
t.penup()
t.backward(100)
t.right(60)
t.backward(30)
t.pendown()
t.left(90)
t.fd(344)
t.left(90)
t.penup()
t.fd(40)
t.left(90)
t.pendown()
t.fd(344)
t.penup()
t.left(90)
t.fd(40)
t.left(90)
t.fd(30)
t.right(90)
t.fd(8)
t.left(90)
t.pendown()
t.begin_fill()
t.fd(284)
t.right(145)
t.fd(70)
t.right(35)
t.fd(170)
t.right(35)
t.fd(70)
t.end_fill()
t.penup()
t.pencolor('white')
t.right(145)
t.fd(28)
t.right(90)
t.fd(5)
t.left(90)
t.pendown()
t.fd(28)
t.right(90)
t.fd(24)
t.left(90)
t.fd(34)
t.left(90)
t.fd(24)
t.right(90)
t.fd(34)
t.right(90)
t.fd(24)
t.left(90)
t.fd(34)
t.left(90)
t.fd(24)
t.right(90)
t.fd(34)
t.right(90)
t.fd(24)
t.left(90)
t.fd(34)
t.left(90)
t.fd(24)
t.right(90)
t.fd(28)

t.pencolor('blue')
#text
t.penup()
t.left(90)
t.fd(20)
t.left(90)
t.fd(278)
t.left(90)
t.write("NANDHA ENGINEERING COLLEGE",font=('Arial',15,'bold'))
t.fd(84)
t.left(90)
t.fd(129)
t.pendown()
t.write("SERVE",font=('Arial',16,'bold'))
t.penup()
t.left(90)
t.fd(120)
t.right(90)
t.fd(30)

t.left(33)
t.speed(10)
t.fd(15)
t.pendown()


#Eagle
t.fillcolor("#0000FF")
t.begin_fill()
t.fd(38)
t.right(240)
t.fd(20)
t.left(29)
t.fd(29)
t.left(29)
t.fd(20)
t.right(240)
t.fd(38)

t.end_fill()
t.penup()
t.right(180)
t.fd(30)
t.left(40)
t.fd(25)
t.left(217)

#wings
t.pendown()
t.pencolor('blue')
t.speed(30)

t.circle(3, 180)  
t.fd(24)  
t.right(50)
t.fd(9)  
t.right(130)
t.fd(24)  

#2
t.circle(3, 180)  
t.fd(30)  
t.right(50)
t.fd(9)  
t.right(130)
t.fd(30)  

#3
t.circle(3, 180)  
t.fd(36)  
t.right(50)
t.fd(9) 
t.right(130)
t.fd(36)  

#4
t.circle(3, 180)  
t.fd(42)  
t.right(50)
t.fd(9) 
t.right(130)
t.fd(42)  

#5
t.circle(3, 180)  
t.fd(48)  
t.right(50)
t.fd(9)  
t.right(130)
t.fd(70)  

#
t.right(360)
t.circle(-25.5, 80)  
t.fd(40)  
t.right(100)
t.fd(12)  
t.left(92)
t.fd(40)  
t.right(138)
t.fd(50)  
t.right(132)
t.fd(19)  


t.penup()

t.right(50)
t.fd(100)
t.right(229)
t.pendown()


# Mirrored wing

#1

t.circle(-3, 180)  
t.fd(24)  
t.left(50)
t.fd(9)  
t.left(130)
t.fd(24)  

#2
t.circle(-3, 180) 
t.fd(30)  
t.left(50)
t.fd(9)  
t.left(130)
t.fd(30)  

#3
t.circle(-3, 180)  
t.fd(36)  
t.left(50)
t.fd(9)  
t.left(130)
t.fd(36) 

#4
t.circle(-3, 180)
t.fd(42)  
t.left(50)
t.fd(9)  
t.left(130)
t.fd(42)  

#5
t.circle(-3, 180)  
t.fd(48)  
t.left(50)
t.fd(9)  
t.left(130)
t.fd(70)  

# Additional
t.left(360)
t.circle(25.5, 80)  
t.fd(40)  
t.left(100)
t.fd(12)  
t.right(92)
t.fd(40)  
t.left(138)
t.fd(50)  
t.left(132)
t.fd(19)

t.penup()
t.left(60)
t.fd(80)
t.right(90)
t.fd(25)
t.color('red')
t.right(85)
t.fd(5)
t.right(90)
t.fd(17)
t.left(90)

#NEC

t.pencolor('white')
t.write("NEC",font=('Arial',17,'bold'))
t.penup()
t.right(90)
t.fd(28)
t.right(122)

t.backward(10)
t.left(30)
t.fd(5)
t.right(30)


t.right(75)
t.fd(60)
t.right(90)

t.pendown()
t.pencolor('blue')
t.pensize(2)
t.fd(20)
t.left(105)
t.fd(4)
t.circle(22.6, 35)
t.circle(9, 110)
t.right(50)
t.circle(9, 40)
t.right(252)
t.circle(-10, 66)

t.penup()
t.left(140)
t.fd(10)

t.pendown()
t.circle(0.4, -360)
t.begin_fill()
t.circle(1.2, 360)
t.end_fill()
t.penup()
t.fd(20)

t.right(180)
t.fd(290)
t.right(90)
t.fd(60)
t.right(90)
t.fd(100)
t.right(95)
t.pendown()

# LEARN
def scale_length(length):
    return length / 8
t.pensize(3)

# L
t.right(90)
t.forward(scale_length(100))
t.left(90)
t.forward(scale_length(50))

t.penup()
t.fd(scale_length(30))
t.pendown()

# E
t.left(90)
t.forward(scale_length(100))
t.right(90)
t.forward(scale_length(50))
t.backward(scale_length(50))
t.right(90)
t.forward(scale_length(50))
t.left(90)
t.forward(scale_length(40))
t.backward(scale_length(40))
t.right(90)
t.forward(scale_length(50))
t.left(90)
t.forward(scale_length(50))

t.penup()
t.fd(scale_length(30))
t.pendown()

# A
t.left(70)
t.forward(scale_length(110))
t.right(140)
t.forward(scale_length(110))
t.right(180)
t.forward(scale_length(35))
t.left(70)
t.forward(scale_length(50))

t.penup()
t.left(180)
t.fd(scale_length(50))
t.right(70)
t.fd(scale_length(35))
t.left(70)
t.fd(scale_length(30))
t.pendown()

# R
t.left(90)
t.forward(scale_length(100))
t.right(90)
t.forward(scale_length(35))
t.circle(-scale_length(25), 180)
t.forward(scale_length(35))
t.left(135)
t.forward(scale_length(70))

t.penup()
t.right(-135)
t.right(90)
t.fd(scale_length(40))
t.pendown()

# N
t.left(90)
t.forward(scale_length(100))
t.right(145)
t.forward(scale_length(120))
t.left(145)
t.forward(scale_length(100))

t.penup()
t.right(55)
t.fd(185)
t.right(93)
t.fd(10)
t.left(90)
t.left(37)

t.pendown()

# succeed
def scale_length(length):
    return length / 12
t.right(80)
t.fd(1)

# S
t.circle(scale_length(45),60)
t.circle(scale_length(45), 200)  
t.right(180)
t.circle(scale_length(45), -200) 
t.circle(scale_length(45),-60)

t.penup()
t.right(100)
t.fd(scale_length(60))
t.right(90)
t.pendown()

# U
t.fd(8)
t.circle(scale_length(50),180)
t.fd(8)

t.penup()
t.right(90)
t.fd(scale_length(140))
t.right(180)

# C

t.pendown()
t.circle(scale_length(80),180)
t.penup()

t.left(90)
t.fd(scale_length(160))
t.right(180)
t.left(90)
t.fd(scale_length(120))
t.left(180)
t.pendown()


# C
t.circle(scale_length(80),180)


t.penup()
t.left(90)
t.fd(scale_length(160))
t.right(180)
t.left(90)
t.fd(scale_length(60))
t.left(270)
t.fd(scale_length(160))
t.right(270)

# E
t.left(90)
t.forward(scale_length(160))
t.right(90)
t.pendown()

t.forward(scale_length(80))
t.backward(scale_length(80))
t.right(90)
t.forward(scale_length(80))
t.left(90)
t.forward(scale_length(64))
t.backward(scale_length(64))
t.right(90)
t.forward(scale_length(80))
t.left(90)
t.forward(scale_length(80))

t.penup()
t.fd(scale_length(60))
t.right(270)
t.fd(scale_length(160))
t.right(90)
t.pendown()

# E
t.forward(scale_length(80))
t.backward(scale_length(80))
t.right(90)
t.forward(scale_length(80))
t.left(90)
t.forward(scale_length(64))
t.backward(scale_length(64))
t.right(90)
t.forward(scale_length(80))
t.left(90)
t.forward(scale_length(80))


t.penup()
t.fd(scale_length(60))
t.pendown()


# Draw D
t.left(90)
t.forward(scale_length(160)) 
t.right(80)

t.fd(scale_length(16))
t.backward(scale_length(32))
t.penup()
t.fd(scale_length(32))
t.pendown()
t.circle(-scale_length(90), 190)
t.fd(scale_length(48))


t.hideturtle()
t.exitonclick()

