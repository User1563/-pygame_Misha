import pygame
import sys

pygame.init()
e = pygame.display.set_mode((1190, 800))
pygame.display.set_caption('Игра')
images = pygame.image.load('fdg.jpg')
m = images.get_rect(bottomright=(1200, 800))
e.blit(images, m)
try:
    sound = pygame.mixer.Sound('cvb.mp3')
    sound.play()
except pygame.error as q:
    print(q)


def main():
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            pygame.time.delay(10)


print(main())
