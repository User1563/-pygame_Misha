import pygame
import sys

pygame.init()
e = pygame.display.set_mode((1190, 800))
pygame.display.set_caption('Игра')
images = pygame.image.load('fdg.jpg')
m = images.get_rect(bottomright=(1200, 800))
e.blit(images, m)
color = pygame.Color(255, 0, 0)
colormouse = pygame.Color(200, 0, 0)
buttonn = 30
buttonm = 30
j2x = 220
j2y = 370
jx = 260
jy = 370
jx1 = 180
jy1 = 370
jx2 = 300
jy2 = 370
jx3 = 1010
jy3 = 370
jx4 = 970
jy4 = 370
jx5 = 930
jy5 = 370
jx6 = 890
jy6 = 370
ex = 220
ey = 750
ex2 = 260
ey2 = 750
ex3 = 300
ey3 = 750
ex4 = 180
ey4 = 750
ex5 = 890
ey5 = 750
ex6 = 930
ey6 = 750
ex7 = 970
ey7 = 750
ex8 = 1010
ey8 = 750
# font = pygame.font.Font(None, 30)

try:
    sound = pygame.mixer.Sound('cvb.mp3')
    sound.play()
except pygame.error as q:
    print(q)


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                # pygame.quit()
                # sys.exit(0)
        mouse = pygame.mouse.get_pos()
        mouse_get = pygame.mouse.get_pressed()
        pygame.draw.rect(e, color, (j2x, j2y, buttonn, buttonm))
        pygame.draw.rect(e, color, (jx, jy, 30, 30))
        pygame.draw.rect(e, color, (jx1, jy1, 30, 30))
        pygame.draw.rect(e, color, (jx2, jy2, 30, 30))
        pygame.draw.rect(e, color, (jx3, jy3, 30, 30))
        pygame.draw.rect(e, color, (jx4, jy4, 30, 30))
        pygame.draw.rect(e, color, (jx5, jy5, 30, 30))
        pygame.draw.rect(e, color, (jx6, jy6, 30, 30))
        pygame.draw.rect(e, color, (ex, ey, 30, 30))
        pygame.draw.rect(e, color, (ex2, ey2, 30, 30))
        pygame.draw.rect(e, color, (ex3, ey3, 30, 30))
        pygame.draw.rect(e, color, (ex4, ey4, 30, 30))
        pygame.draw.rect(e, color, (ex5, ey5, 30, 30))
        pygame.draw.rect(e, color, (ex6, ey6, 30, 30))
        pygame.draw.rect(e, color, (ex7, ey7, 30, 30))
        pygame.draw.rect(e, color, (ex8, ey8, 30, 30))
        if j2x < mouse[0] < j2x + buttonn and j2y < mouse[1] < j2y + buttonm:
            if mouse_get[0] == 1:
                print('+')
            pygame.draw.rect(e, colormouse, (j2x, j2y, buttonn, buttonm))

        if jx < mouse[0] < jx + buttonn and jy < mouse[1] < jy + buttonm:
            if mouse_get[0] == 1:
                print('-')
            pygame.draw.rect(e, colormouse, (jx, jy, buttonn, buttonm))

        if jx1 < mouse[0] < jx1 + buttonn and jy1 < mouse[1] < jy1 + buttonm:
            if mouse_get[0] == 1:
                print('%')
            pygame.draw.rect(e, colormouse, (jx1, jy1, buttonn, buttonm))

        if jx2 < mouse[0] < jx2 + buttonn and jy2 < mouse[1] < jy2 + buttonm:
            if mouse_get[0] == 1:
                print('nm')
            pygame.draw.rect(e, colormouse, (jx2, jy2, buttonn, buttonm))

        if jx3 < mouse[0] < jx3 + buttonn and jy3 < mouse[1] < jy3 + buttonm:
            if mouse_get[0] == 1:
                print('er')
            pygame.draw.rect(e, colormouse, (jx3, jy3, buttonn, buttonm))

        if jx4 < mouse[0] < jx4 + buttonn and jy4 < mouse[1] < jy4 + buttonm:
            if mouse_get[0] == 1:
                print('ud')
            pygame.draw.rect(e, colormouse, (jx4, jy4, buttonn, buttonm))

        if jx5 < mouse[0] < jx5 + buttonn and jy5 < mouse[1] < jy5 + buttonm:
            if mouse_get[0] == 1:
                print('vb')
            pygame.draw.rect(e, colormouse, (jx5, jy5, buttonn, buttonm))

        if jx6 < mouse[0] < jx6 + buttonn and jy6 < mouse[1] < jy6 + buttonm:
            if mouse_get[0] == 1:
                print('rty')
            pygame.draw.rect(e, colormouse, (jx6, jy6, buttonn, buttonm))

        if ex < mouse[0] < ex + buttonn and ey < mouse[1] < ey + buttonm:
            if mouse_get[0] == 1:
                print('etr')
            pygame.draw.rect(e, colormouse, (ex, ey, buttonn, buttonm))

        if ex2 < mouse[0] < ex2 + buttonn and ey2 < mouse[1] < ey2 + buttonm:
            if mouse_get[0] == 1:
                print('dfg')
            pygame.draw.rect(e, colormouse, (ex2, ey2, buttonn, buttonm))

        if ex3 < mouse[0] < ex3 + buttonn and ey3 < mouse[1] < ey3 + buttonm:
            if mouse_get[0] == 1:
                print('vnv')
            pygame.draw.rect(e, colormouse, (ex3, ey3, buttonn, buttonm))

        if ex4 < mouse[0] < ex4 + buttonn and ey4 < mouse[1] < ey4 + buttonm:
            if mouse_get[0] == 1:
                print('hkj')
            pygame.draw.rect(e, colormouse, (ex4, ey4, buttonn, buttonm))

        if ex5 < mouse[0] < ex5 + buttonn and ey5 < mouse[1] < ey5 + buttonm:
            if mouse_get[0] == 1:
                print('vxc')
            pygame.draw.rect(e, colormouse, (ex5, ey5, buttonn, buttonm))

        if ex6 < mouse[0] < ex6 + buttonn and ey6 < mouse[1] < ey6 + buttonm:
            if mouse_get[0] == 1:
                print('iou')
            pygame.draw.rect(e, colormouse, (ex6, ey6, buttonn, buttonm))

        if ex7 < mouse[0] < ex7 + buttonn and ey7 < mouse[1] < ey7 + buttonm:
            if mouse_get[0] == 1:
                print('sdd')
            pygame.draw.rect(e, colormouse, (ex7, ey7, buttonn, buttonm))

        if ex8 < mouse[0] < ex8 + buttonn and ey8 < mouse[1] < ey8 + buttonm:
            if mouse_get[0] == 1:
                print('nky')
            pygame.draw.rect(e, colormouse, (ex8, ey8, buttonn, buttonm))

        pygame.display.flip()
        # text = font.render('1', None, (61, 211, 91))
        # text_rect = text.get_rect()
        # text_rect.center = (j2x + 100, j2y + 15)
        # e.blit(text, text_rect)


print(main())

