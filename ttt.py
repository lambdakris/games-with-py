import random

def drawBoard(board):
    # this function prints out the board that it was passed

    # "board" is a list of 10 strings representing the board

    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])

def inputPlayerLetter():
    # lets the player type which letter they want to use
    # returns a list with the player's letter as the first item and the computer's letter as the second
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the list is the player's letter; the second is the computer's letter
    if letter == 'X':
        return ['X','O']
    else:
        return ['O','X']

def whoGoesFirst():
    # randomly choose who goes first
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(board, letter):
    # takes a board and a letter and determines whether the letter is in a winning combination
    
    return (
        # row by row
        (board[1] == letter and board[2] == letter and board[3] == letter) or
        (board[4] == letter and board[5] == letter and board[6] == letter) or
        (board[7] == letter and board[8] == letter and board[9] == letter) or
        # col by col
        (board[1] == letter and board[4] == letter and board[7] == letter) or
        (board[2] == letter and board[5] == letter and board[8] == letter) or
        (board[3] == letter and board[6] == letter and board[9] == letter) or
        # diagonals
        (board[1] == letter and board[5] == letter and board[9] == letter) or
        (board[7] == letter and board[5] == letter and board[3] == letter))

def getBoardCopy(board):
    # make a copy of the board
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    # check if there is nothing on the board for the move location
    return board[move] == ' '

def getPlayerMove(board):
    # let the player enter their move
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, listOfMoves):
    # returns a random move according to what is possible with the provided board and list of moves
    # returns None if there is no valid move

    freeMoves = []
    for i in listOfMoves:
        if isSpaceFree(board, i):
            freeMoves.append(i)

    if len(freeMoves) > 0:
        return random.choice(freeMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # given a board and the computer's letter, determine where the computer should move next
    # ??? the letter checking logic seems to be a pattern, can the established letters be passed in as a sort of game state???
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # here is the algorithm for our tic tac toe AI
    # first, check if the computer can win in the next move, if so, make that move to win
    # ??? the get winning move logic seems to be a pattern, can it be abstracted into a function???
    for i in range(1,10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i
    
    # second, check if the player can win in the next move, if so, make that move to block the player
    # ??? another instance of winning move logic ???
    for i in range(1,10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    # third, try to take one of the corners, if they are free
    # ??? the chooseRandomMoveFromList seems to include the check for isSpaceFree, which is diff from the get winning move game logic pattern ???
    move = chooseRandomMoveFromList(board, [1,3,7,9])
    if move != None:
        return move

    # fourth, try to take the center, if it is free
    if isSpaceFree(board, 5):
        return 5

    # move to one of the free sides
    return chooseRandomMoveFromList(board, [2,4,6,8])

def isBoardFull(board):
    # check if every space on the board is taken
    for i in range(1,10):
        if isSpaceFree(board, i):
            return False
    return True

def playGame():
    print('Welcome to Tic-Tac-Toe!')

    while True:
        # reset the board
        theBoard = [' '] * 10
        playerLetter, computerLetter = inputPlayerLetter()
        turn = whoGoesFirst()
        print('The ' + turn + ' will go first.')
        gameIsPlaying = True
        
        while gameIsPlaying:
            if turn == 'player':
                # player's turn
                drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)

                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print('Hooray! You have won the game!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'computer'
            else:
                # computer's turn
                move = getComputerMove(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)
                
                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print('Awwww! You lose the game!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player'

        print('Do you want to play again? (y or n)')
        if not input().lower() == 'y':
            break
        
