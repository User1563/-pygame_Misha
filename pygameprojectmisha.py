import pygame

pygame.init()
e = pygame.display.set_mode((1190, 800))
pygame.display.set_caption('Игра')
images = pygame.image.load('fdg (1).jpg')
m = images.get_rect(bottomright=(1200, 800))
e.blit(images, m)
color = pygame.Color(255, 0, 0)
colormouse = pygame.Color(200, 0, 0)
image1 = pygame.transform.scale(images, (430, 280))
e.blit(image1, (40, 30))
image2 = pygame.transform.scale(images, (430, 280))
e.blit(image2, (720, 30))
image3 = pygame.transform.scale(images, (430, 280))
e.blit(image3, (720, 410))
image4 = pygame.transform.scale(images, (430, 280))
e.blit(image4, (40, 410))
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
jx3 = 990
jy3 = 370
jx4 = 950
jy4 = 370
jx5 = 910
jy5 = 370
jx6 = 870
jy6 = 370
ex = 220
ey = 750
ex2 = 260
ey2 = 750
ex3 = 300
ey3 = 750
ex4 = 180
ey4 = 750
ex5 = 870
ey5 = 750
ex6 = 910
ey6 = 750
ex7 = 950
ey7 = 750
ex8 = 990
ey8 = 750
font = pygame.font.Font(None, 30)
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
        font = pygame.font.Font(None, 50)
        text = font.render("4", True, (0, 0, 0))
        text_x = 996
        text_y = 333
        e.blit(text, (text_x, text_y))

        text2 = font.render("4", True, (0, 0, 0))
        text_x2 = 996
        text_y2 = 713
        e.blit(text2, (text_x2, text_y2))

        text3 = font.render("3", True, (0, 0, 0))
        text_x3 = 956
        text_y3 = 713
        e.blit(text3, (text_x3, text_y3))

        text4 = font.render("2", True, (0, 0, 0))
        text_x4 = 916
        text_y4 = 713
        e.blit(text4, (text_x4, text_y4))

        text5 = font.render("1", True, (0, 0, 0))
        text_x5 = 876
        text_y5 = 713
        e.blit(text5, (text_x5, text_y5))

        text6 = font.render("3", True, (0, 0, 0))
        text_x6 = 266
        text_y6 = 713
        e.blit(text6, (text_x6, text_y6))

        text7 = font.render("1", True, (0, 0, 0))
        text_x7 = 186
        text_y7 = 713
        e.blit(text7, (text_x7, text_y7))

        text8 = font.render("2", True, (0, 0, 0))
        text_x8 = 226
        text_y8 = 713
        e.blit(text8, (text_x8, text_y8))

        text9 = font.render("2", True, (0, 0, 0))
        text_x9 = 226
        text_y9 = 333
        e.blit(text9, (text_x9, text_y9))

        text10 = font.render("3", True, (0, 0, 0))
        text_x10 = 266
        text_y10 = 333
        e.blit(text10, (text_x10, text_y10))

        text11 = font.render("1", True, (0, 0, 0))
        text_x11 = 184
        text_y11 = 333
        e.blit(text11, (text_x11, text_y11))

        text12 = font.render("4", True, (0, 0, 0))
        text_x12 = 306
        text_y12 = 333
        e.blit(text12, (text_x12, text_y12))

        text13 = font.render("3", True, (0, 0, 0))
        text_x13 = 956
        text_y13 = 333
        e.blit(text13, (text_x13, text_y13))

        text14 = font.render("2", True, (0, 0, 0))
        text_x14 = 916
        text_y14 = 333
        e.blit(text14, (text_x14, text_y14))

        text15 = font.render("1", True, (0, 0, 0))
        text_x15 = 876
        text_y15 = 333
        e.blit(text15, (text_x15, text_y15))

        text16 = font.render("4", True, (0, 0, 0))
        text_x16 = 306
        text_y16 = 713
        e.blit(text16, (text_x16, text_y16))

        if j2x < mouse[0] < j2x + buttonn and j2y < mouse[1] < j2y + buttonm:
            if mouse_get[0] == 1:
                main2()
                pygame.time.delay(1000)
            pygame.draw.rect(e, colormouse, (j2x, j2y, buttonn, buttonm))

        if jx < mouse[0] < jx + buttonn and jy < mouse[1] < jy + buttonm:
            if mouse_get[0] == 1:
                main3()
                pygame.time.delay(1000)
            pygame.draw.rect(e, colormouse, (jx, jy, buttonn, buttonm))

        if jx1 < mouse[0] < jx1 + buttonn and jy1 < mouse[1] < jy1 + buttonm:
            if mouse_get[0] == 1:
                main4()
                pygame.time.delay(1000)
            pygame.draw.rect(e, colormouse, (jx1, jy1, buttonn, buttonm))

        if jx2 < mouse[0] < jx2 + buttonn and jy2 < mouse[1] < jy2 + buttonm:
            if mouse_get[0] == 1:
                main5()
                pygame.time.delay(1000)
            pygame.draw.rect(e, colormouse, (jx2, jy2, buttonn, buttonm))

        if jx3 < mouse[0] < jx3 + buttonn and jy3 < mouse[1] < jy3 + buttonm:
            if mouse_get[0] == 1:
                main6()
                pygame.time.delay(1000)
            pygame.draw.rect(e, colormouse, (jx3, jy3, buttonn, buttonm))

        if jx4 < mouse[0] < jx4 + buttonn and jy4 < mouse[1] < jy4 + buttonm:
            if mouse_get[0] == 1:
                main7()
                pygame.time.delay(1000)
            pygame.draw.rect(e, colormouse, (jx4, jy4, buttonn, buttonm))

        if jx5 < mouse[0] < jx5 + buttonn and jy5 < mouse[1] < jy5 + buttonm:
            if mouse_get[0] == 1:
                main8()
                pygame.time.delay(1000)
            pygame.draw.rect(e, colormouse, (jx5, jy5, buttonn, buttonm))

        if jx6 < mouse[0] < jx6 + buttonn and jy6 < mouse[1] < jy6 + buttonm:
            if mouse_get[0] == 1:
                main9()
                pygame.time.delay(1000)
            pygame.draw.rect(e, colormouse, (jx6, jy6, buttonn, buttonm))

        if ex < mouse[0] < ex + buttonn and ey < mouse[1] < ey + buttonm:
            if mouse_get[0] == 1:
                main10()
                pygame.time.delay(1000)
            pygame.draw.rect(e, colormouse, (ex, ey, buttonn, buttonm))

        if ex2 < mouse[0] < ex2 + buttonn and ey2 < mouse[1] < ey2 + buttonm:
            if mouse_get[0] == 1:
                main12()
                pygame.time.delay(1000)
            pygame.draw.rect(e, colormouse, (ex2, ey2, buttonn, buttonm))

        if ex3 < mouse[0] < ex3 + buttonn and ey3 < mouse[1] < ey3 + buttonm:
            if mouse_get[0] == 1:
                main13()
                pygame.time.delay(1000)
            pygame.draw.rect(e, colormouse, (ex3, ey3, buttonn, buttonm))

        if ex4 < mouse[0] < ex4 + buttonn and ey4 < mouse[1] < ey4 + buttonm:
            if mouse_get[0] == 1:
                main11()
                pygame.time.delay(1000)
            pygame.draw.rect(e, colormouse, (ex4, ey4, buttonn, buttonm))

        if ex5 < mouse[0] < ex5 + buttonn and ey5 < mouse[1] < ey5 + buttonm:
            if mouse_get[0] == 1:
                main14()
                pygame.time.delay(1000)
            pygame.draw.rect(e, colormouse, (ex5, ey5, buttonn, buttonm))

        if ex6 < mouse[0] < ex6 + buttonn and ey6 < mouse[1] < ey6 + buttonm:
            if mouse_get[0] == 1:
                main15()
                pygame.time.delay(1000)
            pygame.draw.rect(e, colormouse, (ex6, ey6, buttonn, buttonm))

        if ex7 < mouse[0] < ex7 + buttonn and ey7 < mouse[1] < ey7 + buttonm:
            if mouse_get[0] == 1:
                main16()
                pygame.time.delay(1000)
            pygame.draw.rect(e, colormouse, (ex7, ey7, buttonn, buttonm))

        if ex8 < mouse[0] < ex8 + buttonn and ey8 < mouse[1] < ey8 + buttonm:
            if mouse_get[0] == 1:
                main17()
                pygame.time.delay(1000)
            pygame.draw.rect(e, colormouse, (ex8, ey8, buttonn, buttonm))
        pygame.display.flip()


def main2():
    font = pygame.font.Font(None, 48)
    text = font.render("2", True, (0, 0, 0))
    text_x = 226
    text_y = 333
    text_w = text.get_width()
    text_h = text.get_height()
    pygame.draw.rect(e, (255, 0, 0), (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 6)


def main3():
    font = pygame.font.Font(None, 48)
    text = font.render("3", True, (0, 0, 0))
    text_x = 266
    text_y = 333
    text_w = text.get_width()
    text_h = text.get_height()
    pygame.draw.rect(e, (0, 255, 0), (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 6)
    pygame.draw.rect(e, (0, 255, 0), (392, 8, 100, 10))


def main4():
    font = pygame.font.Font(None, 48)
    text = font.render("1", True, (0, 0, 0))
    text_x = 186
    text_y = 333
    text_w = text.get_width()
    text_h = text.get_height()
    pygame.draw.rect(e, (255, 0, 0), (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 6)


def main5():
    font = pygame.font.Font(None, 48)
    text = font.render("4", True, (0, 0, 0))
    text_x = 306
    text_y = 333
    text_w = text.get_width()
    text_h = text.get_height()
    pygame.draw.rect(e, (255, 0, 0), (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 6)


def main6():
    font = pygame.font.Font(None, 48)
    text = font.render("4", True, (0, 0, 0))
    text_x = 996
    text_y = 333
    text_w = text.get_width()
    text_h = text.get_height()
    pygame.draw.rect(e, (0, 255, 0), (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 6)
    pygame.draw.rect(e, (0, 255, 0), (500, 8, 100, 10))


def main7():
    font = pygame.font.Font(None, 48)
    text = font.render("3", True, (0, 0, 0))
    text_x = 956
    text_y = 333
    text_w = text.get_width()
    text_h = text.get_height()
    pygame.draw.rect(e, (255, 0, 0), (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 6)


def main8():
    font = pygame.font.Font(None, 48)
    text = font.render("2", True, (0, 0, 0))
    text_x = 916
    text_y = 333
    text_w = text.get_width()
    text_h = text.get_height()
    pygame.draw.rect(e, (255, 0, 0), (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 6)


def main9():
    font = pygame.font.Font(None, 48)
    text = font.render("1", True, (0, 0, 0))
    text_x = 876
    text_y = 333
    text_w = text.get_width()
    text_h = text.get_height()
    pygame.draw.rect(e, (255, 0, 0), (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 6)


def main10():
    font = pygame.font.Font(None, 48)
    text = font.render("2", True, (0, 0, 0))
    text_x = 226
    text_y = 713
    text_w = text.get_width()
    text_h = text.get_height()
    pygame.draw.rect(e, (255, 0, 0), (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 6)


def main11():
    font = pygame.font.Font(None, 48)
    text = font.render("1", True, (0, 0, 0))
    text_x = 186
    text_y = 713
    text_w = text.get_width()
    text_h = text.get_height()
    pygame.draw.rect(e, (0, 255, 0), (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 6)
    pygame.draw.rect(e, (0, 255, 0), (608, 8, 100, 10))


def main12():
    font = pygame.font.Font(None, 48)
    text = font.render("3", True, (0, 0, 0))
    text_x = 266
    text_y = 713
    text_w = text.get_width()
    text_h = text.get_height()
    pygame.draw.rect(e, (255, 0, 0), (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 6)


def main13():
    font = pygame.font.Font(None, 48)
    text = font.render("4", True, (0, 0, 0))
    text_x = 306
    text_y = 713
    text_w = text.get_width()
    text_h = text.get_height()
    pygame.draw.rect(e, (255, 0, 0), (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 6)


def main14():
    font = pygame.font.Font(None, 48)
    text = font.render("1", True, (0, 0, 0))
    text_x = 876
    text_y = 713
    text_w = text.get_width()
    text_h = text.get_height()
    pygame.draw.rect(e, (255, 0, 0), (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 6)


def main15():
    font = pygame.font.Font(None, 48)
    text = font.render("2", True, (0, 0, 0))
    text_x = 916
    text_y = 713
    text_w = text.get_width()
    text_h = text.get_height()
    pygame.draw.rect(e, (255, 0, 0), (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 6)


def main16():
    font = pygame.font.Font(None, 48)
    text = font.render("3", True, (0, 0, 0))
    text_x = 956
    text_y = 713
    text_w = text.get_width()
    text_h = text.get_height()
    pygame.draw.rect(e, (255, 0, 0), (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 6)


def main17():
    font = pygame.font.Font(None, 48)
    text = font.render("4", True, (0, 0, 0))
    text_x = 996
    text_y = 713
    text_w = text.get_width()
    text_h = text.get_height()
    pygame.draw.rect(e, (0, 255, 0), (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 6)
    pygame.draw.rect(e, (0, 255, 0), (716, 8, 100, 10))


if __name__ == '__main__':
    main()

