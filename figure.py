from pygame import Rect


class Figure:

    def __del__(self):
        pass

    def __init__(self, squares_coordinates, color, square_side_length=0, d_square_side_length=0, falling_speed=50):
        self.__squares_coordinates = squares_coordinates
        self.__square_side_length = square_side_length
        self.__color = color
        self.__square = Rect(0, 0, square_side_length - d_square_side_length, square_side_length - d_square_side_length)
        self.__time_without_falling = 0
        self.__falling_speed = falling_speed
        self.__normal_time_to_fall = 2000
        self.__time_to_fall = self.__normal_time_to_fall
        self.__speed_limit = 250

    def get_normal_time_to_fall(self):
        return self.__normal_time_to_fall

    def set_normal_time_to_fall(self, normal_time_to_fall):
        if isinstance(normal_time_to_fall, int) and normal_time_to_fall > 0:
            self.__normal_time_to_fall = normal_time_to_fall

    def get_time_to_fall(self):
        return self.__time_to_fall

    def set_time_to_fall(self, time_to_fall):
        if isinstance(time_to_fall, int) and time_to_fall > 0:
            self.__time_to_fall = time_to_fall

    def get_speed_limit(self):
        return self.__speed_limit

    def set_speed_limit(self, speed_limit):
        if isinstance(speed_limit, int) and speed_limit > 0:
            self.__speed_limit = speed_limit

    def get_falling_speed(self):
        return self.__falling_speed

    def set_falling_speed(self, falling_speed):
        if isinstance(falling_speed, int) and 0 < falling_speed <= self.__speed_limit:
            self.__falling_speed = falling_speed

    def get_time_without_falling(self):
        return self.__time_without_falling

    def set_time_without_falling(self, time_without_falling):
        if isinstance(time_without_falling, int) and time_without_falling >= 0:
            self.__time_without_falling = time_without_falling

    def get_square(self):
        return self.__square

    def set_square(self, square):
        if isinstance(square, Rect):
            self.__square = square

    def get_color(self):
        return self.__color

    def set_color(self, color):
        main_colors_count = 3
        f = True
        if isinstance(color, list) and len(color) == main_colors_count:
            for main_color in color:
                if not isinstance(main_color, int) or main_color < 0:
                    f = False
            if f:
                self.__color = color

    def get_square_side_length(self):
        return self.__square_side_length

    def set_square_side_length(self, square_side_length):
        if isinstance(square_side_length, int) and square_side_length > 0:
            self.__square_side_length = square_side_length

    def get_squares_coordinates(self):
        return self.__squares_coordinates

    def set_squares_coordinates(self, squares_coordinates):
        squares_count = 4
        f = True
        if isinstance(squares_coordinates, list) and len(squares_coordinates) == squares_count:
            for square in squares_coordinates:
                if not isinstance(square, Rect):
                    f = False
                if f:
                    self.__squares_coordinates = squares_coordinates
