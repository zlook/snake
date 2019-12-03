import sys
import time

SCREEN = []


def init_screen():
    # 初始化屏幕数据
    global SCREEN

    for k in range(18):
        j = ["▓▓" for _ in range(32)]
        SCREEN.append(j)


def drow_point(x, y):
    if y < 0 or y >= len(SCREEN[0]):
        return
    if x < 0 or x >= len(SCREEN):
        return

    SCREEN[x][y] = "╬╬"


def display_screen(content):
    """
    将内容打印到终端
    :param content: [[len32], [], [], []...len18]
    :return:
    """
    screen_content = ""
    for i in content:
        screen_content += "".join(i) + "\n"

    print('\033c')
    sys.stdout.write(screen_content)


if __name__ == '__main__':
    init_screen()
    while True:
        for i in range(3):
            drow_point(i, 10)
            display_screen(SCREEN)
            time.sleep(0.5)
