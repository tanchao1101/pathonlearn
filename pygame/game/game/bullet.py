import pygame
import constants

class Bullet(pygame.sprite.Sprite):
    """
    子弹类
    """
    # 子弹状态，True活着
    active = True

    def __init__(self, screen, plane, speed= None):
        super().__init__()
        # 速度
        self.speed = speed or 10
        self.plane = plane
        self.image = pygame.image.load(constants.BULLET_IMG)
        self.screen = screen

        # 改变子弹的位置
        self.rect = self.image.get_rect()
        self.rect.centerx = plane.rect.centerx
        self.rect.top = plane.rect.top
        # 发射音乐效果
        self.shoot_sound = pygame.mixer.Sound(constants.BULLET_SHOOT_SOUND)
        self.shoot_sound.set_volume(0.3)
        self.shoot_sound.play()
    def update(self, *args):
        """
        更新子弹的位置
        :param args:
        :return:
        """
        self.rect.top -= self.speed
        # 超出屏幕的范围
        if self.rect.top < 0:
            self.remove(self.plane.bullets)
        self.screen.blit(self.image, self.rect)