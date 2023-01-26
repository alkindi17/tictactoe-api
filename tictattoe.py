"""
tic tac toe game
"""

import math

import players as p

class GameBoard:
    def __init__(self) -> None:
        self.board = [0,1,2,
                      3,4,5,
                      6,7,8]

    
    def available_cells(self) -> list[int]:
        return [cell for cell in self.board if isinstance(cell, int)]

    def make_move(self, letter: str, cell: int) -> None:
        if cell in self.available_cells():
            self.board[cell] = letter

    def is_winner_move(self, letter: str, cell: int) -> bool:
        # check the specific cell horizontally, vertically, and  both  diagonal ways.
        # to find out if the letter in that cell wins.

        if len(self.available_cells()) <= 4:

            # check the row of the cell
            row_index = math.floor(cell / 3)
            row = self.board[row_index*3:row_index*3+3]
            if all([c == letter for c in row]):
                return True
            
            # check the column of the cell
            column_index = cell % 3
            column = self.board[column_index:column_index+7:3]
            if all(c == letter for c in column):
                return True
            
            # check diagonally
            back_diagonal = self.board[0:9:4] # "\"
            if all(c == letter for c in back_diagonal):
                return True
            
            forward_diagonal = self.board[2:7:2]
            if all(c == letter for c in forward_diagonal):
                return True
        
        return False


    
class GameSession:
    def __init__(self, player_x:p.Player, player_o:p.Player, start:str) -> None:
        self.board = GameBoard()
        self.player_x = player_x
        self.player_o = player_o
        self.turn = self.player_x if start == "x" else self.player_o
        self.result = ""

    def get_move(self, player):
        # get move from a player and returns it
        while True:
            move = player.get_move(self.board)
            if move in self.board.available_cells():
                return move

    def next_turn(self):
        self.turn = self.player_o if self.turn == self.player_x else self.player_x

    def play_single_turn(self, chosen_cell):
        if not self.result:
            
            self.board.make_move(self.turn.letter, chosen_cell)
            if self.board.is_winner_move(self.turn.letter, chosen_cell):
                self.result = self.turn.letter
                self.turn = ""
            elif not self.board.available_cells():
                self.result = "draw"
                self.turn = ""
            else:
                self.next_turn()


if __name__ == "__main__":
    game = GameSession(p.HumanPlayer("x"), p.RandomAI("o"), 'x')
    print(game.play())
