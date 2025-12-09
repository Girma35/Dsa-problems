class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[i][j]
                if item in s :
                    return False
                elif item !=  "." :
                    s.add(item)
        for i in range (9):
            s = set()
            for j in range(9):
                item = board[j][i]
                if item in s:
                    return False
                elif item != ".":
                    s.add(item)
        start = [
    (0, 0), (0, 3), (0, 6),
    (3, 0), (3, 3), (3, 6),
    (6, 0), (6, 3), (6, 6)
]
        for si , sj in start:
            s = set()
            for i in range(si , si+3):
                for j in range(sj ,sj +3):
                    item = board[i][j]
                    if item in s :
                        return False
                    elif item != '.':
                        s.add(item)

        return True 


