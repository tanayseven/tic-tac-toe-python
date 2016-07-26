#!/usr/bin/env python3
def flatten_2d_list(lst):
    return [elem for row in lst for elem in row]


def total_matching_elements_in_lst(elements, lst):
    return sum(1 for lst_element in lst if lst_element in elements)


def get_main_diagonal(lst):
    return (lst[row][col] for row in range(len(lst)) for col in range(len(lst)) if row == col)


def get_secondary_diagonal(lst):
    return (lst[row][col] for row in range(len(lst)) for col in reversed(range(len(lst))) if row == len(lst)-col-1)


def get_row(lst, row_num):
    return lst[row_num]


def get_col(lst, col_num):
    return [row[col_num] for row in lst]


class Game:
    BLANK = 0
    PLAYER1 = 1
    PLAYER2 = 2
    MAX = 3

    def __init__(self):
        self.__board__ = [[Game.BLANK for _ in range(Game.MAX)] for _ in range(Game.MAX)]

    def are_total_moves_even(self):
        return total_matching_elements_in_lst({Game.PLAYER1, Game.PLAYER2}, flatten_2d_list(self.__board__)) % 2 == 0

    def turn(self):
        return Game.PLAYER1 if self.are_total_moves_even() else Game.PLAYER2

    def play(self, row, col):
        is_playable = self.__board__[row][col] == Game.BLANK and not self.is_over()
        if is_playable:
            self.__board__[row][col] = self.turn()
        return is_playable

    def player_winning_on_main_diagonal(self):
        main_diagonal = list(get_main_diagonal(self.__board__))
        return Game.PLAYER1 \
            if total_matching_elements_in_lst({Game.PLAYER1}, main_diagonal) == len(main_diagonal) \
            else Game.PLAYER2 if total_matching_elements_in_lst({Game.PLAYER2}, main_diagonal) == len(main_diagonal)\
            else None

    def player_winning_on_secondary_diagonal(self):
        diagonal = list(get_secondary_diagonal(self.__board__))
        return Game.PLAYER1 \
            if total_matching_elements_in_lst({Game.PLAYER1}, diagonal) == len(diagonal) \
            else Game.PLAYER2 if total_matching_elements_in_lst({Game.PLAYER2}, diagonal) == len(diagonal) \
            else None

    def player_winning_on_row(self):
        result_player = None
        for row in range(len(self.__board__)):
            if total_matching_elements_in_lst({Game.PLAYER1}, get_row(self.__board__, row)) == len(self.__board__):
                result_player = Game.PLAYER1
                break
            if total_matching_elements_in_lst({Game.PLAYER2}, get_row(self.__board__, row)) == len(self.__board__):
                result_player = Game.PLAYER2
                break
        return result_player

    def player_winning_on_column(self):
        result_player = None
        for col in range(len(self.__board__)):
            if total_matching_elements_in_lst({Game.PLAYER1}, get_col(self.__board__, col)) == len(self.__board__):
                result_player = Game.PLAYER1
                break
            if total_matching_elements_in_lst({Game.PLAYER2}, get_col(self.__board__, col)) == len(self.__board__):
                result_player = Game.PLAYER2
                break
        return result_player

    def winner(self):
        return self.player_winning_on_main_diagonal() or \
            self.player_winning_on_secondary_diagonal() or \
            self.player_winning_on_row() or \
            self.player_winning_on_column()

    def is_board_full(self):
        return Game.BLANK not in flatten_2d_list(self.__board__)

    def is_over(self):
        return self.winner() is not None or self.is_board_full()
