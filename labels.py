from pygame import Color
from fonts import Fonts


class Labels:
    label_menu_tetris = None
    label_score = None
    label_score_str = None
    label_record = None
    label_record_str = None
    label_total_record = None
    label_total_record_str = None

    @staticmethod
    def text_game_labels_initialization(color_score=Color("green"), color_record=Color("orange"),
                                        color_total_record=Color("yellow")):
        Labels.label_score_str = Fonts.small_font.render('Score:', True, color_score)
        Labels.label_record_str = Fonts.small_font.render('Record:', True, color_record)
        Labels.label_total_record_str = Fonts.small_font.render('Total record:', True, color_total_record)

    @staticmethod
    def menu_label_tetris_initialization(color=Color("Yellow")):
        Labels.label_menu_tetris = Fonts.large_font.render('TETRIS', True, color)

    @staticmethod
    def label_score_initialization(score="0", color=Color("white")):
        Labels.label_score = Fonts.small_font.render(str(score), True, color)

    @staticmethod
    def label_record_initialization(record="0", color=Color("white")):
        Labels.label_record = Fonts.small_font.render(str(record), True, color)

    @staticmethod
    def label_total_record_initialization(total_record="0", color=Color("white")):
        Labels.label_total_record = Fonts.small_font.render(str(total_record), True, color)
