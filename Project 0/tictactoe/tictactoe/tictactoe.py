"""
Tic Tac Toe Player
"""

import math
import random

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
    Returns the player ('X' or 'O') who has the next turn on a board.
    """
    x_count = 0
    o_count = 0

    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1
    
    if x_count > o_count:
        return O
    
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns a new board state after making the move at 'action' (i, j)
    without modifying the original board.
    """
    new_board = []
    for row in board:
        new_row = []
        for element in row:
            new_row.append(element)
        new_board.append(new_row)  # Copy each row so if don't mess with the original
    new_board[action[0]][action[1]] = player(board)

    return new_board 


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    winner = None
    
    # Check rows and columns
    for i in range(3):
        # Rows
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            winner = board[i][0]
        # Columns
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            winner = board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        winner = board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        winner = board[0][2]
    
    return winner


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check rows and columns
    for i in range(3):
        # Rows
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return True
        # Columns
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return True
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return True

    # Check if there are empty spaces (game not finished)
    for row in board:
        if EMPTY in row:
            return False

    # No winner and no empty spaces = draw
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner = None
    result = 0
    
    # Check rows and columns
    for i in range(3):
        # Rows
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            winner = board[i][0]
        # Columns
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            winner = board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        winner = board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        winner = board[0][2]
    
    if winner == X:
        result = 1
    elif winner == O:
        result = -1

    return result


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        best_score = -9999
    else:
        best_score = 9999

    best_move = None

    for action in actions(board):
        new_board = result(board, action)
        score = minimax_score(new_board)

        if current_player == X and score > best_score:
            best_score = score
            best_move = action
            if best_score == 1:
                return best_move
        elif current_player == O and score < best_score:
            best_score = score
            best_move = action
            if best_score == -1:
                return best_move

    return best_move

def minimax_score(board, alpha=-9999, beta=9999):
    if terminal(board):
        return utility(board)

    current_player = player(board)

    if current_player == X:
        best_score = -9999
        for action in actions(board):
            score = minimax_score(result(board, action), alpha, beta)
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            if best_score == 1:
                return best_score  # Early return
            if beta <= alpha:
                break  # Pruning
        return best_score
    else:
        best_score = 9999
        for action in actions(board):
            score = minimax_score(result(board, action), alpha, beta)
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            if best_score == -1:
                return best_score  # Early return
            if beta <= alpha:
                break  # Pruning
        return best_score