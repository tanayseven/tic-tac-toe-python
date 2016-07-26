import unittest

from TicTacToe import Game


class GameTest(unittest.TestCase):

    def test_it_should_be_player1_turn__when_the_game_starts(self):
        game = Game()

        turn = game.turn()

        self.assertEquals(turn, Game.PLAYER1)

    def test_it_should_be_player2_turn__when_player1_plays(self):
        game = Game()

        game.play(0, 0)
        turn = game.turn()

        self.assertEquals(turn, Game.PLAYER2)

    def test_it_should_be_player1_turn_when_player2_plays(self):
        game = Game()

        game.play(0, 0)
        game.play(1, 1)
        turn = game.turn()

        self.assertEquals(turn, Game.PLAYER1)

    def test_player1_should_not_be_able_to_play__when_the_location_is_used_by_player1(self):
        game = Game()

        game.play(0, 0)
        game.play(1, 1)
        success = game.play(0, 0)

        self.assertFalse(success)

    def test_player1_should_not_be_able_to_play__when_the_location_is_used_by_player2(self):
        game = Game()

        game.play(0, 0)
        game.play(1, 1)
        success = game.play(1, 1)

        self.assertFalse(success)

    def test_player2_should_not_be_able_to_play__when_the_location_is_used_by_player1(self):
        game = Game()

        game.play(1, 0)
        success = game.play(1, 0)

        self.assertFalse(success)

    def test_player2_should_not_be_able_to_play__when_the_location_is_used_by_player2(self):
        game = Game()

        game.play(1, 0)
        game.play(1, 1)
        game.play(0, 0)
        success = game.play(1, 1)

        self.assertFalse(success)

    def test_player1_should_win__when_main_diagonal_is_full_with_player1_moves(self):
        game = Game()

        game.play(0, 0)
        game.play(0, 1)
        game.play(1, 1)
        game.play(1, 2)
        game.play(2, 2)
        winner = game.winner()

        self.assertEquals(winner, Game.PLAYER1)

    def test_player2_should_win__when_main_diagonal_is_full_with_player1_moves(self):
        game = Game()

        game.play(0, 1)
        game.play(0, 0)
        game.play(0, 2)
        game.play(1, 1)
        game.play(2, 0)
        game.play(2, 2)
        winner = game.winner()

        self.assertEquals(winner, Game.PLAYER2)

    def test_player1_should_win__when_secondary_diagonal_is_full_with_player1_moves(self):
        game = Game()

        game.play(0, 2)
        game.play(0, 1)
        game.play(1, 1)
        game.play(0, 0)
        game.play(2, 0)
        winner = game.winner()

        self.assertEquals(winner, Game.PLAYER1)

    def test_player2_should_win__when_secondary_diagonal_is_full_with_player2_moves(self):
        game = Game()

        game.play(0, 0)
        game.play(0, 2)
        game.play(0, 1)
        game.play(1, 1)
        game.play(1, 0)
        game.play(2, 0)
        winner = game.winner()

        self.assertEquals(winner, Game.PLAYER2)

    def test_player1_should_win__when_the_1st_row_is_full_with_player1_moves(self):
        game = Game()

        game.play(0, 0)
        game.play(1, 0)
        game.play(0, 1)
        game.play(2, 0)
        game.play(0, 2)
        winner = game.winner()

        self.assertEquals(winner, Game.PLAYER1)

    def test_player1_should_win__when_the_2nd_row_is_full_with_player1_moves(self):
        game = Game()

        game.play(1, 0)
        game.play(0, 0)
        game.play(1, 1)
        game.play(0, 1)
        game.play(1, 2)
        winner = game.winner()

        self.assertEquals(winner, Game.PLAYER1)

    def test_player1_should_win__when_the_3rd_row_is_full_with_player1_moves(self):
        game = Game()

        game.play(2, 0)
        game.play(0, 0)
        game.play(2, 1)
        game.play(0, 1)
        game.play(2, 2)
        winner = game.winner()

        self.assertEquals(winner, Game.PLAYER1)

    def test_player2_should_win__when_the_1st_row_is_full_with_player2_moves(self):
        game = Game()

        game.play(1, 0)
        game.play(0, 0)
        game.play(1, 1)
        game.play(0, 1)
        game.play(2, 0)
        game.play(0, 2)
        winner = game.winner()

        self.assertEquals(winner, Game.PLAYER2)

    def test_player2_should_win__when_the_2nd_row_is_full_with_player2_moves(self):
        game = Game()

        game.play(0, 0)
        game.play(1, 0)
        game.play(0, 1)
        game.play(1, 1)
        game.play(2, 0)
        game.play(1, 2)
        winner = game.winner()

        self.assertEquals(winner, Game.PLAYER2)

    def test_player2_wins__when_3rd_row_is_full_with_player2_moves(self):
        game = Game()

        game.play(1, 0)
        game.play(0, 0)
        game.play(1, 1)
        game.play(0, 1)
        game.play(2, 0)
        game.play(0, 2)
        winner = game.winner()

        self.assertEquals(winner, Game.PLAYER2)

    def test_player1_should_win__when_the_1st_column_is_full_with_player1_moves(self):
        game = Game()

        game.play(0, 0)
        game.play(0, 1)
        game.play(1, 0)
        game.play(0, 2)
        game.play(2, 0)
        winner = game.winner()

        self.assertEquals(winner, Game.PLAYER1)

    def test_player1_should_win__when_the_2nd_column_is_full_with_player1_moves(self):
        game = Game()

        game.play(0, 1)
        game.play(1, 2)
        game.play(1, 1)
        game.play(0, 2)
        game.play(2, 1)
        winner = game.winner()

        self.assertEquals(winner, Game.PLAYER1)

    def test_player1_should_win__when_the_3rd_column_is_full_with_player1_moves(self):
        game = Game()

        game.play(0, 2)
        game.play(0, 1)
        game.play(1, 2)
        game.play(1, 1)
        game.play(2, 2)
        winner = game.winner()

        self.assertEquals(winner, Game.PLAYER1)

    def test_player2_should_win__when_1st_column_is_full_with_player2_moves(self):
        game = Game()

        game.play(0, 1)
        game.play(0, 0)
        game.play(0, 2)
        game.play(1, 0)
        game.play(1, 1)
        game.play(2, 0)
        winner = game.winner()

        self.assertEquals(winner, Game.PLAYER2)

    def test_player2_should_win__when_2nd_column_is_full_with_player2_moves(self):
        game = Game()

        game.play(1, 0)
        game.play(0, 1)
        game.play(1, 2)
        game.play(1, 1)
        game.play(0, 2)
        game.play(2, 1)
        winner = game.winner()

        self.assertEquals(winner, Game.PLAYER2)

    def test_player2_should_win__when_3rd_column_is_full_with_player2_moves(self):
        game = Game()

        game.play(1, 0)
        game.play(0, 2)
        game.play(2, 0)
        game.play(1, 2)
        game.play(1, 1)
        game.play(2, 2)
        winner = game.winner()

        self.assertEquals(winner, Game.PLAYER2)

    def test_game_is_over__when_player1_wins(self):
        game = Game()

        game.play(0, 2)
        game.play(0, 1)
        game.play(1, 2)
        game.play(1, 1)
        game.play(2, 2)
        game_over = game.is_over()

        self.assertTrue(game_over)

    def test_game_is_over__when_player2_wins(self):
        game = Game()

        game.play(1, 0)
        game.play(0, 2)
        game.play(2, 0)
        game.play(1, 2)
        game.play(1, 1)
        game.play(2, 2)
        game_over = game.is_over()

        self.assertTrue(game_over)

    def test_game_not_over__when_no_player_wins__and_board_not_full(self):
        game = Game()

        game.play(0, 2)
        game.play(0, 1)
        game.play(1, 2)
        game.play(1, 1)
        game_over = game.is_over()

        self.assertFalse(game_over)

    def test_game_is_over__when_board_is_full(self):
        game = Game()

        game.play(0, 0)
        game.play(0, 2)
        game.play(0, 1)
        game.play(1, 0)
        game.play(1, 2)
        game.play(1, 1)
        game.play(2, 0)
        game.play(2, 1)
        game.play(2, 2)
        game_over = game.is_over()

        self.assertTrue(game_over)

    def test_player2_should_not_be_able_to_play__when_game_is_over_by_player1_winning(self):
        game = Game()

        game.play(0, 2)
        game.play(0, 1)
        game.play(1, 2)
        game.play(1, 1)
        game.play(2, 2)
        success = game.play(0, 0)

        self.assertFalse(success)

    def test_player1_should_not_be_able_to_play__when_game_is_over_by_player2_winning(self):
        game = Game()

        game.play(1, 0)
        game.play(0, 2)
        game.play(2, 0)
        game.play(1, 2)
        game.play(1, 1)
        game.play(2, 2)
        success = game.play(0, 0)

        self.assertFalse(success)

if __name__ == '__main__':
    unittest.main()
