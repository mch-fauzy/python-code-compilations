# 1 - To Display Board (3x3)
#from IPython.display import clear_output
def display_board(board):
  #clear_output() # only work on google colab or jupyter notebook
  print('\n' * 100)
  print(f' {board[1]} | {board[2]} | {board[3]} ')
  print('-----------')
  print(f' {board[4]} | {board[5]} | {board[6]} ')
  print('-----------')
  print(f' {board[7]} | {board[8]} | {board[9]} ')

# 2 - To Pick Marker or Symbol for plays the tic tac toe
def player_marker():
  # List of Posible Marker
  posible_marker = ['X', 'O']
  
  while True:
    # Pick your marker
    marker = input('Player 1: Pick your marker "X" or "O" -> ').upper()

    if marker not in posible_marker:
      # If marker not in list, then:
      print('Sorry, wrong marker')
    elif marker == posible_marker[0]:
      # return Tuple (Player 1 is "X", Player 2 is "O")
      return ('X', 'O')
    else:
      # return Tuple (Player 1 is "O", Player 2 is "X")
      return ('O', 'X')

# 3 - To place the marker in the board
def place_marker(board, marker, position):
  board[position] = marker

# 4 - to Check whick player is won
def win_check(board, mark):
  return ((board[1] == mark and board[2] == mark and board[3] == mark) or # Horizontal Atas
          (board[4] == mark and board[5] == mark and board[6] == mark) or # Horizontal Tengah
          (board[7] == mark and board[8] == mark and board[9] == mark) or # Horizontal Bawah
          (board[1] == mark and board[4] == mark and board[7] == mark) or # Vertikal Kiri
          (board[2] == mark and board[5] == mark and board[8] == mark) or # Vertikal Tengah
          (board[3] == mark and board[6] == mark and board[9] == mark) or # Vertikal Kanan
          (board[1] == mark and board[5] == mark and board[9] == mark) or # Diagonal
          (board[3] == mark and board[5] == mark and board[7] == mark))   # Diagonal


# 5 - Pick which player takes the first turn
from random import randint
def plays_first():
    if randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

# 6 - Check available space for every position
def board_check(board):
    for position in range(1,10):
      if board[position] == ' ':
        # Return False if there is available space
        return False

    # Return True if Full
    return True

# 7 - to pick a position for marker
def pick_position(board):
    while True:
      position = int(input('Choose your next position: (1-9) '))
      # Check if position is within range or the board space is available
      if position not in range(1, 10) or not board[position] == ' ':
        print('Position is not within range or space is occupied')
      else:
        break
        
    return position

# 8 - Return True if Y or y is entered (To play the game again)
def replay():
  return input('Do you want to play again ("Y" or "N"): ').upper().startswith('Y')

# 9 - Main Program

# Board position
the_board = ['Dummy','1','2','3',
                     '4','5','6',
                     '7','8','9']
display_board(the_board)

while True:

  # Assign tuple from player_marker() to variable
  player1_marker, player2_marker = player_marker()
  print(f'Player 1 is {player1_marker} and Player 2 is {player2_marker}')

  # To pick whick player plays first
  turn = plays_first()
  print(f'{turn} plays first')

  # To Enter the Game
  play_game = input('Are you ready to play ("Y" or "N"): ').upper()
  if play_game[0] == 'Y':
    ok = True
  else:
    break
  
  # Assign the empty board
  the_board = ['Dummy',' ',' ',' ',
                       ' ',' ',' ',
                       ' ',' ',' ']

  # if ok is True, lets the game begin (game loop)
  while ok:

    # Player 1 turn
    if turn == 'Player 1':
      # Display the Board
      display_board(the_board)
      
      print('--Player 1 Turn--')
      # Assign position number ot variable
      position = pick_position(the_board)

      # Place the marker to the board based on player 1 marker and picked position number
      place_marker(the_board, player1_marker, position)
      
      # To check if player 1 has won or not
      if win_check(the_board, player1_marker):
        # If won
        display_board(the_board)
        print('Player 1 won the game !!')
        # break from the game loop
        ok = False
      else:
        # check is it the board is already full or not
        if board_check(the_board):
          display_board(the_board)
          print('The game is draw !!')
          break
        else:
          # If not, then player 2 takes the turn
          turn = 'Player 2'
    
    # Player 2 Turn
    elif turn == 'Player 2':
      display_board(the_board)
      print('--Player 2 Turn--')
      position = pick_position(the_board)
      place_marker(the_board, player2_marker, position)
      
      if win_check(the_board, player2_marker):
        display_board(the_board)
        print('Player 2 won the game !!')
        ok = False
      else:
        if board_check(the_board):
          display_board(the_board)
          print('The game is draw !!')
          break
        else:
          turn = 'Player 1'
  
  # If replay() is True / not replay() is False, then play again
  if not replay():
    break