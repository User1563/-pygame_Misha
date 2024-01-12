import pygame
import sys

pygame.init()
e = pygame.display.set_mode((1190, 800))
pygame.display.set_caption('Игра')
images = pygame.image.load('fdg.jpg')
m = images.get_rect(bottomright=(1200, 800))
e.blit(images, m)

buttonn = 200
buttonm = 30
j2x = 160
j2y = 370
font = pygame.font.Font(None, 30)

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

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        pygame.draw.rect(e, (150, 0, 0), (j2x, j2y, buttonn, buttonm))

        if j2x < mouse_pos[0] < j2x + buttonn and j2y < mouse_pos[1] < j2y + buttonm:
            if mouse_click[0] == 1:
                print('+')

            pygame.draw.rect(e, (100, 0, 0), (j2x, j2y, buttonn, buttonm))

        text = font.render('1', True, (61, 211, 91))
        text_rect = text.get_rect()
        text_rect.center = (j2x + buttonn // 2, j2y + buttonm // 2)
        e.blit(text, text_rect)

print(main())



