import sys
import pygame
from power_up import PowerUp


def check_controller(warrior, configurations, screen, skills):
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #If the user press any arrow keys, set the moving_right, moving_left, moving_up or moving_down flag to True.
        elif event.type == pygame.KEYDOWN:
            check_event_key_down(event, warrior, configurations, screen, skills)

        elif event.type == pygame.KEYUP:
            check_event_key_up(event, warrior)


def check_event_key_down(event, configurations, screen, warrior, skills):
    if event.key == pygame.K_RIGHT:
        warrior.moving_right = True
    elif event.key == pygame.K_LEFT:
        warrior.moving_left = True
    elif event.key == pygame.K_UP:
        warrior.moving_up = True
    elif event.key == pygame.K_DOWN:
        warrior.moving_down = True
    elif event.key == pygame.K_SPACE:
        skill = PowerUp(event, configurations, screen, warrior, skills)
        skills.add(skill)


def check_event_key_up(event, warrior):
    if event.key == pygame.K_RIGHT:
        warrior.moving_right = False
    elif event.key == pygame.K_LEFT:
        warrior.moving_left = False
    elif event.key == pygame.K_UP:
        warrior.moving_up = False
    elif event.key == pygame.K_DOWN:
        warrior.moving_down = False


def updated_screen(configurations, screen, warrior, skills):
    # Update the screen during each pass through the loop.
    
    # Redraw the screen during each pass through the loop with the function bg_screen() with the warrior.bmp
    screen.fill(configurations.bg_screen)
    
    #Redraw the skills in the screen during each pass through the loop with the function blaster_skill()
    for skill in skills.sprites():
        skill.release_power_up()
    
    #Reiniciative the warrior.bmp in the screen during each pass through the loop with the function start_on_screen()
    warrior.start_on_screen()

    # Make the most recently drawn screen visible. 
    pygame.display.flip()
