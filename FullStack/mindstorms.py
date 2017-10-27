import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("blue")
#First turtle: square  
    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("black")
    counter = 0;
    
    while (counter < 4):
     brad.forward(100)
     brad.right(90)
     counter = counter + 1

    
#second turtle: circle
    angie = turtle.Turtle()
    angie.shape("classic")
    angie.color("red")
    angie.circle(100)
        
       
    window.exitonclick()
draw_square()
