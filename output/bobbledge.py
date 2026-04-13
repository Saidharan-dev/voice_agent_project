# Bobble Game in Python
import random
import time

class BobbleGame:
    def __init__(self):
        self.score = 0
        self.level = 1

    def draw_board(self, board):
        print("  +---+")
        for row in board:
            print(f" | {row[0]} | ", end="")
            for cell in row[1:]:
                if isinstance(cell, str):
                    print(f" ({cell}) ", end="")
                else:
                    print(cell, end=" ")
            print("|")
            print("  +---+")

    def update_board(self, board, move):
        new_board = [row[:] for row in board]
        # Update score
        if move == "up":
            self.score += len(new_board[0])
        elif move == "down":
            self.score -= len(new_board[0])

        # Check and update level
        if random.random() < 0.1:
            new_level = random.randint(2, 10)
            print(f"\nLevel increased to {new_level}!")
            self.level = new_level

        # Update game state
        for i in range(len(new_board)):
            for j in range(len(new_board[i])):
                if move == "left":
                    new_board[i][j] = (self.score + new_board[i][j]) % 10
                elif move == "right":
                    new_board[i][j] = (self.score - new_board[i][j]) % 10

        return new_board

    def play(self):
        board_size = random.randint(3, 7)
        initial_board = [[random.randint(1, 9) for _ in range(board_size)] for _ in range(board_size)]
        while True:
            self.draw_board(initial_board)
            move = input("Enter direction (up, down, left, right): ")
            if move not in ["up", "down", "left", "right"]:
                print("Invalid move. Try again!")
                continue

            new_board = self.update_board(initial_board, move)
            initial_board = new_board
            # Game over condition
            if all(cell == 0 for row in new_board for cell in row):
                print("\nCongratulations! You won with a score of", self.score)
                break


if __name__ == "__main__":
    game = BobbleGame()
    game.play()