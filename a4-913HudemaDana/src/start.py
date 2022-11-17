"""
  Start the program by running this module
"""

from ui import *
from test import big_boss_test

def main():
    dict = {
        'apartment': [1, 2, 3,   4,  5, 6, 7,  8,   9,  10],
        'amount': [1, 10, 100, 200, 22, 2, 3, 30, 300, 333],
        'water': [1,   2,  12,  24,  2, 0, 0, 10, 100,   3],
        'heating': [0, 3,   8,  16,  2, 2, 3,  7,   0, 150],
        'electricity': [0,1,30, 60,  2, 0, 0,  5,   0,  30],
        'gas': [0,     3,   24, 48,  6, 0, 0,  2, 200,   0],
        'other': [0,   1,   26, 52, 10, 0, 0,  3,   0, 150]
          }

    list_max=[[1,1,0,0,0,0],[2,2,3,1,3,1],[3,12,8,30,24,26],[4,24,16,60,48,52],[5,2,2,2,6,10],[6,0,2,0,0,0],\
              [7,0,3,0,0,0],[8,10,7,5,2,3],[9,100,0,0,200,0],[10,3,150,30,0,150]]

    history = []
    big_boss_test(dict)
    console(dict, list_max, history)



main()
