import pygame
import random


def main():
    dlugoszWeza = 1
    punkty = 0
    xApple = random.randint(0, 9) * 40 + 20
    yApple = random.randint(0, 9) * 40 + 20
    pygame.init()
    OknoGry = pygame.display.set_mode((400, 400), 0, 32)
    run = True
    zmienna1 = 120
    zmienna2 = 120
    # przypisanie pierwszej pozycji węża
    pozycjaWaz = [(zmienna1, zmienna2)]
    # pozycjaWaz.append((160,120))
    while (run):
        OknoGry.fill((0, 0, 0))
        pygame.time.delay(200)
        # rysowanie weza

        for wspolrzendne in pozycjaWaz[::-1]:
            wazShape = pygame.Rect((wspolrzendne[0], wspolrzendne[1]), (40, 40))
            pygame.draw.rect(OknoGry, (255, 192, 203), wazShape)
            # rysowanie jabłka
        pygame.draw.circle(OknoGry, (0, 255, 0), (xApple, yApple), 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # ruch weza
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    zmienna2 = zmienna2 - 40
                elif event.key == pygame.K_DOWN:
                    zmienna2 = zmienna2 + 40
                elif event.key == pygame.K_LEFT:
                    zmienna1 = zmienna1 - 40
                elif event.key == pygame.K_RIGHT:
                    zmienna1 = zmienna1 + 40

                # sprawdzenie czy wąż sam siebie nie zjadł
                for wspol in pozycjaWaz[::]:
                    if zmienna1 == wspol[0] and zmienna2 == wspol[1]:
                        pozycjaWaz = []
                        dlugoszWeza = 1
                        punkty=0
                # dodawanie nowej pozycji węża
                pozycjaWaz.append((zmienna1, zmienna2))
                if dlugoszWeza < len(pozycjaWaz):
                    del pozycjaWaz[0]

        # waż zjada jabłko
        if zmienna1 == xApple - 20 and zmienna2 == yApple - 20:
            xApple = random.randint(0, 9) * 40 + 20
            yApple = random.randint(0, 9) * 40 + 20
            pygame.draw.circle(OknoGry, (255, 255, 0), (xApple, yApple), 20)
            dlugoszWeza += 1
            punkty+=1
        # zmienna1=zmienna1+20
        # zmienna2=zmienna2+20
        # przejście strona prawa
        if zmienna1 > 400:
            zmienna1 = 0
            # przejście dół
        if zmienna2 > 400:
            zmienna2 = 0
        # przejście strona lewa
        if zmienna1 < 0:
            zmienna1 = 400
            # przejście góra
        if zmienna2 < 0:
            zmienna2 = 400
        czcionka=pygame.font.SysFont('comicsans',20)
        tekst=czcionka.render("Punkty: {0}".format(punkty),1,(255,255,255))
        OknoGry.blit(tekst,(10,10))

        pygame.display.update()

main()
