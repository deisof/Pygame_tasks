import os
import sys
import pygame

pygame.init()
size = width, height = 300, 300
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Герой двигается!')
screen.fill('white')


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((x, y))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


position = 0, 0
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
image = load_image('creature.png')
image = pygame.transform.scale(image, (100, 100))

all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
sprite.image = load_image("creature.png")
sprite.rect = sprite.image.get_rect()
all_sprites.add(sprite)
sprite.rect.x = 0
sprite.rect.y = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                sprite.rect.y += 10
            if pygame.key.get_pressed()[pygame.K_UP]:
                sprite.rect.y -= 10
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                sprite.rect.x -= 10
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                sprite.rect.x += 10
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
