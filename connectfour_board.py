

## DONE ## 

import connectfour



def print_board(Board: list) -> str:


    '''prints an empty board '''
    
    my_list = (connectfour.BOARD_COLUMNS)
    for num in range(my_list):
        print(num + 1, sep = ' ', end = " ")
    print()
    for rows in range (connectfour.BOARD_ROWS):
        for col in range(connectfour.BOARD_COLUMNS):
            
            if Board[col][rows]==0:
                print('.',sep = ' ',end = " " )
            elif Board[col][rows]== 1:
                print('R',sep = ' ',end = " ")
            else:
                print('Y',sep = ' ',end = " ")
        print()
