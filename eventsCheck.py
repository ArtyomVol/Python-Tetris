import pygame
from manager import Manager
from figureActions import FigureActions


class EventsCheck:

    @staticmethod
    def pause_event_check(button_restart, button_menu, button_continue):
        flag = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Manager.file_total_record.close()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_p or event.key == pygame.K_c:
                    flag = 3
                elif event.key == pygame.K_r:
                    flag = 1
                elif event.key == pygame.K_m:
                    flag = 2
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button_restart.collidepoint(mouse_pos):
                    flag = 1
                elif button_menu.collidepoint(mouse_pos):
                    flag = 2
                elif button_continue.collidepoint(mouse_pos):
                    flag = 3
        return flag

    @staticmethod
    def game_event_check(game_screen_width, game_screen_height, field, figure, button_pause, button_music):
        flag_pause = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Manager.file_total_record.close()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                    flag_pause = True
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    move_x = -1
                    figure = FigureActions.figure_move_x(figure, move_x, game_screen_width, field)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    move_x = 1
                    figure = FigureActions.figure_move_x(figure, move_x, game_screen_width, field)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    figure.set_time_to_fall(figure.get_falling_speed())
                elif event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_w:
                    figure = FigureActions.figure_rotate(figure, game_screen_width, game_screen_height, field)
                elif event.key == pygame.K_m:
                    Manager.music_on = not Manager.music_on
                    if Manager.music_on:
                        pygame.mixer.music.play()
                    else:
                        pygame.mixer.music.pause()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button_pause.collidepoint(mouse_pos):
                    flag_pause = True
                elif button_music.collidepoint(mouse_pos):
                    Manager.music_on = not Manager.music_on
                    if Manager.music_on:
                        pygame.mixer.music.play()
                    else:
                        pygame.mixer.music.pause()
        return figure, flag_pause

    @staticmethod
    def menu_event_check(button_play, button_exit):
        flag = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = 2
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    flag = 1
                elif event.key == pygame.K_e:
                    flag = 2
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button_play.collidepoint(mouse_pos):
                    flag = 1
                elif button_exit.collidepoint(mouse_pos):
                    flag = 2
        return flag
