"""
    0----1     4
    | .  |   . 
    |  . | .
    3    2  
"""

dic = {
    0:[3, 2, 1], 
    3:[0], 
    1:[0, 2], 
    2:[0, 1, 4], 
    4:[2]
       }
def bfs(d, a):
    lis = []
    