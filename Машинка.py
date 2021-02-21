import os
import sys
import pygame

pygame.init()
size = width, height = 600, 95
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


image_size = 130, 80
x = 10
v = 60
fps = 60
clock = pygame.time.Clock()


class Car(pygame.sprite.Sprite):
    image = load_image("car2.png")
    image = pygame.transform.scale(image, image_size)

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Car.image
        self.rect = self.image.get_rect()
        self.rect.y = 10

    def next_move(self):
        global v
        self.rect.x += v * fps / 1000
        if self.rect.x > width - image_size[0] or self.rect.x == 0:
            v *= (-1)
            self.image = pygame.transform.flip(self.image, 1, 0)


all_sprites = pygame.sprite.Group()
hero = Car(all_sprites)
if __name__ == '__main__':
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        hero.next_move()
        all_sprites.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
