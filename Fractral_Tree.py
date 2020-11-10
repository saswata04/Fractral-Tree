import turtle as tu

my_turtle = tu.Turtle()

my_turtle.left(90)
my_turtle.speed(20)
my_turtle.pensize(5)
my_turtle.screen.title("Fractal Tree")

def fractal(n):
    if n<10:
        return
    else:
        my_turtle.forward(n)
        my_turtle.left(30)
        fractal(3*n/4)
        my_turtle.right(60)
        fractal(3*n/4)
        my_turtle.left(30)
        my_turtle.backward(n)

fractal(80)

tu.done()