class BordersCheck:

    @staticmethod
    def check_walls(squares_coordinates, game_screen_width):
        for sqr in squares_coordinates:
            if sqr.x < 0 or sqr.x > game_screen_width - 1:
                return False
        return True

    @staticmethod
    def check_bottom(squares_coordinates, game_screen_height):
        for sqr in squares_coordinates:
            if sqr.y > game_screen_height - 1:
                return False
        return True

    @staticmethod
    def check_roof(squares_coordinates):
        for sqr in squares_coordinates:
            if sqr.y < 0:
                return False
        return True

    @staticmethod
    def check_field(squares_coordinates, field):
        for sqr in squares_coordinates:
            if field[sqr.y][sqr.x]:
                return False
        return True
