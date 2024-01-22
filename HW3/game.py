class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def display_board(self):
        for i in range(0, 9, 3):
            print(f'{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}')
            if i < 6:
                print('-'*9)

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            return True
        else:
            return False

    def check_winner(self):
        # Проверка победителя
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ' ':
                return True
        return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def is_tie(self):
        return ' ' not in self.board

    def play_game(self):
        while not self.check_winner() and not self.is_tie():
            self.display_board()
            try:
                move = int(input(f"Player {self.current_player}, enter the position (0-8): "))
                if 0 <= move <= 8:
                    if self.make_move(move):
                        if self.check_winner():
                            self.display_board()
                            print(f"Player {self.current_player} wins!")
                        else:
                            self.switch_player()
                    else:
                        print("This position is already taken. Try again.")
                else:
                    print("Invalid input. Please enter a number between 0 and 8.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if self.is_tie():
            self.display_board()
            print("It's a tie!")
