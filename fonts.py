from pygame import font


class Fonts:
    small_font = None
    big_font = None
    large_font = None

    @staticmethod
    def fonts_initialization(address_small='font/font2.ttf', size_small=30, address_big='font/font3.ttf',
                             size_big=65, address_large='font/font3.ttf', size_large=150):
        Fonts.small_font = font.Font(address_small, size_small)
        Fonts.big_font = font.Font(address_big, size_big)
        Fonts.large_font = font.Font(address_large, size_large)
