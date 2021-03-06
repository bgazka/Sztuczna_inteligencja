import pygame
import map
import main_guy
import entity_manager

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (10, 123, 10)
blue = (0, 0, 100)
bg_color = white

window_width = 640
window_height = 320
FPS = 30

gameDisplay = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Sztuczna inteligencja')
clock = pygame.time.Clock()

entity_manager = entity_manager.Entity_manager()
mapa = map.Map()
mapa.load_from_file(entity_manager)

gameExit = False

test = pygame.Rect(332, 32, 32, 32)

while not gameExit: #game_loop
    for event in pygame.event.get(): #event_loop
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                main_guy.Main_guy.move_right()
            elif event.key == pygame.K_LEFT:
                main_guy.Main_guy.move_left()
            elif event.key == pygame.K_DOWN:
                main_guy.Main_guy.move_down()
            elif event.key == pygame.K_UP:
                main_guy.Main_guy.move_up()
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameExit = True


    gameDisplay.fill(bg_color)
    pygame.draw.rect(gameDisplay, red, test, 0)
    mapa.draw_map(gameDisplay, entity_manager)
    # entity_manager.render(gameDisplay, entity_manager)
    # mapa.Render(gameDisplay)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
quit()
