
from collections import deque


def isValidSudoku(board):
  cnt = 0
  # 3 * 3씩 bfs로 
  # x, y로 이동
  dx = [-1, -1, -1, 0, 0, 1, 1, 1]
  dy = [-1, 0, 1, -1, 1, -1, 0, 1]

  for i in range(len(board)):
    row = {}
    col = {}
    
    #가로줄
    for j in board[i]:
      if cnt == 9:
        cnt = 1
      if j in row:
        return False
      

      cnt += 1

      if j != ".":
        row[j] = j

    for j in range(len(board[i])):
      dict = {}
      if board[j][i] in col:
        return False
      
      if board[j][i] != ".":
        col[board[j][i]] = board[j][i] 

      if board[i][j] != '.':
        dict[board[i][j]] = board[i][j]
      if (i == 1 or i == 4 or i == 7) and (j == 1 or j == 4 or j == 7):
        for k in range(8):

          next_x = i + dx[k]
          next_y = j + dy[k]
            
          if board[next_x][next_y] in dict :
            return False
            
          if board[next_x][next_y] != '.':
            dict[board[next_x][next_y]] = board[next_x][next_y]
  return True




print(isValidSudoku(
[["5","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]]
))