import pygame
def main():
   pygame.init()
   OknoGry=pygame.display.set_mode((400,400),0,32)
   run=True
   zmienna1=140
   zmienna2=140
   while(run):
       OknoGry.fill((0,0,0))
       pygame.time.delay(200)
       wazShape=pygame.Rect((zmienna1,zmienna2),(47,47))
       wazShape=pygame.Rect((zmienna1,zmienna2),(40,40))
       pygame.draw.rect(OknoGry,(255,192,203),wazShape)
       pygame.draw.circle(OknoGry,(0,255,0),(100,100),20)
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               run=False
           elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_UP:
                   zmienna2=zmienna2-20
               elif event.key == pygame.K_DOWN:
                   zmienna2=zmienna2+20
               elif event.key == pygame.K_LEFT:
                   zmienna1=zmienna1-20
               elif event.key == pygame.K_RIGHT:
                   zmienna1=zmienna1+20
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
