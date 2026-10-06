from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running, dir_x, face

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1

    # 좌우로 움직일 때만 바라보는 방향을 바꾼다
    if dir_x > 0:
        face = 1
    elif dir_x < 0:
        face = -1


running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
dir_x = 0
face = 1  # 1: 오른쪽, -1: 왼쪽

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    # 스프라이트 줄(아래부터): 0 왼쪽 달리기, 100 오른쪽 달리기, 200 왼쪽 IDLE, 300 오른쪽 IDLE
    if dir_x != 0:
        row = 100 if face == 1 else 0
    else:
        row = 300 if face == 1 else 200
    character.clip_draw(frame * 100, row, 100, 100, x, y)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += dir_x * 5
    delay(0.05)

close_canvas()
