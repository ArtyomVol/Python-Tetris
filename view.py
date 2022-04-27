from pygame import draw
from labels import Labels


class View:

    def __del__(self):
        pass

    @staticmethod
    def draw_field(field, figure, game_screen, dx=2, dy=2):
        square = figure.get_square()
        square_side_length = figure.get_square_side_length()
        for y, row in enumerate(field):
            for x, column in enumerate(row):
                if column:
                    square.x = x * square_side_length + dx
                    square.y = y * square_side_length + dy
                    draw.rect(game_screen, column, square)  # in column stored RGB

    @staticmethod
    def draw_figure(figure, game_screen, mov_x=0, mov_y=0, dx=2, dy=2):
        square = figure.get_square()
        square_side_length = figure.get_square_side_length()
        color = figure.get_color()
        for sqr in figure.get_squares_coordinates():
            square.x = sqr.x * square_side_length + dx + mov_x
            square.y = sqr.y * square_side_length + dy + mov_y
            draw.rect(game_screen, color, square)

    @staticmethod
    def draw_grid(game_screen, grid_color, grid, width=1):
        for square in grid:
            draw.rect(game_screen, grid_color, square, width)

    @staticmethod
    def draw_label(screen, label, x, y):
        screen.blit(label, [x, y])

    @staticmethod
    def game_labels_update(screen):
        label_score_x = 450
        label_score_y = 500
        label_score_str_x = 320
        label_score_str_y = 500
        label_record_str_x = 320
        label_record_str_y = 450
        label_record_x = 470
        label_record_y = 450

        View.draw_label(screen, Labels.label_score, label_score_x, label_score_y)
        View.draw_label(screen, Labels.label_score_str, label_score_str_x, label_score_str_y)
        View.draw_label(screen, Labels.label_record_str, label_record_str_x, label_record_str_y)
        View.draw_label(screen, Labels.label_record, label_record_x, label_record_y)
