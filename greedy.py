# -*- coding: utf-8 -*-
def main(board):
    while(not board.check_board_solve()):
        best = board.select_base_condidate()
        board.move(best)
        board.show_board()
        print("-----------------------------")
def main2(board):
    while(not board.check_board_solve()):
        best = board.select_bast_condidate_manhatan()
        board.move(best)
        board.show_board()
        print("-----------------------------")
