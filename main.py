# -*- coding: utf-8 -*-
from greedy import main as main_greedy
from greedy import main2 as main_greedy_2
from branch_and_bound import main as main_branch_and_bound
from branch_and_bound import main2 as branch_and_bound_2
from board import Board


def check_items(ar):
    check_flag = []
    for i in range(0,16):
        check_flag.append(False)
    print(check_flag)
    for item in ar:
        for innerItem in item:
            if innerItem == '*':
                check_flag[0] = True
            else:
                index = int(innerItem)
                check_flag[index] = True
    
    if False in check_flag:
        return False
    else :
        return True
        


print("welcome to my project : ")
file_name = input("Enter name of your file")
print(file_name)
file = ''
try:
    file = open(file_name,"r")
except :
    print("error in opening file")
    exit()

print("hey")
print(file)
lines = file.readlines()
ar = []
if(len(lines) != 4):
    print("this program is designed to solve 4*4 8 puzzle")
    exit()
else:
    for line in lines:
        line = line.replace("\n","")
        item = line.split(" ")           
        ar.append(item)
    status = check_items(ar)
    if(status == False):
        print("error in input file values")
    else:
        board = Board(ar)
        if (board.solvable() == False):
            print("the instance is not solvable")
            exit()
            
        print("we can continue")
        print("Enter 1-for first greedy approach")
        print("Enter 2-for first branch and bound approach")
        print("Enter 3-for second greedy approach")
        print("Enter 4-for second branch and bound approach")
        menu = input("Enter number of algorithm ")
        
        if menu == '1':
            main_greedy(board)            
        elif menu == '2':
            first_answer =  main_branch_and_bound(board)
            stack = []
            while(first_answer!=None):
                stack.append(first_answer)
                first_answer = first_answer.parent
            while(len(stack)):
                o = stack.pop()
                print("-----------------------")
                o.show_board()
        elif menu == '3':
            main_greedy_2(board)
        elif menu == '4':
            first_answer = branch_and_bound_2(board)
            stack = []
            while(first_answer!=None):
                stack.append(first_answer)
                first_answer = first_answer.parent
            while(len(stack)):
                o = stack.pop()
                print("-----------------------")
                o.show_board()