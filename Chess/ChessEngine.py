"""
Main file to handle user input and display GameState object
"""


class GameState():
    def __init__(self):
        #creates a 2x2 list of strings of 2 characters
        #, where the first letter of the string represents b(lack) or w(hite)
        #where the second letter denotes the type of piece p(awn), R(ook), k(N)ight, B(ishop), Q(ueen), K(ing)
        # and where -- denotes an empty space
        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bK', 'bR'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wK', 'wR'],
        ]
        #gives white the first move
        self.whiteToMove = True
        #log of moves, where the move is what square a piece moves to
        self.moveLog = []