""""
飞机的基类
"""
import pygame
import constants
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
        self._img_list = []
        self._destroy_img_list = []
        self.down_sound = None
        self.load_src()
        self.speed = speed or 10
        self.screen = screen
        self.rect = self._img_list[0].get_rect()
    def load_src(self):
        # 加载静态资源
        # 飞机的图像
        for img in self.plane_images:
            self._img_list.append(pygame.image.load(img))
        # 飞机坠毁图像
        for img in self.destroy_images:
            self._destroy_img_list.append(pygame.image.load(img))
        # 坠毁的音乐
        if self.down_sound_src:
            self.down_sound= pygame.mixer.Sound(self.down_sound_src)
    @property
    def image(self):
        return self._img_list[0]
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
class OurPlane(Plane):
    # 飞机的图片
    plane_images = [constants.OUR_PLANE_IMG_1, constants.OUR_PLANE_IMG_2]
    # 飞机爆炸的图片
    destroy_images = constants.OUR_DESTROY_IMG_LIST
    # 坠毁的音乐地址
    down_sound_src = None
