# Emmanuel Reyes 58725927 Carlos Esparza 80821030
# connectfour_connect

from collections import namedtuple
import socket 
import connectfour_ui 


#connect_host = 'woodhouse.ics.uci.edu'
#connect_port = 4444


ConnectFourConnection = namedtuple('ConnectFourConnection', ['socket', 'f_input', 'output'])

class ConnectFourError(Exception):
    pass

def wired(host: str, port: int) -> ConnectFourConnection:

    '''connects to server given host and port, returns a connection or raises
       an exception if connection fails'''
    four_socket = socket.socket()
    
    four_socket.connect((host,port))

    four_input = four_socket.makefile('r')
    four_output = four_socket.makefile('w')

    return ConnectFourConnection(
        socket = four_socket,
        f_input = four_input,
        output = four_output)

def hi ( connection: ConnectFourConnection, user: str) -> None:

    '''logs a user into the connectfour server'''

    write_line(connection,'I32CSFP_HELLO ' + user)
    expect_line(connection, 'WELCOME ' + user)
    #expect_line(connection, 'Error')
    write_line(connection,'AI_GAME' )
    expect_line(connection, 'READY' )



def read(connection: ConnectFourConnection) -> str :

    ''' reads a line of text from the server'''
    print(connection)
    return connection.f_input.readline()[:-1]


def ConnectFourClose(connection: ConnectFourConnection)-> None:

    ''' closes the connecton to the server '''
    connection.f_input.close()
    connection.output.close()
    connection.socket.close()


def sent( connection: ConnectFourConnection, response: str) -> None:

    ''' sends a message to the server from the user, if the communication fails
    an exception is raised'''
    
    write_line(connection, response  )
    expect_line(connection, 'OKAY')
    move = read( connection)
    read(connection)
    
    
    return move

def log_in(connection: ConnectFourConnection)-> bool:

    username = connectfour_ui.username()
    write_line(connection)
    
    
    
def expect_line(connection: ConnectFourConnection,expected:str) -> None:

    ''' reads and expects a specific line from the server '''
    print (connection)
    #line = read(connection)
    print(line)
    print(expected)
    if line != expected:
        raise ConnectFourError()

def write_line(connection:ConnectFourConnection, line: str) -> None:

    '''writes a line to the server and sends it immediately '''

    connection.output.write(line + '\r\n')
    connection.output.flush()






    

