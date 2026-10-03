class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(curr: str, row: int, column: int, used: [(int,int)]) -> bool: 
            # print(curr)
            # print("row: ", row)
            # print("column: ", column)
            if curr == word:
                return True
            if (row, column) in used: 
                return False
            for i in range(min(len(curr), len(word))):
                if curr[i] != word[i]:
                    return False
            if row >= len(board):
                return False
            if column >= len(board[0]):
                return False
            if row < 0:
                return False
            if column < 0:
                return False
            x = backtrack(curr + board[row][column], row + 1, column, used + [(row, column)]) or backtrack(curr + board[row][column], row, column+1,used + [(row, column)])
            y = backtrack(curr + board[row][column], row - 1, column, used + [(row, column)]) or backtrack(curr + board[row][column], row, column - 1, used + [(row, column)])
            # z = backtrack(board[row][column], row + 1, column, used + [(row, column)]) or backtrack(board[row][column], row, column, used + [(row, column)])
            # k = backtrack(board[row][column], row - 1, column, used + [(row, column)]) or backtrack(board[row][column], row, column - 1, used + [(row, column)])
            return x or y
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack("",i,j,[]):
                    return True
        return False