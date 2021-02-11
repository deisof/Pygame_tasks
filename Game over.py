import os
import sys
import pygame

pygame.init()
size = width, height = 600, 300
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class ScreenGameOver(pygame.sprite.Sprite):
    image = load_image("gameover.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = ScreenGameOver.image
        self.rect = self.image.get_rect()
        self.rect.x = -600
        self.rect.y = 0
        self.pos = 0

    def update(self):
        if self.rect.x > 0:
            self.rect = self.rect.move(0, 0)
        else:
            self.pos += v / fps
            self.rect = self.rect.move(self.pos, 0)


if __name__ == '__main__':
    all_sprites = pygame.sprite.Group()
    ScreenGameOver(all_sprites)

    v = 200
    fps = 30
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 255))
        all_sprites.draw(screen)
        all_sprites.update()
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
