import turtle

def draw_square(my_turtle):
    for i in range(1,5):
        my_turtle.forward(100)
        my_turtle.right(90)
    
#First turtle: square
def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")
        
    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("black")
    counter = 0;
    
    for counter in range (1,5):
     draw_The_Square(brad)
     brad.right(10)
    
    

       
    window.exitonclick()
draw_square()
draw_art()
