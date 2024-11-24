class TicTacToeLogic:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.winner = None
        self.game_over = False

    def make_move(self, position):
        """Make a move on the board"""
        if self._is_valid_move(position):
            self.board[position] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
                self.game_over = True
                return True, "win"
            elif self.is_board_full():
                self.game_over = True
                return True, "tie"
            else:
                self._switch_player()
                return True, "next_turn"
        return False, "invalid_move"

    def _is_valid_move(self, position):
        """Check if the move is valid"""
        return 0 <= position < 9 and self.board[position] == " " and not self.game_over

    def check_winner(self):
        """Check if there's a winner"""
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        
        for combo in win_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == 
                self.board[combo[2]] != " "):
                return combo
        return None

    def is_board_full(self):
        """Check if the board is full"""
        return " " not in self.board

    def _switch_player(self):
        """Switch the current player"""
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset_game(self):
        """Reset the game state"""
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.winner = None
        self.game_over = False