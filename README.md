# Algorithm-Design-Project
This the Repository for my Project in Algorithm Design Course in University of Kashan!

-----------------------------

This project is for solving the 15 puzzle problem. and this project is written in Python programming language!

15 puzzle problem consists of 15 squares in 4*4 shape and contains numbers from 1 to 15!

the main goal in 15 puzzle problem is to order all the numbers are aligned in the specified order!

in here we want to develope this puzzle in 4*4 shape and we give the puzzle in a txt file as input! after that our program have to order the givven sample and show it to user!

we solved this problem in 2 ways! :

- first: Greedy
- second: Branch & Bound

Sample input:
1 2 3 4
5 10 6 8
9 14 7 11
13 * 15 12



Sample output:
1 2 3 4
5 10 6 8
9 * 7 11
13 14 15 12
-------------------------------------
1 2 3 4
5 * 6 8
9 10 7 11
13 14 15 12
-------------------------------------
1 2 3 4
5 6 * 8
9 10 7 11
13 14 15 12
-------------------------------------
1 2 3 4
5 6 7 8
9 10 * 11
13 14 15 12
-------------------------------------
1 2 3 4
5 6 7 8
9 10 11 *
13 14 15 12
-------------------------------------
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 *
