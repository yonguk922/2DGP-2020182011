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
        character.draw(x, 550)
        update_canvas()
    pass

def move_right():
    print("RIGHT")
    pass

def move_bottom():
    print("BOTTOM")
    pass

def move_left():
    print("LEFT")
    pass

def move_rectangle():
    move_top()
    move_right()
    move_bottom()
    move_left()
    print("RECTANGLE")
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
