import pygame
from manager import Manager
from view import View
from god import God
from eventsCheck import EventsCheck
from figureActions import FigureActions
from labels import Labels


class GameStates:

    @staticmethod
    def menu_open(screen):
        back_ground = pygame.image.load('img/main_bg.png').convert()

        png_button_play = pygame.image.load('img/play.png')
        button_play = png_button_play.get_rect()
        button_play.x = 186
        button_play.y = 250

        png_button_exit = pygame.image.load('img/exit.png')
        button_exit = png_button_exit.get_rect()
        button_exit.x = 186
        button_exit.y = 400

        label_menu_tetris_color = [255, 255, 0]
        Labels.menu_label_tetris_initialization(label_menu_tetris_color)

        clock = pygame.time.Clock()
        fps = 60

        flag = 0
        while flag != 2:
            screen.blit(back_ground, (0, 0))
            screen.blit(png_button_play, button_play)
            screen.blit(png_button_exit, button_exit)
            label_menu_tetris_color = Manager.change_color_smooth(label_menu_tetris_color)
            Labels.menu_label_tetris_initialization(label_menu_tetris_color)
            View.draw_label(screen, Labels.label_menu_tetris, 60, 50)
            flag = EventsCheck.menu_event_check(button_play, button_exit)
            pygame.display.update()
            clock.tick(fps)
            if flag == 1:
                GameStates.game_open(screen)
        Manager.file_total_record.close()

    @staticmethod
    def pause(screen, game_continue=False):
        pause_back_ground = pygame.image.load('img/pause menu.png')
        pause_coordinates = [25, 160]

        png_button_restart = pygame.image.load('img/restart.png')
        button_restart = png_button_restart.get_rect()
        button_restart.x = 75
        button_restart.y = 200

        png_button_menu = pygame.image.load('img/menu.png')
        button_menu = png_button_menu.get_rect()
        button_menu.x = 75
        button_menu.y = 315

        png_button_continue = pygame.image.load('img/continue.png')
        button_continue = png_button_continue.get_rect()
        button_continue.x = 315
        button_continue.y = 200

        label_total_record_str_x = 295
        label_total_record_str_y = 330
        Labels.label_total_record_initialization(str(Manager.total_record))
        label_total_record_x = 295
        label_total_record_y = 370

        screen.blit(pause_back_ground, pause_coordinates)
        screen.blit(png_button_restart, button_restart)
        screen.blit(png_button_menu, button_menu)
        if game_continue:
            screen.blit(png_button_continue, button_continue)
        View.draw_label(screen, Labels.label_total_record_str, label_total_record_str_x, label_total_record_str_y)
        View.draw_label(screen, Labels.label_total_record, label_total_record_x, label_total_record_y)

        clock = pygame.time.Clock()
        fps = 60
        game_flag = 0
        pause_flag = True
        while pause_flag:
            flag = EventsCheck.pause_event_check(button_restart, button_menu, button_continue)
            if flag == 1:  # restart
                if game_continue:
                    Manager.score_redefinition()
                game_flag = 2
                pause_flag = False
            elif flag == 2:  # menu
                Manager.score_redefinition()
                pygame.mixer.music.pause()
                pause_flag = False
            elif flag == 3 and game_continue:  # continue
                game_flag = 1
                pause_flag = False
            pygame.display.flip()
            clock.tick(fps)
        return game_flag

    @staticmethod
    def game_open(screen):
        square_side_length = 30

        game_screen_height = 20
        game_screen_width = 10
        game_screen_size = game_screen_width * square_side_length, game_screen_height * square_side_length

        grid_color = [0, 0, 0]
        grid = God.create_grid(square_side_length, game_screen_width, game_screen_height, grid_color)
        figure, next_figure = [God.create_figure(game_screen_width, square_side_length),
                               God.create_figure(game_screen_width, square_side_length)]
        field = God.create_field(game_screen_width, game_screen_height)
        game_screen = pygame.Surface(game_screen_size)
        game_back_ground = pygame.image.load('img/bg.png').convert()
        back_ground = pygame.image.load('img/main_bg.png').convert()
        next_figure_back_ground = pygame.image.load('img/next figure bg.png')
        next_figure_x = 300
        next_figure_y = 100

        Labels.label_record_initialization(str(Manager.record))
        Labels.label_score_initialization(str(Manager.score))

        png_button_pause = pygame.image.load('img/pause button.png')
        button_pause = png_button_pause.get_rect()
        button_pause.x = 540
        button_pause.y = 10

        png_button_music_on = pygame.image.load('img/music on button.png')
        png_button_music_off = pygame.image.load('img/music off button.png')
        button_music = png_button_music_on.get_rect()
        button_music.x = 480
        button_music.y = 10

        flag_game_continue = True

        if Manager.music_on:
            pygame.mixer.music.play()

        clock = pygame.time.Clock()
        fps = 60
        flag = True
        while flag:
            screen.blit(back_ground, (0, 0))
            screen.blit(game_screen, (10, 10))
            screen.blit(next_figure_back_ground, (375, 70))
            screen.blit(png_button_pause, button_pause)
            if Manager.music_on:
                screen.blit(png_button_music_on, button_music)
            else:
                screen.blit(png_button_music_off, button_music)
            game_screen.blit(game_back_ground, (0, 0))
            View.draw_grid(game_screen, grid.get_color_rgb(), grid.get_representation())
            View.draw_figure(figure, game_screen)
            View.draw_figure(next_figure, screen, next_figure_x, next_figure_y)
            View.draw_field(field, figure, game_screen)
            View.game_labels_update(screen)

            field = Manager.check_lines_for_filling(field, game_screen_width, figure, game_screen)
            figure, flag_pause = EventsCheck.game_event_check(game_screen_width, game_screen_height, field, figure,
                                                              button_pause, button_music)
            figure, next_figure = FigureActions.figure_move_y(figure, next_figure, game_screen_width,
                                                              game_screen_height,
                                                              field)

            for column in field[0]:
                if column:
                    Manager.game_over(field, screen, game_screen, game_screen_height, game_screen_width, figure)
                    flag_pause = True
                    flag_game_continue = False
                    break

            if flag_pause:
                flag = GameStates.pause(screen, flag_game_continue)
                if flag == 2:
                    figure, next_figure = [God.create_figure(game_screen_width, square_side_length),
                                           God.create_figure(game_screen_width, square_side_length)]
                    field = God.create_field(game_screen_width, game_screen_height)
                    flag_game_continue = True
            pygame.display.flip()
            clock.tick(fps)
