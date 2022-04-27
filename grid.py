class Grid:

    def __del__(self):
        pass

    def __init__(self, square_side_length=0, width=0, height=0, color_rgb=(0, 0, 0), representation=None):
        if representation is None:
            representation = []
        self.__square_side_length = square_side_length
        self.__width = width
        self.__height = height
        self.__color_rgb = color_rgb
        self.__representation = representation
        self.__need_to_update = False

    def get_square_side_length(self):
        return self.__square_side_length

    def set_square_side_length(self, square_side_length):
        if isinstance(square_side_length, int) and square_side_length > 0:
            self.__square_side_length = square_side_length
            self.__need_to_update = True

    def get_width(self):
        return self.__width

    def set_width(self, width):
        if isinstance(width, int) and width > 0:
            self.__width = width
            self.__need_to_update = True

    def get_height(self):
        return self.__height

    def set_height(self, height):
        if isinstance(height, int) and height > 0:
            self.__height = height
            self.__need_to_update = True

    def get_color_rgb(self):
        return self.__color_rgb

    def set_color_rgb(self, color_rgb):
        main_colors_count = 3
        f = True
        if isinstance(color_rgb, list) and len(color_rgb) == main_colors_count:
            for color in color_rgb:
                if not isinstance(color, int) or color < 0:
                    f = False
            if f:
                self.__color_rgb = color_rgb
                self.__need_to_update = True

    def get_representation(self):
        return self.__representation
