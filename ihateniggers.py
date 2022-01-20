import pygame

def main():
    pygame.init()
    OknoGry=pygame.display.set_mode((400,400),0,32)
    run=True
    while(run):
        pygame.time.delay(200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False

main()