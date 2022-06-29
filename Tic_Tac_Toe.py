import random
import os
def clear():
    if os.name == 'nt':
        _ = os.system('cls')

class TicTacToe:

    def __init__(self):        #"Constructor"
        self.board = []        #Here we create a varibale called board.      

    def create_board(self):
        for i in range(3):
            row = []                    #variable declared
            for j in range(3):          #Loop nested      
                row.append('_')
            self.board.append(row)      #appending the constructor

    def get_random_first_player(self):
        return random.randint(0,1)       #Randomly getting the 1st player

    def fix_spot(self, row, col, player):
        self.board[row][col] = player       #This will be use during marking the cross or circle

    def is_board_filled(self):
        for row in self.board:
            for item in row:              # This  loop will check if the boxes are filled or not
                if item == '_':
                    return False
        return True


    def is_player_win(self, player):
        win = None

        n = len(self.board)                 #It will count the number of lists i.e. = 3

        # Checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # Checking Columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        #Checking Diagonals
        win =True
        for i in range(n):
            if self.board[i][i] != player:
                win = False            
                break
        if win:
            return win
        
        for i in range(n):
            win = True
            if self.board[i][i - 1 -i] != player:
                win = False
                break
        if win:
            return win
        return False

        self.is_board_filled()

    def swap_player_turn(self, player):            # It'll declare the turn of the player.
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        # clear()
        for row in self.board:
            for item in row:
                print(item, end =" ")
            print()
    
    def start(self):
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            
            print(f"Player {player} turn")
            
            self.show_board()

            #Taking User's Input
            row, col = list(
                map(int, input("Enter Row and Column numbers to fix the spot: ").split()))
            print()

            #Fixing the spot
            self.fix_spot(row - 1, col - 1, player)

            # Checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # Checking whether the game is draw or not
            clear()
            if self.is_board_filled():
                print("Match Draw!")
                break

            #Swapping the turn
            player = self.swap_player_turn(player)

        #Showing the final view of board
        print()
        self.show_board()

#Starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
