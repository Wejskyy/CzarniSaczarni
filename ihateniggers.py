import pygame
import random

def main():
    dlugoscWeza=1
    xApple=random.randint(0,9)*40+20
    yApple=random.randint(0,9)*40+20
    pygame.init()
    OknoGry=pygame.display.set_mode((400,400),0,32)
    run=True
    zmienna1=120
    zmienna2=120

    pozycjaWaz=[(zmienna1,zmienna2)]
    pozycjaWaz.append((160,120))
    while(run):
        pozycja=[1,2,3,5,7,"a","d"]
        print("Czarni:",pozycja)
        OknoGry.fill((0,0,0))
        pygame.time.delay(200)
        for wspolrzedne in pozycjaWaz[::-1]:
            x=wspolrzedne[0]
            wazShape=pygame.Rect((wspolrzedne[0],wspolrzedne[1]),(40,40))
            pygame.draw.rect(OknoGry,(255,192,203),wazShape)
            pygame.draw.circle(OknoGry,(0,255,0),(xApple,yApple),20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    zmienna2=zmienna2-40
                elif event.key == pygame.K_DOWN:
                    zmienna2=zmienna2+40
                elif event.key == pygame.K_LEFT:
                    zmienna1=zmienna1-40
                elif event.key == pygame.K_RIGHT:
                    zmienna1=zmienna1+40

        pozycjaWaz.append((zmienna1,zmienna2))
        if dlugoscWeza<len(pozycjaWaz):
            del pozycjaWaz[0]

        if zmienna1==xApple-20 and zmienna2==yApple-20:
            xApple=random.randint(0,9)*40+20
            yApple=random.randint(0,9)*40+20
            pygame.draw.circle(OknoGry,(255,255,0),(xApple,yApple),20)
            dlugoscWeza+=1
        if zmienna1>400:
            zmienna1=0
        if zmienna2>400:
            zmienna2=0
        if zmienna1<0:
            zmienna1=400
        if zmienna2<0:
            zmienna2=400
        pygame.display.update()

main()
