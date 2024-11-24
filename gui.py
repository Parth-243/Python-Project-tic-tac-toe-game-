import tkinter as tk
from tkinter import messagebox
from logic import TicTacToeLogic
from styles import GameStyles

class TicTacToeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.configure(bg=GameStyles.COLORS['bg'])
        self.window.resizable(False, False)

        self.game_logic = TicTacToeLogic()
        self.buttons = []
        self._create_widgets()

    def _create_widgets(self):
        # Create title
        title = tk.Label(
            self.window,
            text="Tic Tac Toe",
            font=GameStyles.FONTS['title'],
            bg=GameStyles.COLORS['bg'],
            fg=GameStyles.COLORS['text'],
            pady=GameStyles.LAYOUT['padding']
        )
        title.pack()

        # Create game board
        self.board_frame = tk.Frame(
            self.window,
            bg=GameStyles.COLORS['bg'],
            padx=GameStyles.LAYOUT['padding'],
            pady=GameStyles.LAYOUT['padding']
        )
        self.board_frame.pack()

        # Create buttons
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(
                    self.board_frame,
                    text="",
                    font=GameStyles.FONTS['button'],
                    bg=GameStyles.COLORS['button'],
                    fg=GameStyles.COLORS['text'],
                    **GameStyles.BUTTON_STYLES,
                    command=lambda row=i, col=j: self._handle_click(row, col)
                )
                button.grid(
                    row=i, 
                    column=j, 
                    padx=GameStyles.LAYOUT['button_spacing'],
                    pady=GameStyles.LAYOUT['button_spacing']
                )
                button.bind('<Enter>', lambda e, btn=button: self._on_enter(btn))
                button.bind('<Leave>', lambda e, btn=button: self._on_leave(btn))
                row.append(button)
            self.buttons.append(row)

        # Create status label
        self.status = tk.Label(
            self.window,
            text=GameStyles.MESSAGES['turn'].format('X'),
            font=GameStyles.FONTS['status'],
            bg=GameStyles.COLORS['bg'],
            fg=GameStyles.COLORS['text'],
            pady=15
        )
        self.status.pack()

        # Create reset button
        self.reset_button = tk.Button(
            self.window,
            text="New Game",
            font=GameStyles.FONTS['reset'],
            command=self._reset_game,
            bg=GameStyles.COLORS['button'],
            fg=GameStyles.COLORS['text'],
            padx=20,
            pady=10
        )
        self.reset_button.pack(pady=10)
        self.reset_button.bind('<Enter>', lambda e: self._on_enter(self.reset_button))
        self.reset_button.bind('<Leave>', lambda e: self._on_leave(self.reset_button))

    def _handle_click(self, row, col):
        index = row * 3 + col
        success, result = self.game_logic.make_move(index)

        if success:
            button = self.buttons[row][col]
            player = self.game_logic.board[index]
            button.config(
                text=player,
                fg=GameStyles.COLORS['x'] if player == 'X' else GameStyles.COLORS['o']
            )

            if result == "win":
                self._highlight_winner()
                messagebox.showinfo("Game Over", GameStyles.MESSAGES['win'].format(player))
                self._disable_board()
            elif result == "tie":
                messagebox.showinfo("Game Over", GameStyles.MESSAGES['tie'])
                self._disable_board()
            else:
                self._update_status()

    def _highlight_winner(self):
        winning_combo = self.game_logic.check_winner()
        if winning_combo:
            for index in winning_combo:
                row, col = index // 3, index % 3
                self.buttons[row][col].config(bg=GameStyles.COLORS['win'])

    def _update_status(self):
        player = self.game_logic.current_player
        self.status.config(
            text=GameStyles.MESSAGES['turn'].format(player),
            fg=GameStyles.COLORS['x'] if player == 'X' else GameStyles.COLORS['o']
        )

    def _disable_board(self):
        for row in self.buttons:
            for button in row:
                button.config(state=tk.DISABLED)

    def _reset_game(self):
        self.game_logic.reset_game()
        for row in self.buttons:
            for button in row:
                button.config(
                    text="",
                    state=tk.NORMAL,
                    bg=GameStyles.COLORS['button'],
                    fg=GameStyles.COLORS['text']
                )
        self._update_status()

    def _on_enter(self, button):
        if button['state'] != tk.DISABLED:
            button['bg'] = GameStyles.COLORS['hover']

    def _on_leave(self, button):
        if button['state'] != tk.DISABLED:
            button['bg'] = GameStyles.COLORS['button']

    def run(self):
        self.window.mainloop()