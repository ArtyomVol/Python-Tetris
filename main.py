import pygame
from gameStates import GameStates
from fonts import Fonts
from labels import Labels


def main():
    pygame.init()
    screen_rez = 600, 620
    screen = pygame.display.set_mode(screen_rez)
    application_name = "Tetris"
    pygame.display.set_caption(application_name)
    icon = pygame.image.load('img/icon.png')
    pygame.display.set_icon(icon)
    pygame.mixer.music.load('songs/back song.mp3')
    Fonts.fonts_initialization()
    Labels.text_game_labels_initialization()
    GameStates.menu_open(screen)
    pygame.quit()


if __name__ == '__main__':
    main()
