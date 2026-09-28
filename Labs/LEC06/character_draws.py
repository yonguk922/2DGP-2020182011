# 실습 과제 진행
from pico2d import *

#맨 처음 해야할 일은.
open_canvas(800,600)
character = load_image('character.png')


def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)

def move_circle():
    for degree in range(360):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)
        draw_character(x, y)


def move_top():
    for x in range(50, 751, 5):
        draw_character(x, 550)

def move_right():
    for y in range(550, 49, -5):
        draw_character(750, y)

def move_bottom():
    for x in range(750, 49, -5):
        draw_character(x, 50)
def move_left():
    for y in range(50, 551, 5):
        draw_character(50, y)

def move_rectangle():
    move_top()
    move_right()
    move_bottom()
    move_left()
    print("RECTANGLE")
    pass

def move_line(x0, y0, x1, y1, n=100):
    for step in range(n + 1):
        t = step / n
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        draw_character(x, y)

def move_ab():
    move_line(100, 100, 700, 100)

def move_bc():
    move_line(700, 100, 400, 500)

def move_ca():
    move_line(400, 500, 100, 100)

def move_triangle():
    move_ab()
    move_bc()
    move_ca()


while True:
    #move_circle()
    move_rectangle()
    #move_triangle()
    pass


close_canvas()
