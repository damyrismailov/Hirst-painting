from turtle import Screen
import turtle as t
import random
t.colormode(255)
dot = t.Turtle()
dot.hideturtle()
color = [(235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51), (6, 68, 42), (176, 176, 233), (239, 168, 161), (249, 8, 48), (5, 246, 222), (15, 76, 110), (243, 15, 14), (38, 43, 221)]
dot.speed("fastest")
dot.penup()
dot.setheading(225)
dot.forward(300)
dot.setheading(0)
dots = 100

for dot_counts in range(1, dots + 1):
    dot.dot(20, random.choice(color))
    dot.forward(50)
    if dot_counts % 10 == 0:
       dot.penup()
       dot.setheading(90)
       dot.forward(50)
       dot.setheading(180)
       dot.forward(500)
       dot.setheading(0)



screen = Screen()
screen.exitonclick()

if __name__ == '__main__':
    print('Run the game here')
