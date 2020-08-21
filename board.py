# -*- coding: utf-8 -*-
import copy
class Board:
    def __init__(self,ar,empty_house=None,parent=None,child=[],promissing=True,expanded=False,level=0):
        self.ar = copy.deepcopy(ar)
        self.empty_house = (0,0)
        col = 0
        row = 0
        self.parent = parent
        self.child = child
        self.promissing = promissing
        self.expanded = expanded
        self.level = level
        if empty_house == None:
            for i in ar:
                col = 0
                for innerItem in i:
                    if innerItem == '*':
                        self.empty_house = (row,col)
                        return;
                    col +=1
                row+=1   
        else:
            self.empty_house = empty_house

        
    def move(self,cell=(0,0)):
        if(self.move_check(cell)):
            self.ar[self.empty_house[0]][self.empty_house[1]] = self.ar[cell[0]][cell[1]]
            self.ar[cell[0]][cell[1]] = '*'
            self.empty_house = cell
    
    def move_check(self,cell=(0,0)):
        #check being in smae col or same row
        if cell[0] == self.empty_house[0]  or cell[1] == self.empty_house[1]:
            return True
        return False
    def show_board(self):
        for i in self.ar:
            print(i)
    def check_board_solve(self):
        value = 1
        for row in self.ar:
            for col in row:
                cmp = str(value)
                if col != cmp :
                    if value == 16 and col == '*':
                        return True
                    return False
                value = value + 1
        return True
    
    def find_condidates(self):
        condidates = []
        x = self.empty_house[0]
        y = self.empty_house[1]
        if x+1 <= 3 :
            condidates.append((x+1,y))
        if y+1 <=3 :
            condidates.append((x,y+1))
        if y-1 >= 0:
            condidates.append((x,y-1))
        if x-1 >= 0:
            condidates.append((x-1,y))
        return condidates
    
    def select_base_condidate(self):
        condidates = self.find_condidates()
        val = self.calculate_required_number(self.empty_house)
        for item in condidates:
            if self.ar[item[0]][item[1]] == str(val):
                return item
        return condidates[0]
    
    def sorted_conditions_branch_and_bound(self):
        return self.find_condidates()
        
    def calculate_required_number(self,house=(0,0)):
        val = (house[0])*4+ house[1] + 1
        return val
    def solvable(self):
        '''
            geeksforgeeks.org/check-instance-15-puzzle-solvable
            if N is even ,puzzle instance is sovable if:
            the blank is on an evenrow counting from the bottom and number of inversions is odd
            the blank is on an odd row counting from the bottm and inversion is even
            
        '''
        inversions = self.count_inversions()
        if(self.empty_house[0] == 2 or self.empty_house[0] == 0):
            if inversions % 2 == 1 :
                return True
        if(self.empty_house[0] == 3 or self.empty_house[0] == 1):
            if inversions % 2 == 0:
                return True
        return False
        
        pass
    def sum_of_manhatan_distance(self):
        locations = [[],
                     [0,0],[0,1],[0,2],[0,3],
                     [1,0],[1,1],[1,2],[1,3],
                     [2,0],[2,1],[2,2],[2,3],
                     [3,0],[3,1],[3,2],[3,3],        
        ]
        sum_man = 0
        for i in range(0,4):
            for j in range(0,4) :
                if self.ar[i][j] != '*':
                    x = locations[int(self.ar[i][j]) ][0]
                    y = locations[ int(self.ar[i][j]) ][1]
                    sum_man += abs(i-x) + abs(y-j)
        return sum_man
    def select_bast_condidate_manhatan(self):
        condidates = self.find_condidates()
        best = Board(self.ar,empty_house=self.empty_house)
        best_cell = condidates[0]
        best.move(best_cell)
        dis = best.sum_of_manhatan_distance()
        for i in range(1,len(condidates)):
            best = Board(self.ar,empty_house=self.empty_house)
            best.move(condidates[i])
            if(best.sum_of_manhatan_distance()<dis):
                best_cell = condidates[i]
                dis = best.sum_of_manhatan_distance()
        return best_cell
    def count_inversions(self):
        '''
            if we assume tiles are written out ina single row
            instead of being in spread in N-rows ,a pair of tiles (a,b) 
            from an inversion if a apears before b but a>b
            1 8 2 x 4 3 7 6 5
        '''
        single_row = []
        for i in self.ar:
            for j in i:
                if j!= '*':
                    single_row.append(int(j))
        inversions = 0
        for i in range(0,len(single_row)):
            for j in range(i+1,len(single_row)):
                if(single_row[i]>single_row[j]):
                    inversions+=1
        return inversions
    def count_wrong_tiles(self):
        wrong = 0
        num = 1
        for i in self.ar:
            for j in i:
                if j == '*':
                    if num != 16:
                        wrong+=1
                elif j != str(num):
                    wrong+=1
                num+=1
        return wrong
                                    