import random
import math

class Player:
    def __init__(self, letter) -> None:
        self.letter = letter
    
    def get_move(self):
        pass

class HumanPlayer(Player):
    def __init__(self, letter) -> None:
        super().__init__(letter)
        self.reference = "human"
    
    def get_move(self, board):
        chosen_cell = input(f"Choose cell from {board.available_cells()}")
        return int(chosen_cell)
    
class RandomAI(Player):
    def __init__(self, letter) -> None:
        super().__init__(letter)
        self.reference = "random"
    
    def get_move(self, board):
        chosen_cell = random.choice(board.available_cells())
        return chosen_cell

class MiniMaxAI(Player):
    def __init__(self, letter) -> None:
        super().__init__(letter)
        self.reference = "minimax"
    
    def get_move(self, board):
       
        if len(board.available_cells()) == 9:
            # chosen_cell = random.choice([0,2,6,8])
            chosen_cell = random.choice(board.available_cells())
        else:
            chosen_cell = self.miniMax(board, True)['chosen_cell']
        
        return chosen_cell
        
    def miniMax(self, board, isMax):
        
        if isMax:
            best = {'chosen_cell': None, 'score': -math.inf}
            letter = self.letter
        else:
            best = {'chosen_cell': None, 'score': math.inf}
            letter = 'o' if self.letter == 'x' else 'x'
        
        for possible_move in board.available_cells():
            
            board.make_move(letter, possible_move)

            if board.is_winner_move(letter, possible_move):
                board.board[possible_move] = possible_move
                return {
                    'chosen_cell': possible_move,
                    'score': (len(board.available_cells())+1) * (1 if isMax else -1)
                }
            
            elif len(board.available_cells()) == 0:
                board.board[possible_move] = possible_move
                return {'chosen_cell': possible_move, 'score': 0}



            latest_score = self.miniMax(board, not isMax)

            board.board[possible_move] = possible_move
            latest_score['chosen_cell'] = possible_move

            if isMax:
                if latest_score['score'] > best['score']:
                    best = latest_score
                
            else:
                if latest_score['score'] < best['score']:
                    best = latest_score

        return best
    

if __name__ == "__main__":
    minimax = MiniMaxAI("x")
    print(minimax.get_move([0,1,2,3,4,5,6,7,8]))
