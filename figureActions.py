from copy import deepcopy
from god import God
from bordersCheck import BordersCheck


class FigureActions:

    @staticmethod
    def figure_rotate(figure, game_screen_width, game_screen_height, field):
        square_count = 4
        squares_coordinates = deepcopy(figure.get_squares_coordinates())
        center = squares_coordinates[0]
        for i in range(square_count):
            dx = squares_coordinates[i].y - center.y
            dy = squares_coordinates[i].x - center.x
            squares_coordinates[i].x = center.x - dx
            squares_coordinates[i].y = center.y + dy
            if not BordersCheck.check_walls(squares_coordinates, game_screen_width) or \
                    not BordersCheck.check_bottom(squares_coordinates, game_screen_height, ) or \
                    not BordersCheck.check_roof(squares_coordinates) or \
                    not BordersCheck.check_field(squares_coordinates, field):
                return figure
        figure.set_squares_coordinates(squares_coordinates)
        return figure

    @staticmethod
    def figure_move_x(figure, move_x, game_screen_width, field):
        figure_copy = deepcopy(figure)
        for sqr in figure.get_squares_coordinates():
            sqr.x += move_x
            if not BordersCheck.check_walls(figure.get_squares_coordinates(), game_screen_width) or \
                    not BordersCheck.check_field(figure.get_squares_coordinates(), field):
                return figure_copy
        return figure

    @staticmethod
    def figure_move_y(figure, next_figure, game_screen_width, game_screen_height, field, move_y=1):
        figure_copy = deepcopy(figure)
        figure.set_time_without_falling(figure.get_time_without_falling() + figure.get_falling_speed())
        if figure.get_time_without_falling() > figure.get_time_to_fall():
            for sqr in figure.get_squares_coordinates():
                sqr.y += move_y
            figure.set_time_without_falling(0)
            if not BordersCheck.check_bottom(figure.get_squares_coordinates(), game_screen_height) or \
                    not BordersCheck.check_field(figure.get_squares_coordinates(), field):
                for sqr in figure_copy.get_squares_coordinates():
                    field[sqr.y][sqr.x] = figure.get_color()
                figure = next_figure
                next_figure = God.create_figure(game_screen_width, figure.get_square_side_length(),
                                                figure.get_falling_speed())
        return figure, next_figure
