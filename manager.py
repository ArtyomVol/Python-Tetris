import pygame
from copy import deepcopy
from random import randrange
from grid import Grid
from god import God
from view import View
from labels import Labels


class Manager:
    file_total_record = open('data/total record.txt', 'r+')
    score = 0
    record = 0
    total_record = int(file_total_record.readline())
    music_on = True

    @staticmethod
    def update_grid_representation(grid):
        square_side_length = grid.get_square_side_length()
        width = grid.get_width()
        height = grid.get_height()
        representation = [
            pygame.Rect(square_side_length * x, square_side_length * y, square_side_length, square_side_length)
            for x in range(width) for y in range(height)]
        return Grid(square_side_length, width, height, grid.get_color_rgb(), representation)

    @staticmethod
    def del_filled_rows(field, filled_row_count, game_screen_width):
        msg = "del"
        new_field = []
        zero_row = [0 for i in range(game_screen_width)]
        for row in field:
            if row[0] != msg:
                new_field.append(row)
        for i in range(filled_row_count):
            new_field = [deepcopy(zero_row)] + new_field
        return new_field

    @staticmethod
    def score_up(filled_row_count, score):
        points_for_one_line = 100
        points_for_two_lines = 300
        points_for_three_line = 700
        points_for_four_line = 1500
        if filled_row_count == 1:
            return score + points_for_one_line
        elif filled_row_count == 2:
            return score + points_for_two_lines
        elif filled_row_count == 3:
            return score + points_for_three_line
        # for protection from error (5,6..., -1.0...) not "else"
        elif filled_row_count == 4:
            return score + points_for_four_line

    @staticmethod
    def check_lines_for_filling(field, game_screen_width, figure, game_screen):
        msg = "del"
        filled_row_count = 0
        for y, row in enumerate(field):
            filled_row = True
            for column in row:
                if not column:
                    filled_row = False
            if filled_row:
                filled_row_count += 1
                row[0] = msg
        if filled_row_count:
            field = Manager.del_filled_rows(field, filled_row_count, game_screen_width)
            Manager.score = Manager.score_up(filled_row_count, Manager.score)
            View.draw_field(field, figure, game_screen)
        Labels.label_score_initialization(str(Manager.score))
        return field

    @staticmethod
    def game_over(field, screen, game_screen, game_screen_height, game_screen_width, figure):
        Manager.score_redefinition()
        Manager.ending_of_game(field, game_screen, screen, game_screen_height, game_screen_width, figure)

    @staticmethod
    def score_redefinition():
        if Manager.score > Manager.record:
            Manager.record = Manager.score
            Labels.label_record_initialization(str(Manager.record))
            if Manager.record > Manager.total_record:
                Manager.total_record = Manager.record
                Labels.label_total_record_initialization(str(Manager.record))
                Manager.file_total_record.seek(0)
                Manager.file_total_record.write(str(Manager.total_record))
                Manager.file_total_record.flush()
        Manager.score = 0

    @staticmethod
    def ending_of_game(field, game_screen, screen, game_screen_height, game_screen_width, figure):
        clock = pygame.time.Clock()
        fps = 250
        game_screen_x = game_screen_y = 10
        for i in range(game_screen_height):
            j = 0
            while i >= 0 and j < game_screen_width:
                field[i][j] = God.create_color()
                View.draw_field(field, figure, game_screen)
                screen.blit(game_screen, (game_screen_x, game_screen_y))
                j += 1
                i -= 1
                pygame.display.flip()
                clock.tick(fps)
        for j in range(game_screen_width):
            i = game_screen_height - 1
            while j < game_screen_width:
                field[i][j] = God.create_color()
                View.draw_field(field, figure, game_screen)
                screen.blit(game_screen, (game_screen_x, game_screen_y))
                j += 1
                i -= 1
                pygame.display.flip()
                clock.tick(fps)

    @staticmethod
    def change_color_smooth(color, beg=0, end=255):
        i = randrange(0, 3)
        operation = randrange(0, 2)
        add = 5
        if color[i] < end - add:
            if operation or color[i] <= beg + add:
                color[i] += add
            else:
                color[i] -= add
        else:
            color[i] -= add
        return color
