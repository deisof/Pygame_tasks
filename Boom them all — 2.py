import os
import sys
import random

import pygame

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


image_size = 50, 50
need_coordinates = pygame.sprite.Group()


class Bomb(pygame.sprite.Sprite):
    image = load_image("bomb.png")
    image = pygame.transform.scale(image, image_size)
    image_boom = load_image("boom.png", -1)
    image_boom = pygame.transform.scale(image_boom, image_size)

    def __init__(self, group):
        super().__init__(group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - image_size[0])
        self.rect.y = random.randrange(height - image_size[0])
        while pygame.sprite.spritecollideany(self, need_coordinates):
            self.rect.x = random.randrange(width - image_size[0])
            self.rect.y = random.randrange(height - image_size[0])
        self.add(need_coordinates)

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom

    def get_event(self):
        if self.rect.collidepoint(event.pos):
            self.image = self.image_boom


all_sprites = pygame.sprite.Group()
bomb_image = load_image("bomb.png")
bomb_image = pygame.transform.scale(bomb_image, image_size)

for _ in range(20):
    Bomb(all_sprites)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for bomb in all_sprites:
                bomb.get_event()
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
pygame.quit()
