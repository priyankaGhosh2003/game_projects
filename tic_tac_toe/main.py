
def print_board():
        print()
        print("| {} | {} | {} |".format(board[0], board[1], board[2]))
        print("| {} | {} | {} |".format(board[3], board[4], board[5]))
        print("| {} | {} | {} |".format(board[6], board[7], board[8]))
        print()

def player_move(icon, player):
        print("%s's turn..." %player)
        choice=int(input("enter yout move(1-9):").strip())
        while board[choice-1]!=" ":
                choice= int(input("worng choice...enter yout move(1-9):").strip())
        board[choice-1]=icon
def victory(icon):
        if (board[0]==board[1]==board[2]==icon) or\
           (board[3]==board[4]==board[5]==icon) or\
           (board[6]==board[7]==board[8]==icon) or\
           (board[0]==board[3]==board[6]==icon) or\
           (board[1]==board[4]==board[7]==icon) or\
           (board[2]==board[5]==board[8]==icon) or\
           (board[0]==board[4]==board[8]==icon) or\
           (board[2]==board[4]==board[6]==icon):
                return True
        else:
                return False

def draw():
        if " " not in board:
                return True
        else:
                return False
def play():
        player1=input("enter the name of the first player:")
        player2=input("enter the name of second player:")
        while(True):
                print_board()
                player_move('X',player1)
                if victory('X'):
                        print_board()
                        print("%s win the game" %player1)
                        break
                if draw():
                        print_board()
                        print("Draw!!!")
                        break
                print_board()
                player_move('O',player2)
                if victory('O'):
                        print_board()
                        print("%s win the game" %player2)
                        break

if __name__ == "__main__":
        while(True):
                board=[" " for i in range(9)]
                play()
                temp=input("want to play again?(y/n)").lower()
                if temp=="n":
                        break

