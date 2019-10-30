import os
print(__file__)
# 项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 静态文件的目录  \\ /
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
# 背景图片
BG_IMG = os.path.join(ASSETS_DIR, 'images/background.png')
# 标题图片
IMG_GAME_TITLE = os.path.join(ASSETS_DIR, 'images/game_title.png')
# 开始游戏按钮图片
IMG_GAME_START_BTN = os.path.join(ASSETS_DIR, 'images/game_start.png')
# 背景音乐
BG_MUSIC = os.path.join(ASSETS_DIR, 'sounds/game_bg_music.mp3')

# 我方飞机的静态资源
OUR_PLANE_IMG_1 = os.path.join(ASSETS_DIR, 'images/hero1.png')
OUR_PLANE_IMG_2 = os.path.join(ASSETS_DIR, 'images/hero2.png')
OUR_DESTROY_IMG_LIST = [
    os.path.join(ASSETS_DIR, 'images/hero_broken_n1.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n2.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n3.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n4.png')
]