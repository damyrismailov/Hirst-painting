from turtle import Screen
import turtle as t
import random
t.colormode(255)
diddy = t.Turtle()
diddy.hideturtle()
color = [(235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51), (6, 68, 42), (176, 176, 233), (239, 168, 161), (249, 8, 48), (5, 246, 222), (15, 76, 110), (243, 15, 14), (38, 43, 221)]
diddy.speed("fastest")
diddy.penup()
diddy.setheading(225)
diddy.forward(300)
diddy.setheading(0)
dot = 100

for dot_counts in range(1, dot + 1):
    diddy.dot(20, random.choice(color))
    diddy.forward(50)
    if dot_counts % 10 == 0:
       diddy.penup()
       diddy.setheading(90)
       diddy.forward(50)
       diddy.setheading(180)
       diddy.forward(500)
       diddy.setheading(0)



screen = Screen()
screen.exitonclick()

if __name__ == '__main__':
    print('Run the game here')
