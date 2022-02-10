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
       wazShape=pygame.Rect((140,140),(47,47))
       wazShape=pygame.Rect((zmienna1,zmienna2),(47,47))
       pygame.draw.rect(OknoGry,(255,192,203),wazShape)
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               run=False
           #ruch weza
           elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_UP:
                   zmienna2=zmienna2-20
               elif event.key == pygame.K_DOWN:
                   zmienna2=zmienna2+20
       #zmienna1=zmienna1+20
       #zmienna2=zmienna2+20
       if zmienna1>400:
           zmienna1=0
       if zmienna2>400:
           zmienna2=0
       pygame.display.update()

main()  
