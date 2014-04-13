#!/usr/bin/python 

import sys
import fileinput

def main(argv):
	T = int(sys.stdin.readline())
	for count in range(1, T+1):
		# get arrg 1
		n1 = int(sys.stdin.readline()) - 1
		for i in range(0, 4):
			line = sys.stdin.readline()
			if i == n1:
				c1 = map(int, line.split())

		# get arrg 2
		n2 = int(sys.stdin.readline()) - 1
		for i in range(0, 4):
			line = sys.stdin.readline()
			if i == n2:
				c2 = map(int, line.split())

		temp = list(set(c1) & set(c2))

		if len(temp) == 0:
			res = "Volunteer cheated!"
		elif len(temp) == 1:
			res = str(temp[0])
		elif len(temp) > 1:
			res = "Bad magician!"

		# print results
		ss = "Case #"+ str(count) + ": " + res
		print(ss)

	pass

if __name__ == '__main__':
	main(sys.argv)
