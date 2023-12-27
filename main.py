import turtle
import random

while True:
    try:
        num = int(input('Enter the number of turtles from 2 - 10 '))
        if num > 10 or num < 2:
            continue
        break

    except ValueError:
        pass

colors = ['black', 'green', 'blue', 'pink', 'purple', 'grey', 'red', 'yellow', 'orange', 'gold']

def initialize():
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.title('Random Racer')
    screen.update()

def turtles(number=num):
    turtle_list = []
    position = 60
    for i in range(number):
        t = turtle.Turtle('turtle')
        t.left(90)
        t.penup()
        t.setpos(-275 + (position * i), -250)
        t.color(colors[i])
        turtle_list.append(t)
    return turtle_list

def movement(turtles_function):
    run = True

    while run:
        for i in turtles_function:
            x = random.randint(1, 15)  # Can adjust speed of turtles by increasing a or b values
            i.pendown()
            i.forward(x)
            if i.ycor() > 299: # Reach end screen
                winner = list(i.color())
                run = False
                print('The winner is', winner[0])
                break

def main():
    initialize()
    movement(turtles())

if __name__ == '__main__':
    main()


