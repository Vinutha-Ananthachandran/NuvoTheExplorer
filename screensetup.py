import turtle
import maze
import turtlehelper as th
import tkinter as tk
import solution

def setup_screen():
    screen = turtle.Screen()
    screen.title("Nuvo The Explorer")
    screen.setup(width=800, height=600)
    screen.bgcolor("#FCC600")

    text = th.create_turtle_object("black",4,"arrow")
    text.hideturtle()
    th.set_cursor(text,0,225,False)
    text.write("Welcome to the Tale of Nuvo and Nuvi", align="center", font=("Comic Sans MS", 24, "bold"))
    th.set_cursor(text,0,160,False)
    text.write("The Great Maze Adventure", align="center", font=("Comic Sans MS", 24, "bold"))
    th.set_cursor(text,290,-260,False)
    text.write("Nuevo Foundation", align="center", font=("Arial", 12, "bold"))

    # Register the image as a new shape
    screen.addshape("images/Nuevo.gif")   # must be .gif
    screen.addshape("images/Nuvi.gif")   # must be .gif

    # Create a turtle with that shape
    nuevo = th.create_turtle_object(turtle_shape="images/Nuevo.gif")
    th.set_cursor(nuevo,275,-130,False)

    maze.draw_maze()
    # Set Nuvi's starting position
    nuvi = th.create_turtle_object("green",5,"images/Nuvi.gif",1)
    th.set_cursor(nuvi,10,-135)
    nuvi.right(90)
    nuvi.right(90)

    canvas = screen.getcanvas()
    root = canvas.master

    def show_solution():
        btn.config(state=tk.DISABLED)  # Disable the button after clicking
        nuvo = th.create_turtle_object("#ffffff",4,"images/Nuvi.gif",5)
        th.set_cursor(nuvo,-20,110)
        nuvo.right(90)

        solution.draw_solution(nuvo,text)
        return

    btn = tk.Button(
        root, 
        text="View Solution", 
        command=show_solution,
        font=("Comic Sans MS", 13, "bold"),   # font style, size, weight
        fg="black", # text color
        bg="#0DBED4", # button background color
        relief="raised", # button border style: flat, raised, sunken, groove, ridge
        bd=4 # border width
    )
    btn.pack(pady=3)
    return