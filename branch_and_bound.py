 # -*- coding: utf-8 -*-
from board import Board
from queue import Queue
def main(board,min_cost=-1,tt=1):
    selections = board.find_condidates()
    childrens = []
    for i in selections:
        newObj = Board(board.ar,empty_house=board.empty_house,parent=board,child=[],promissing=True,expanded=False,level=board.level+1)
        newObj.move(i)
        childrens.append(newObj)
    min_board = childrens[0]
    min_num = min_board.count_wrong_tiles()
    for i in range(1,len(childrens)):
        item = childrens[i]
        current_num = item.count_wrong_tiles()
        if(current_num < min_num):
            min_board = item
            min_num = current_num
    if(not min_board.check_board_solve()):
        min_board.expanded = True
        return main(min_board,min_cost,tt+1)
    if(min_cost == -1 or min_cost>min_board.level):
        min_cost = min_board.level
    
    return min_board

def main2(board):
    if(board.check_board_solve() == True):
        return board
    q = Queue()
    q.put(board)

    while(True):
        if(q.empty()):break
        node = q.get()
        if(node.check_board_solve()):return node
        conditions = node.find_condidates()
        childrens = []
        for i in conditions:
            newObj = Board(node.ar,empty_house=node.empty_house,parent=node,child=[],promissing=True,expanded=False,level=node.level+1)
            newObj.move(i)
            childrens.append(newObj)
        node.childrens = childrens
        for i in node.childrens:
            q.put(i)


