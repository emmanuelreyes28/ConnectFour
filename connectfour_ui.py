# Emmanuel Reyes 58725927 Carlos Esparza 80821030
#connect_ui

import connectfour_console
import connectfour_board
import connectfour_connection
import connectfour


connect_host = 'woodhouse.ics.uci.edu'
connect_port = 4444



def Host()-> str:
    while True:

        connect_host = input('Host: ').strip()

        if connect_host == '' :
            print('Please enter host: ')
        else:
            return connect_host
def Port() -> int:
    while True:
        try:
            connect_port = int(input('Port: ').strip())

            if connect_port < 0 or connect_port >65535:
                print(' Enter a port number between 0 and 65535')
            else:
                return connect_port
        except ValueError:
            print('Port must be a number between 0 and 65535')
            


         

def user_interface() -> None:

    host_connect = Host()
    port_connect = Port()
            
    name = username()

    connection = connectfour_connection.wired(host_connect,port_connect)

    try:

        connectfour_connection.hi(connection,name)
        
        while handle_command(connection):
            pass
        
    finally:
        connectfour_connection.ConnectFourClose(connection)


def handle_command( connection : connectfour_connection.ConnectFourConnection) -> bool:
    
    command = connectfour_console.movement()

    


    


#def handle_ai_command(connection : connectfour_connection.ConnectFourConnection) -> None

    
    


def username() -> str:

    '''asks user for username that does not contain whitespace'''
    while True:
        username = input('Please provide a username: ' )
        if len(username.split(' ')) == 1 :
            return username    
        else:
            print()


