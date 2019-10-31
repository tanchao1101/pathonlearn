""""
飞机的基类
"""
import pygame
import constants

from game.game.bullet import Bullet


class Plane(pygame.sprite.Sprite):
    # 飞机的图片
    plane_images = []
    # 飞机爆炸的图片
    destroy_images = []
    # 坠毁的音乐地址
    down_sound_src = None
    # 飞机的状态：true,活的，false,死的
    active = True
    # 该飞机发射的子弹精灵图
    bullets = pygame.sprite.Group()
    def __init__(self, screen: object, speed: object = None) -> object:
        super().__init__()
        # 加载静态资源
        self.img_list = []
        self._destroy_img_list = []
        self.down_sound = None
        self.load_src()
        self.speed = speed or 10
        self.screen = screen
        self.rect = self.img_list[0].get_rect()
        # 飞机的宽高
        self.plane_w, self.plane_h = self.img_list[0].get_size()
        # 游戏窗口的宽高
        self.width, self.height = self.screen.get_size()
        # 改变飞机的初始位置
        self.rect.left = int((self.width - self.plane_w) / 2)
        self.rect.top = int(self.height/2)
    def load_src(self):
        # 加载静态资源
        # 飞机的图像
        for img in self.plane_images:
            self.img_list.append(pygame.image.load(img))
        # 飞机坠毁图像
        for img in self.destroy_images:
            self._destroy_img_list.append(pygame.image.load(img))
        # 坠毁的音乐
        if self.down_sound_src:
            self.down_sound= pygame.mixer.Sound(self.down_sound_src)
    @property
    def image(self):
        return self.img_list[0]
    def blit_me(self):
        self.screen.blit(self.image, self.rect)
    def move_up(self):
        self.rect.top -= self.speed
    def move_down(self):
        self.rect.top += self.speed
    def move_left(self):
        self.rect.left -= self.speed
    def move_right(self):
        self.rect.left += self.speed
    def broken_down(self):
        #播放坠毁的音乐
        if self.down_sound:
            self.down_sound.play()
        # 播放坠毁动画
        for img in self._destroy_img_list:
            self.screen.blit(img, self.rect)
        # 坠毁后
        self.active = False
    def shoot(self):
        # 飞机发射子弹
        bullet = Bullet( self.screen, self , 15)
        self.bullets.add(bullet)

class OurPlane(Plane):
    # 飞机的图片
    plane_images = [constants.OUR_PLANE_IMG_1, constants.OUR_PLANE_IMG_2]
    # 飞机爆炸的图片
    destroy_images = constants.OUR_DESTROY_IMG_LIST
    # 坠毁的音乐地址
    down_sound_src = None
    def update(self, frame):
        if frame % 5 == 0:
            self.screen.blit(self.img_list[0], self.rect)
        else:
            self.screen.blit(self.img_list[1], self.rect)
    def move_up(self):
        super().move_up()
        if self.rect.top <=0:
            self.rect.top = 0
    def move_down(self):
        super().move_down()
        if self.rect.top >= (self.height - self.plane_h):
            self.rect.top = self.height - self.plane_h
    def move_left(self):
        super().move_left()
        if self.rect.left <=0:
            self.rect.left = 0
    def move_right(self):
        super().move_right()
        if self.rect.left >= (self.width - self.plane_w):
            self.rect.left = self.width - self.plane_w