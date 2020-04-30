#Emmanuel Reyes 58725927 Carlos Esparza 80821030

#y = connectfour._new_game_board()
#print_board(y)

import connectfour
import connectfour_board


##DO NOT TOUCH

## DONE ###


##def new_game()->'ConnectFourGame':
##    '''Returns an empty board'''
##    return gs.connectfour.new_game()
##
##def print_board(gs:'GameState')->None:
##    connectfour_board.print_board(gs)
##
##def drop_piece(gs:'GameState', column:int):
##    return connectfour.drop(gs, column-1)
            
def movement() -> str:

    ''' allows the player to pop or drop a disc into a given column
    and determines the winner'''
    
    gs = connectfour.new_game()
    connectfour_board.print_board(gs.board)
    print('If you want to drop type D, press enter and a column number.')
    print('If you want to pop type P, press enter and a column number.')
    while True:
        try:
            command = input()
            col=int(input())
            if command[0] == 'D':
                gs = connectfour.drop(gs, col-1)
                connectfour_board.print_board(gs.board)
            else:
                gs = connectfour.pop(gs, col-1)
                connectfour_board.print_board(gs.board)

            if connectfour.winner(gs) != connectfour.NONE:
                x= connectfour.winner(gs)
                if x == 1 :
                    print('RED WINS!')
                elif x == 2:
                    print('YELLOW WINS!')

                return command + ' '  + col
            
            
        except ValueError:
            print('Try again')
            pass

if __name__ == '__main__':
    movement()
    


        

        
        
        
    
        
        
