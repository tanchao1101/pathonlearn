import pygame
import sys
import constants
# from constants import BG_IMG, BG_MUSIC
from game.game.plane import OurPlane


def mian():
    # 游戏入口初始化
    print(__name__)
    #初始化
    pygame.init()
    width, height = 480, 852
    #屏幕对象
    screen = pygame.display.set_mode((width, height))
    # 设置窗口
    pygame.display.set_caption('飞机大战')
    # 加载背景图片
    bg = pygame.image.load(constants.BG_IMG)
    # 加载游戏标题
    img_game_title = pygame.image.load(constants.IMG_GAME_TITLE)
    img_game_title_rect = img_game_title.get_rect()
    # 获取宽高
    t_width, t_height = img_game_title.get_size()
    img_game_title_rect.topleft = (int((width -t_width)/2), int(height/2 - t_height))
    # 加载开始游戏按钮图片
    btn_start = pygame.image.load(constants.IMG_GAME_START_BTN)
    btn_start_rect = btn_start.get_rect()
    # 获取宽高
    btn_width, btn_height = btn_start.get_size()
    btn_start_rect.topleft = (int((width -btn_width)/2), int(height/2 + btn_height))
    # 加载背景音乐
    # pygame.mixer.music.load(constants.BG_MUSIC)
    # pygame.mixer.music.play(-1)  # 无限循环播放
    # pygame.mixer.music.set_volume(0.2)  #设置音量
    status = 0 #0准备中，1游戏中，2游戏结束
    our_plane = OurPlane(screen)
    # 播放帧数
    frame = 0

    while True:
        #1.监听事件
        for event in pygame.event.get():
            #退出游戏
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 鼠标点击进入游戏
                # 游戏正在准备中，点击才能进入游戏
                if status == 0:
                    status = 1
        # 更新游戏的状态
        if status == 0:
            # 绘制
            screen.blit(bg, bg.get_rect())
            screen.blit(img_game_title, img_game_title_rect)
            screen.blit(btn_start, btn_start_rect)
        elif status == 1:
            # 绘制
            screen.blit(bg, bg.get_rect())
            #  绘制飞机
            our_plane.blit_me()

        pygame.display.flip()
if __name__ == '__main__':
    print(__name__)
    mian()