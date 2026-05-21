class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = 9
        col = 9

        for i in range(row):
            s = set()
            for j in range(col):
                if board[i][j] == ".":
                    continue
                if board[i][j] in s:
                    return False
                s.add(board[i][j])
        
        for i in range(row):
            s = set()
            for j in range(col):
                if board[j][i] == ".":
                    continue
                if board[j][i] in s:
                    return False
                s.add(board[j][i])
        

        for i in range(0,row,3):
            for j in range(0,col,3):
                s = set()
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        if board[k][l] == ".":
                            continue
                        if board[k][l] in s:
                            return False
                        s.add(board[k][l])
        return True
                        

        