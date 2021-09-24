#Author: Yahia Moussadek
from time import sleep

print('Enter the board 9x9 separated with space [0 for empty cells]....')
print()
l = [list(map(int,input().split(' '))) for i in range(9)]

def solve(l):
	if not find_empty(l):
		return True

	else :
		x,y = find_empty(l)

		for i in range(1,10):
			if valid(l, i, (x,y)):
				l[x][y] = i

				if solve(l):
					return True
				l[x][y] = 0

def valid(l, num, pos):
	#Check row
	for i in range(9):
		if l[pos[0]][i] == num and i != pos[1]:
			return False

	#Check column
	for i in range(9):
		if l[i][pos[1]] == num and i != pos[0]:
			return False

	#Check box
	box_x = pos[1] // 3
	box_y = pos[0] // 3

	for i in range(box_y*3, box_y*3+3):
		for j in range(box_x*3, box_x*3+3):
			if l[i][j] == num and (i,j) != pos:
				return False

	return True


def print_l(l):
	for i in range(9):
		if i % 3 == 0 and i != 0:
			print('---------------------')

		for j in range(9):
			print(l[i][j], end=" ")
			if j == 2 or j == 5:
				print('|',end=" ")

		print()


def find_empty(l):
	for i in range(9):
		for j in range(9):
			if l[i][j] == 0:
				return (i,j)

	return False

solve(l)
sleep(5)
print()
print_l(l)