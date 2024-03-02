#Write a Program for Tic-Tac-Toe game between two human players.

#Importing the required libraries
import numpy as np
import random
from time import sleep
import sys

board = [' ' for x in range(10)]    
def printBoard(board):
    print(' | | ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print(' | | ')
    print('------------')
    print(' | | ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' | | ')
    print('------------')
    print(' | | ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(' | | ')

printBoard(board)