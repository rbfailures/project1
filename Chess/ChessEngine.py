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
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]
        #gives white the first move
        self.whiteToMove = True
        #log of moves, where the move is what square a piece moves to
        self.moveLog = []
    def makeMove(self, move):
        self.board[move.startRow][move.startColumn] = '--'
        self.board[move.endRow][move.endColumn] = move.pieceMoved
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove
class Move():
    #dictionaries to help with coordinate to chess notation conversion
    ranksToRows = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToColumns = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    columnsToFiles = {v: k for k, v in filesToColumns.items()}

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startColumn = startSq[1]
        self.endRow = endSq[0]
        self.endColumn = endSq[1]
        self.pieceMoved = board[self.startRow][self.startColumn]
        self.pieceCaptured = board[self.endRow][self.endColumn]

    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startColumn) + self.getRankFile(self.endRow, self.endColumn)

    def getRankFile(self, r, c):
        return self.columnsToFiles[c] + self.rowsToRanks[r]

