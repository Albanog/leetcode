class Solution(object):
    
    def isValidSudoku(self, board):
        '''
        :type board: List[List[str]]
        :rtype: bool
        '''
        for row in range(9):
            vistos = set()
            for col in range(9):
                v = board[row][col]
                if v != ".":
                    if v in vistos:
                        return False
                    vistos.add(v)

        for col in range(9):
            vistos = set()
            for row in range(9):
                v = board[row][col]
                if v != ".":
                    if v in vistos:
                        return False
                    vistos.add(v)

        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                vistos = set()
                for i in range(3):
                    for j in range(3):
                        v = board[box_row+i][box_col+j]
                        if v != ".":
                            if v in vistos:
                                return False
                            vistos.add(v)

        return True