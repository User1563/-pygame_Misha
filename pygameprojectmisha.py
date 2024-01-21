import pygame

pygame.init()
game_field = pygame.display.set_mode((1190, 800))
pygame.display.set_caption('Игра')
images = pygame.image.load('fdg.jpg')
imagem2 = images.get_rect(bottomright=(1200, 800))
game_field.blit(images, imagem2)
color = pygame.Color(255, 0, 0)
colormouse = pygame.Color(200, 0, 0)
imagess = pygame.image.load('dert.jpg')
image1 = pygame.transform.scale(imagess, (430, 280))
game_field.blit(image1, (40, 30))
imagess2 = pygame.image.load('fgt.jpg')
image2 = pygame.transform.scale(imagess2, (430, 280))
game_field.blit(image2, (720, 30))
imagess3 = pygame.image.load('colorr.jpg')
image3 = pygame.transform.scale(imagess3, (430, 280))
game_field.blit(image3, (720, 410))
imagess4 = pygame.image.load('img.jpg')
image4 = pygame.transform.scale(imagess4, (430, 280))
game_field.blit(image4, (40, 410))
buttonn = 30
buttonm = 30
cor_2x = 220
cor_2y = 370
cor_3x = 260
cor_3y = 370
cor_x = 180
cor_y = 370
cor_4x = 300
cor_4y = 370
cor_8x = 990
cor_8y = 370
cor_7x = 950
cor_7y = 370
cor_6x = 910
cor_6y = 370
cor_5x = 870
cor_5y = 370
cor_10x = 220
cor_10y = 750
cor_11x = 260
cor_11y = 750
cor_12x = 300
cor_12y = 750
cor_9x = 180
cor_9y = 750
cor_13x = 870
cor_13y = 750
cor_14x = 910
cor_14y = 750
cor_15x = 950
cor_15y = 750
cor_16x = 990
cor_16y = 750
font = pygame.font.Font(None, 30)
try:
    sound = pygame.mixer.Sound('cvb.mp3')
    sound.play()
except pygame.error as q:
    print(q)


def game_main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        mouse = pygame.mouse.get_pos()
        mouse_get = pygame.mouse.get_pressed()
        pygame.draw.rect(game_field, color, (cor_2x, cor_2y, buttonn, buttonm))
        pygame.draw.rect(game_field, color, (cor_3x, cor_3y, 30, 30))
        pygame.draw.rect(game_field, color, (cor_x, cor_y, 30, 30))
        pygame.draw.rect(game_field, color, (cor_4x, cor_4y, 30, 30))
        pygame.draw.rect(game_field, color, (cor_8x, cor_8y, 30, 30))
        pygame.draw.rect(game_field, color, (cor_7x, cor_7y, 30, 30))
        pygame.draw.rect(game_field, color, (cor_6x, cor_6y, 30, 30))
        pygame.draw.rect(game_field, color, (cor_5x, cor_5y, 30, 30))
        pygame.draw.rect(game_field, color, (cor_10x, cor_10y, 30, 30))
        pygame.draw.rect(game_field, color, (cor_11x, cor_11y, 30, 30))
        pygame.draw.rect(game_field, color, (cor_12x, cor_12y, 30, 30))
        pygame.draw.rect(game_field, color, (cor_9x, cor_9y, 30, 30))
        pygame.draw.rect(game_field, color, (cor_13x, cor_13y, 30, 30))
        pygame.draw.rect(game_field, color, (cor_14x, cor_14y, 30, 30))
        pygame.draw.rect(game_field, color, (cor_15x, cor_15y, 30, 30))
        pygame.draw.rect(game_field, color, (cor_16x, cor_16y, 30, 30))
        font = pygame.font.Font(None, 50)
        text = font.render("4", True, (0, 0, 0))
        text_x = 996
        text_y = 333
        game_field.blit(text, (text_x, text_y))

        text2 = font.render("4", True, (0, 0, 0))
        text_x2 = 996
        text_y2 = 713
        game_field.blit(text2, (text_x2, text_y2))

        text3 = font.render("3", True, (0, 0, 0))
        text_x3 = 956
        text_y3 = 713
        game_field.blit(text3, (text_x3, text_y3))

        text4 = font.render("2", True, (0, 0, 0))
        text_x4 = 916
        text_y4 = 713
        game_field.blit(text4, (text_x4, text_y4))

        text5 = font.render("1", True, (0, 0, 0))
        text_x5 = 876
        text_y5 = 713
        game_field.blit(text5, (text_x5, text_y5))

        text6 = font.render("3", True, (0, 0, 0))
        text_x6 = 266
        text_y6 = 713
        game_field.blit(text6, (text_x6, text_y6))

        text7 = font.render("1", True, (0, 0, 0))
        text_x7 = 186
        text_y7 = 713
        game_field.blit(text7, (text_x7, text_y7))

        text8 = font.render("2", True, (0, 0, 0))
        text_x8 = 226
        text_y8 = 713
        game_field.blit(text8, (text_x8, text_y8))

        text9 = font.render("2", True, (0, 0, 0))
        text_x9 = 226
        text_y9 = 333
        game_field.blit(text9, (text_x9, text_y9))

        text10 = font.render("3", True, (0, 0, 0))
        text_x10 = 266
        text_y10 = 333
        game_field.blit(text10, (text_x10, text_y10))

        text11 = font.render("1", True, (0, 0, 0))
        text_x11 = 184
        text_y11 = 333
        game_field.blit(text11, (text_x11, text_y11))

        text12 = font.render("4", True, (0, 0, 0))
        text_x12 = 306
        text_y12 = 333
        game_field.blit(text12, (text_x12, text_y12))

        text13 = font.render("3", True, (0, 0, 0))
        text_x13 = 956
        text_y13 = 333
        game_field.blit(text13, (text_x13, text_y13))

        text14 = font.render("2", True, (0, 0, 0))
        text_x14 = 916
        text_y14 = 333
        game_field.blit(text14, (text_x14, text_y14))

        text15 = font.render("1", True, (0, 0, 0))
        text_x15 = 876
        text_y15 = 333
        game_field.blit(text15, (text_x15, text_y15))

        text16 = font.render("4", True, (0, 0, 0))
        text_x16 = 306
        text_y16 = 713
        game_field.blit(text16, (text_x16, text_y16))

        fontes = pygame.font.Font(None, 30)
        text16 = fontes.render("Под каким номером находится зима", True, (0, 0, 0))
        text_x16 = 70
        text_y16 = 413
        game_field.blit(text16, (text_x16, text_y16))

        text19 = fontes.render("Под каким номером синий цвет", True, (0, 0, 0))
        text_x19 = 780
        text_y19 = 413
        game_field.blit(text19, (text_x19, text_y19))

        text20 = fontes.render("Под каким номером находится птица", True, (0, 0, 0))
        text_x20 = 60
        text_y20 = 30
        game_field.blit(text20, (text_x20, text_y20))

        text21 = fontes.render("Под каким номером воздушный транспорт", True, (0, 0, 0))
        text_x21 = 720
        text_y21 = 30
        game_field.blit(text21, (text_x21, text_y21))

        fonts = pygame.font.Font(None, 40)
        text17 = fonts.render("ВЫБЕРИ ВЕРНЫЙ ОТВЕТ", True, (100, 100, 100))
        text_x17 = 426
        text_y17 = 713
        game_field.blit(text17, (text_x17, text_y17))

        font = pygame.font.Font(None, 50)
        txt = font.render("1", True, (0, 0, 0))
        txt_x = 83
        txt_y = 63
        game_field.blit(txt, (txt_x, txt_y))

        txt2 = font.render("3", True, (0, 0, 0))
        txt_x2 = 83
        txt_y2 = 183
        game_field.blit(txt2, (txt_x2, txt_y2))

        txt3 = font.render("2", True, (0, 0, 0))
        txt_x3 = 283
        txt_y3 = 63
        game_field.blit(txt3, (txt_x3, txt_y3))

        txt3 = font.render("4", True, (0, 0, 0))
        txt_x3 = 283
        txt_y3 = 183
        game_field.blit(txt3, (txt_x3, txt_y3))

        txt4 = font.render("1", True, (0, 0, 0))
        txt_x4 = 53
        txt_y4 = 450
        game_field.blit(txt4, (txt_x4, txt_y4))

        txt5 = font.render("1", True, (0, 0, 0))
        txt_x5 = 53
        txt_y5 = 450
        game_field.blit(txt5, (txt_x5, txt_y5))

        txt6 = font.render("3", True, (0, 0, 0))
        txt_x6 = 53
        txt_y6 = 580
        game_field.blit(txt6, (txt_x6, txt_y6))

        txt7 = font.render("2", True, (0, 0, 0))
        txt_x7 = 273
        txt_y7 = 450
        game_field.blit(txt7, (txt_x7, txt_y7))

        txt8 = font.render("4", True, (0, 0, 0))
        txt_x8 = 273
        txt_y8 = 580
        game_field.blit(txt8, (txt_x8, txt_y8))

        txt9 = font.render("1", True, (0, 0, 0))
        txt_x9 = 743
        txt_y9 = 63
        game_field.blit(txt9, (txt_x9, txt_y9))

        txt10 = font.render("3", True, (0, 0, 0))
        txt_x10 = 743
        txt_y10 = 183
        game_field.blit(txt10, (txt_x10, txt_y10))

        txt11 = font.render("2", True, (0, 0, 0))
        txt_x11 = 943
        txt_y11 = 63
        game_field.blit(txt11, (txt_x11, txt_y11))

        txt12 = font.render("4", True, (0, 0, 0))
        txt_x12 = 943
        txt_y12 = 183
        game_field.blit(txt12, (txt_x12, txt_y12))

        txt13 = font.render("1", True, (0, 0, 0))
        txt_x13 = 743
        txt_y13 = 450
        game_field.blit(txt13, (txt_x13, txt_y13))

        txt14 = font.render("2", True, (0, 0, 0))
        txt_x14 = 933
        txt_y14 = 450
        game_field.blit(txt14, (txt_x14, txt_y14))

        txt15 = font.render("3", True, (0, 0, 0))
        txt_x15 = 743
        txt_y15 = 580
        game_field.blit(txt15, (txt_x15, txt_y15))

        txt16 = font.render("4", True, (0, 0, 0))
        txt_x16 = 933
        txt_y16 = 580
        game_field.blit(txt16, (txt_x16, txt_y16))

        if cor_2x < mouse[0] < cor_2x + buttonn and cor_2y < mouse[1] < cor_2y + buttonm:
            if mouse_get[0] == 1:
                main2()
                pygame.time.delay(1000)
            pygame.draw.rect(game_field, colormouse, (cor_2x, cor_2y, buttonn, buttonm))

        if cor_3x < mouse[0] < cor_3x + buttonn and cor_3y < mouse[1] < cor_3y + buttonm:
            if mouse_get[0] == 1:
                main3()
                pygame.time.delay(1000)
            pygame.draw.rect(game_field, colormouse, (cor_3x, cor_3y, buttonn, buttonm))

        if cor_x < mouse[0] < cor_x + buttonn and cor_y < mouse[1] < cor_y + buttonm:
            if mouse_get[0] == 1:
                main4()
                pygame.time.delay(1000)
            pygame.draw.rect(game_field, colormouse, (cor_x, cor_y, buttonn, buttonm))

        if cor_4x < mouse[0] < cor_4x + buttonn and cor_4y < mouse[1] < cor_4y + buttonm:
            if mouse_get[0] == 1:
                main5()
                pygame.time.delay(1000)
            pygame.draw.rect(game_field, colormouse, (cor_4x, cor_4y, buttonn, buttonm))

        if cor_8x < mouse[0] < cor_8x + buttonn and cor_8y < mouse[1] < cor_8y + buttonm:
            if mouse_get[0] == 1:
                main6()
                pygame.time.delay(1000)
            pygame.draw.rect(game_field, colormouse, (cor_8x, cor_8y, buttonn, buttonm))

        if cor_7x < mouse[0] < cor_7x + buttonn and cor_7y < mouse[1] < cor_7y + buttonm:
            if mouse_get[0] == 1:
                main7()
                pygame.time.delay(1000)
            pygame.draw.rect(game_field, colormouse, (cor_7x, cor_7y, buttonn, buttonm))

        if cor_6x < mouse[0] < cor_6x + buttonn and cor_6y < mouse[1] < cor_6y + buttonm:
            if mouse_get[0] == 1:
                main8()
                pygame.time.delay(1000)
            pygame.draw.rect(game_field, colormouse, (cor_6x, cor_6y, buttonn, buttonm))

        if cor_5x < mouse[0] < cor_5x + buttonn and cor_5y < mouse[1] < cor_5y + buttonm:
            if mouse_get[0] == 1:
                main9()
                pygame.time.delay(1000)
            pygame.draw.rect(game_field, colormouse, (cor_5x, cor_5y, buttonn, buttonm))

        if cor_10x < mouse[0] < cor_10x + buttonn and cor_10y < mouse[1] < cor_10y + buttonm:
            if mouse_get[0] == 1:
                main10()
                pygame.time.delay(1000)
            pygame.draw.rect(game_field, colormouse, (cor_10x, cor_10y, buttonn, buttonm))

        if cor_11x < mouse[0] < cor_11x + buttonn and cor_11y < mouse[1] < cor_11y + buttonm:
            if mouse_get[0] == 1:
                main12()
                pygame.time.delay(1000)
            pygame.draw.rect(game_field, colormouse, (cor_11x, cor_11y, buttonn, buttonm))

        if cor_12x < mouse[0] < cor_12x + buttonn and cor_12y < mouse[1] < cor_12y + buttonm:
            if mouse_get[0] == 1:
                main13()
                pygame.time.delay(1000)
            pygame.draw.rect(game_field, colormouse, (cor_12x, cor_12y, buttonn, buttonm))

        if cor_9x < mouse[0] < cor_9x + buttonn and cor_9y < mouse[1] < cor_9y + buttonm:
            if mouse_get[0] == 1:
                main11()
                pygame.time.delay(1000)
            pygame.draw.rect(game_field, colormouse, (cor_9x, cor_9y, buttonn, buttonm))

        if cor_13x < mouse[0] < cor_13x + buttonn and cor_13y < mouse[1] < cor_13y + buttonm:
            if mouse_get[0] == 1:
                main14()
                pygame.time.delay(1000)
            pygame.draw.rect(game_field, colormouse, (cor_13x, cor_13y, buttonn, buttonm))

        if cor_14x < mouse[0] < cor_14x + buttonn and cor_14y < mouse[1] < cor_14y + buttonm:
            if mouse_get[0] == 1:
                main15()
                pygame.time.delay(1000)
            pygame.draw.rect(game_field, colormouse, (cor_14x, cor_14y, buttonn, buttonm))

        if cor_15x < mouse[0] < cor_15x + buttonn and cor_15y < mouse[1] < cor_15y + buttonm:
            if mouse_get[0] == 1:
                main16()
                pygame.time.delay(1000)
            pygame.draw.rect(game_field, colormouse, (cor_15x, cor_15y, buttonn, buttonm))

        if cor_16x < mouse[0] < cor_16x + buttonn and cor_16y < mouse[1] < cor_16y + buttonm:
            if mouse_get[0] == 1:
                main17()
                pygame.time.delay(1000)
            pygame.draw.rect(game_field, colormouse, (cor_16x, cor_16y, buttonn, buttonm))
        pygame.display.flip()


def main2():
    font1 = pygame.font.Font(None, 48)
    text1 = font1.render("2", True, (0, 0, 0))
    text_x_cor1 = 226
    text_y_cor1 = 333
    text_w1 = text1.get_width()
    text_h1 = text1.get_height()
    pygame.draw.rect(game_field, (255, 0, 0), (text_x_cor1 - 10, text_y_cor1 - 10, text_w1 + 20, text_h1 + 12), 6)


def main3():
    font2 = pygame.font.Font(None, 48)
    text2 = font2.render("3", True, (0, 0, 0))
    text_x_cor2 = 266
    text_y_cor2 = 333
    text_w2 = text2.get_width()
    text_h2 = text2.get_height()
    pygame.draw.rect(game_field, (0, 255, 0), (text_x_cor2 - 10, text_y_cor2 - 10, text_w2 + 20, text_h2 + 12), 6)
    pygame.draw.rect(game_field, (0, 255, 0), (392, 8, 100, 10))


def main4():
    font3 = pygame.font.Font(None, 48)
    text3 = font3.render("1", True, (0, 0, 0))
    text_x_cor3 = 186
    text_y_cor3 = 333
    text_w3 = text3.get_width()
    text_h3 = text3.get_height()
    pygame.draw.rect(game_field, (255, 0, 0), (text_x_cor3 - 10, text_y_cor3 - 10, text_w3 + 20, text_h3 + 12), 6)


def main5():
    font4 = pygame.font.Font(None, 48)
    text4 = font4.render("4", True, (0, 0, 0))
    text_x_cor4 = 306
    text_y_cor4 = 333
    text_w4 = text4.get_width()
    text_h4 = text4.get_height()
    pygame.draw.rect(game_field, (255, 0, 0), (text_x_cor4 - 10, text_y_cor4 - 10, text_w4 + 20, text_h4 + 12), 6)


def main6():
    font5 = pygame.font.Font(None, 48)
    text5 = font5.render("4", True, (0, 0, 0))
    text_x_cor5 = 996
    text_y_cor5 = 333
    text_w5 = text5.get_width()
    text_h5 = text5.get_height()
    pygame.draw.rect(game_field, (0, 255, 0), (text_x_cor5 - 10, text_y_cor5 - 10, text_w5 + 20, text_h5 + 12), 6)
    pygame.draw.rect(game_field, (0, 255, 0), (500, 8, 100, 10))


def main7():
    font6 = pygame.font.Font(None, 48)
    text6 = font6.render("3", True, (0, 0, 0))
    text_x_cor6 = 956
    text_y_cor6 = 333
    text_w6 = text6.get_width()
    text_h6 = text6.get_height()
    pygame.draw.rect(game_field, (255, 0, 0), (text_x_cor6 - 10, text_y_cor6 - 10, text_w6 + 20, text_h6 + 12), 6)


def main8():
    font7 = pygame.font.Font(None, 48)
    text7 = font7.render("2", True, (0, 0, 0))
    text_x_cor7 = 916
    text_y_cor7 = 333
    text_w7 = text7.get_width()
    text_h7 = text7.get_height()
    pygame.draw.rect(game_field, (255, 0, 0), (text_x_cor7 - 10, text_y_cor7 - 10, text_w7 + 20, text_h7 + 12), 6)


def main9():
    font8 = pygame.font.Font(None, 48)
    text8 = font8.render("1", True, (0, 0, 0))
    text_x_cor8 = 876
    text_y_cor8 = 333
    text_w7 = text8.get_width()
    text_h7 = text8.get_height()
    pygame.draw.rect(game_field, (255, 0, 0), (text_x_cor8 - 10, text_y_cor8 - 10, text_w7 + 20, text_h7 + 12), 6)


def main10():
    font9 = pygame.font.Font(None, 48)
    text9 = font9.render("2", True, (0, 0, 0))
    text_x_cor9 = 226
    text_y_cor9 = 713
    text_w8 = text9.get_width()
    text_h8 = text9.get_height()
    pygame.draw.rect(game_field, (255, 0, 0), (text_x_cor9 - 10, text_y_cor9 - 10, text_w8 + 20, text_h8 + 12), 6)


def main11():
    font10 = pygame.font.Font(None, 48)
    text10 = font10.render("1", True, (0, 0, 0))
    text_x_cor10 = 186
    text_y_cor10 = 713
    text_w9 = text10.get_width()
    text_h9 = text10.get_height()
    pygame.draw.rect(game_field, (0, 255, 0), (text_x_cor10 - 10, text_y_cor10 - 10, text_w9 + 20, text_h9 + 12), 6)
    pygame.draw.rect(game_field, (0, 255, 0), (608, 8, 100, 10))


def main12():
    font11 = pygame.font.Font(None, 48)
    text11 = font11.render("3", True, (0, 0, 0))
    text_x_cor11 = 266
    text_y_cor11 = 713
    text_w10 = text11.get_width()
    text_h10 = text11.get_height()
    pygame.draw.rect(game_field, (255, 0, 0), (text_x_cor11 - 10, text_y_cor11 - 10, text_w10 + 20, text_h10 + 12), 6)


def main13():
    font12 = pygame.font.Font(None, 48)
    text12 = font12.render("4", True, (0, 0, 0))
    text_x_cor12 = 306
    text_y_cor12 = 713
    text_w11 = text12.get_width()
    text_h11 = text12.get_height()
    pygame.draw.rect(game_field, (255, 0, 0), (text_x_cor12 - 10, text_y_cor12 - 10, text_w11 + 20, text_h11 + 12), 6)


def main14():
    font13 = pygame.font.Font(None, 48)
    text13 = font13.render("1", True, (0, 0, 0))
    text_x_cor13 = 876
    text_y_cor13 = 713
    text_w12 = text13.get_width()
    text_h12 = text13.get_height()
    pygame.draw.rect(game_field, (255, 0, 0), (text_x_cor13 - 10, text_y_cor13 - 10, text_w12 + 20, text_h12 + 12), 6)


def main15():
    font14 = pygame.font.Font(None, 48)
    text14 = font14.render("2", True, (0, 0, 0))
    text_x_cor14 = 916
    text_y_cor14 = 713
    text_w13 = text14.get_width()
    text_h13 = text14.get_height()
    pygame.draw.rect(game_field, (255, 0, 0), (text_x_cor14 - 10, text_y_cor14 - 10, text_w13 + 20, text_h13 + 12), 6)


def main16():
    font15 = pygame.font.Font(None, 48)
    text15 = font15.render("3", True, (0, 0, 0))
    text_x_cor15 = 956
    text_y_cor15 = 713
    text_w14 = text15.get_width()
    text_h14 = text15.get_height()
    pygame.draw.rect(game_field, (255, 0, 0), (text_x_cor15 - 10, text_y_cor15 - 10, text_w14 + 20, text_h14 + 12), 6)


def main17():
    font16 = pygame.font.Font(None, 48)
    text16 = font16.render("4", True, (0, 0, 0))
    text_x_cor16 = 996
    text_y_cor16 = 713
    text_w15 = text16.get_width()
    text_h15 = text16.get_height()
    pygame.draw.rect(game_field, (0, 255, 0), (text_x_cor16 - 10, text_y_cor16 - 10, text_w15 + 20, text_h15 + 12), 6)
    pygame.draw.rect(game_field, (0, 255, 0), (716, 8, 100, 10))


if __name__ == '__main__':
    game_main()
