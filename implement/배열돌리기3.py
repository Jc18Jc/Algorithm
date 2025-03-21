import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
operations = list(map(int, input().split()))

def fun1():
  board2 = [[0 for _ in range(M)] for _ in range(N)]
  for i in range(N):
    for j in range(M):
      board2[i][j] = board[N-i-1][j]
  return board2, N, M

def fun2():
  board2 = [[0 for _ in range(M)] for _ in range(N)]
  for i in range(N):
    for j in range(M):
      board2[i][j] = board[i][M-j-1]
  return board2, N, M

def fun3():
  board2 = [[0 for _ in range(N)] for _ in range(M)]
  for i in range(M):
    for j in range(N):
      board2[i][j] = board[N-1-j][i]
  return board2, M, N

def fun4():
  board2 = [[0 for _ in range(N)] for _ in range(M)]
  for i in range(M):
    for j in range(N):
      board2[i][j] = board[j][M-1-i]
  return board2, M, N

def fun5():
  board2 = [[0 for _ in range(M)] for _ in range(N)]
  for i in range(N//2):
    for j in range(M//2):
      board2[i][j] = board[i+N//2][j]
  for i in range(N//2):
    for j in range(M//2, M):
      board2[i][j] = board[i][j-M//2]
  for i in range(N//2, N):
    for j in range(M//2, M):
      board2[i][j] = board[i-N//2][j]
  for i in range(N//2, N):
    for j in range(M//2):
      board2[i][j] = board[i][j+M//2]
  return board2, N, M
  

def fun6():
  board2 = [[0 for _ in range(M)] for _ in range(N)]
  for i in range(N//2):
    for j in range(M//2):
      board2[i][j] = board[i][j+M//2]
  for i in range(N//2):
    for j in range(M//2, M):
      board2[i][j] = board[i+N//2][j]
  for i in range(N//2, N):
    for j in range(M//2, M):
      board2[i][j] = board[i][j-M//2]
  for i in range(N//2, N):
    for j in range(M//2):
      board2[i][j] = board[i-N//2][j]
  return board2, N, M
  

for operation in operations:
  if operation == 1:
    board, N, M = fun1()
  elif operation == 2:
    board, N, M = fun2()
  elif operation == 3:
    board, N, M = fun3()
  elif operation == 4:
    board, N, M = fun4()
  elif operation == 5:
    board, N, M = fun5()
  elif operation == 6:
    board, N, M = fun6()

for boardLine in board:
  print(*boardLine)
  