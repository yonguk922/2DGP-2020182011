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
    print("CIRCLE")
    #캐릭터 이미지 표시
    clear_canvas()
    character.draw(400, 300)
    update_canvas()
    pass


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

def move_ab():
    pass

def move_bc():
    pass

def move_ca():
    pass

def move_triangle():
    print("TRIANGLE")
    pass



while True:
    #move_circle()
    move_rectangle()
    #move_triangle()
    pass


close_canvas()
