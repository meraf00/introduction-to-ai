from abc import abstractmethod, ABC
from typing import Optional
import random


class XOPlayer(ABC):
    def __init__(self, player_letter):
        self.letter = player_letter
        self.opponent_letter = "O" if self.letter == "X" else "X"

    @abstractmethod
    def next_move(self, game):
        ...


class TicTacToe:
    def __init__(self, player_1: XOPlayer, player_2: XOPlayer):
        self.__board = [" "] * 9
        self.player_1 = player_1
        self.player_2 = player_2

    @property
    def board(self):
        return self.__board[:]

    def __str__(self):
        b = self.__board
        return f" {b[0]} | {b[1]} | {b[2]} \n-----------\n {b[3]} | {b[4]} | {b[5]}\n-----------\n {b[6]} | {b[7]} | {b[8]}"

    def is_game_complete(self, board=None) -> bool:
        board = board or self.__board
        return self.is_draw(board) or bool(self.get_winner(board))

    def is_draw(self, board=None) -> bool:
        board = board or self.__board

        if self.get_winner():
            return False

        for pos in board:
            if pos == " ":
                return False

        return True

    def get_winner(self, board=None) -> Optional[XOPlayer]:
        b = board or self.__board

        winner = None

        if b[0] == b[1] == b[2] and b[0] != " ":
            winner = b[0]
        elif b[3] == b[4] == b[5] and b[3] != " ":
            winner = b[3]
        elif b[6] == b[7] == b[8] and b[6] != " ":
            winner = b[6]
        elif b[0] == b[4] == b[8] and b[0] != " ":
            winner = b[0]
        elif b[2] == b[4] == b[6] and b[2] != " ":
            winner = b[2]
        elif b[0] == b[3] == b[6] and b[0] != " ":
            winner = b[0]
        elif b[1] == b[4] == b[7] and b[1] != " ":
            winner = b[1]
        elif b[2] == b[5] == b[8] and b[2] != " ":
            winner = b[2]

        if winner == self.player_1.letter:
            return self.player_1
        elif winner == self.player_2.letter:
            return self.player_2

        return None

    def is_valid_move(self, move: int, board=None) -> bool:
        board = board or self.__board
        return 0 <= move <= 8 and board[move] == " "

    def make_move(self, player: XOPlayer) -> bool:
        player_move = player.next_move(self)

        if self.is_valid_move(player_move):
            self.__board[player_move] = player.letter
            return True

        return False

    def valid_moves(self, board=None):
        board = board or self.__board
        return [i for i, letter in enumerate(board) if letter == " "]

    def start(self):
        players = [self.player_1, self.player_2]

        turn = 0

        while not self.is_game_complete():
            print("\n", self, "\n", sep="")

            current_player = players[turn]

            while not self.make_move(current_player):
                continue

            turn = (turn + 1) % 2

        winner = self.get_winner()

        print("\n", self, "\n", sep="")

        if winner:
            print(f"Player \033[92m{winner.letter}\033[0m won!")

        else:
            print(f"\033[94mDraw!\033[0m")


class HumanPlayer(XOPlayer):
    def __init__(self, player_letter):
        super().__init__(player_letter)

    def next_move(self, game):
        valid_moves = list(map(lambda x: x + 1, game.valid_moves()))

        while True:
            try:
                move = int(input())
                if move in valid_moves:
                    return move - 1

            except ValueError:
                pass

            print(f"Invalid input, try again: {valid_moves}")


class ComputerPlayer(XOPlayer):
    EASY = 0
    MEDIUM = 1
    HARD = 2

    def __init__(self, player_letter, difficulty=EASY):
        super().__init__(player_letter)

        move_processors = [self.easy, self.medium, self.hard]

        self.move_processor = move_processors[difficulty]

    def easy(self, game):
        return random.choice(game.valid_moves())

    def medium(self, game):
        move_1 = self.easy(game)
        move_2 = self.hard(game)

        if random.uniform(0, 1) < 0.7:
            return move_2
        return move_1

    def hard(self, game):
        _, move = self.max_value(game, game.board, float('-inf'), float('inf'))
        return move

    def max_value(self, game, board, alpha, beta):
        if game.is_game_complete(board):
            return self.evaluate_board(game, board), None

        valid_moves = game.valid_moves(board)

        max_score = float("-inf")
        max_move = None

        for move in valid_moves:
            board[move] = self.letter
            score, _ = self.min_value(game, board, alpha, beta)
            board[move] = " "
            if score > max_score:
                max_score = score
                max_move = move
                alpha = max(alpha, max_score)
            
            if score >= beta:
                return max_score, max_move

            

        return max_score, max_move

    def min_value(self, game, board, alpha, beta):
        if game.is_game_complete(board):
            return self.evaluate_board(game, board), None

        valid_moves = game.valid_moves(board)

        min_score = float("inf")
        min_move = None

        for move in valid_moves:
            board[move] = self.opponent_letter
            score, _ = self.max_value(game, board, alpha, beta)
            board[move] = " "

            if score < min_score:
                min_score = score
                min_move = move
                beta = min(beta, min_score)
            
            if score <= alpha:
                return min_score, min_move

            

        return min_score, min_move

    def evaluate_board(self, game: TicTacToe, board):
        valid_moves = game.valid_moves(board=board)

        win_count = 0
        lose_count = 0

        winner = game.get_winner(board)
        if winner and winner.letter == self.letter:
            win_count += 1

        if winner and winner.letter == self.opponent_letter:
            lose_count += 1

        for move in valid_moves:
            board[move] = self.letter

            winner = game.get_winner(board)
            if winner and winner.letter == self.letter:
                win_count += 1

            board[move] = self.opponent_letter

            winner = game.get_winner(board)
            if winner and winner.letter == self.opponent_letter:
                lose_count += 1

            board[move] = " "

        return win_count - lose_count

    def next_move(self, game):
        return self.move_processor(game)


if __name__ == "__main__":
    game_2_player = TicTacToe(HumanPlayer("X"), HumanPlayer("O"))

    game_2_computers = TicTacToe(
        ComputerPlayer("X", ComputerPlayer.HARD),
        ComputerPlayer("O", ComputerPlayer.HARD),
    )

    game_easy = TicTacToe(HumanPlayer("X"), ComputerPlayer("O"))

    game_medium = TicTacToe(
        HumanPlayer("X"), ComputerPlayer("O", difficulty=ComputerPlayer.MEDIUM)
    )

    game_hard = TicTacToe(
        HumanPlayer("X"), ComputerPlayer("O", difficulty=ComputerPlayer.HARD)
    )

    game_2_computers.start()
