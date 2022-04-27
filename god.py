from pygame import Rect
from random import randrange, choice
from grid import Grid
from figure import Figure


class God:

    @staticmethod
    def create_grid(square_side_length=0, grid_width=0, grid_height=0, grid_color_rgb=(0, 0, 0)):
        f = True
        grid = None
        if isinstance(square_side_length, int) and square_side_length > 0 and isinstance(grid_width, int) and \
                grid_width > 0 and isinstance(grid_height, int) and grid_height > 0 and \
                isinstance(grid_color_rgb,list):
            for color in grid_color_rgb:
                if not isinstance(color, int) or color < 0:
                    f = False
            if f:
                representation = [
                    Rect(square_side_length * x, square_side_length * y, square_side_length, square_side_length)
                    for x in range(grid_width) for y in range(grid_height)]
                grid = Grid(square_side_length, grid_width, grid_height, grid_color_rgb, representation)
        return grid

    @staticmethod
    def create_figure(game_screen_width, square_side_length, falling_speed=49):
        if isinstance(game_screen_width, int) and game_screen_width > 0 \
                and isinstance(square_side_length, int) and square_side_length > 0:
            figures_positions = [[[-1, -1], [-2, -1], [0, -1], [1, -1]],
                                 [[0, -1], [-1, -1], [0, 0], [-1, 0]],
                                 [[0, 0], [-1, -1], [0, -1], [0, 1]],
                                 [[0, 0], [0, -1], [-1, 1], [0, 1]],
                                 [[0, 0], [-1, -1], [-1, 0], [0, 1]],
                                 [[0, 0], [0, -1], [-1, 0], [-1, 1]],
                                 [[0, 0], [-1, 0], [0, -1], [0, 1]]]
            position = choice(figures_positions)
            center = game_screen_width // 2
            top_indent = 1
            width = 0
            height = 0
            squares_coordinates = [Rect(x + center, y + top_indent, width, height) for x, y in position]
            color = God.create_color()
            d_square_side_length = 4
            return Figure(squares_coordinates, color, square_side_length, d_square_side_length, falling_speed + 1)

    @staticmethod
    def create_color(begin=50, end=255):
        if isinstance(begin, int) and 0 <= begin < 255 and isinstance(end, int) and 0 < end <= 255:
            return [randrange(begin, end), randrange(begin, end), randrange(begin, end)]

    @staticmethod
    def create_field(game_screen_width, game_screen_height):
        field = [[0 for i in range(game_screen_width)] for j in range(game_screen_height)]
        return field
