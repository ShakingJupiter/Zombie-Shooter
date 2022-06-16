import pygame,sys

pygame.init()

WIDTH,HEIGHT = 800,800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Unnamed Project 1")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PLAYER_SPRITE = 
PLAYER = 

ZOMBIE_SPRITE = 
ZOMBIE = 

def main():

    while True:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        

        
        pygame.display.update()        

main()
