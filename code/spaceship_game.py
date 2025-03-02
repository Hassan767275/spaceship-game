import pygame

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Spaceship Game")
running = True

#create a surface to put on display surface
surface = pygame.Surface((100, 200))
surface.fill("pink")
x = 100

#importing an image
player_surface = pygame.image.load("images/player.png")

while running:
    #event loop
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #draw the game
    # fill window with red color
    display_surface.fill("lightslateblue")
    x += 0.1
    display_surface.blit(surface, (x, 150))
    pygame.display.update()
pygame.quit()