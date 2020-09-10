"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countx=0
    counto=0
    for i in range(3):
        for j in range(3):
            if board[i][j]==X:
                countx+=1
            elif board[i][j]==O:
                counto+=1
    if countx>counto:
        return O
    else:
        return X

    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    allactionspossible= set()
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                allactionspossible.add((i,j))
    return allactionspossible
    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result = copy.deepcopy(board)
    result[action[0]][action[1]] = player(board)
    return result
    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]:
            return board[i][0]
    for j in range(3):
        if board[0][j]==board[1][j]==board[2][j]:
            return board[0][j]
    if board[0][0]==board[1][1]==board[2][2] or board[0][2]==board[1][1]==board[2][0]:
        return board[1][1]


    return None
    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    if not(any(EMPTY in sublist for sublist in board) and winner(board) is None):
        return True
    else:
        return False
    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board)==X:
            return 1
        elif winner(board)==O:
            return -1
        else:
            return 0
    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board)==X:
            value,ac= maxval(board)
            return ac
        else:
            value,ac= minval(board)
            return ac
    # raise NotImplementedError




def maxval(board):
    if terminal(board):
        return utility(board),None
    v=-10
    mov=None
    for action in actions(board):
        sup,act=minval(result(board,action))
        if sup>v:
            v=sup
            mov=action
            if v==1:
                return v,mov

    return v,mov


def minval(board):
    if terminal(board):
        return utility(board),None
    v=10
    mov=None
    for action in actions(board):
        sup,act=maxval(result(board,action))
        if sup<v:
            v=sup
            mov=action
            if v==-1:
                return v,mov

    return v,mov
