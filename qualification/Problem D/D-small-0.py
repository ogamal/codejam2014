#!/usr/bin/python 

import sys
import fileinput

def main(argv):
	T = int(sys.stdin.readline())
	for count in range(1, T+1):
		# init variables
		score = 0
		dscore = 0

		N = int(sys.stdin.readline())
		
		# get naomi's blocks
		line = sys.stdin.readline()
		naomi = sorted(map(float, line.split()))
		
		#get ken's blocks
		line = sys.stdin.readline()
		ken = sorted(map(float, line.split()))

		# Normal war
		nn = list(naomi)
		kk = list(ken)
		while (len(nn) > 0):
			x = nn.pop(-1)
			for i in range(0, len(kk)):
				if kk[i] > x:
					del kk[i]
					break
				elif i == len(kk) - 1:
					kk.pop(0)
					score = score + 1

		# Deceitful war
		while (N > 0):
			if naomi[0] > ken[0]:
				del naomi[0]
				del ken[0]
				dscore = dscore + 1
			else:
				del naomi[0]
				del ken[-1]
			N = N - 1

		dscore = dscore + len(ken)

		# print results
		ss = "Case #"+ str(count) + ": " + str(dscore) + " " + str(score)
		print(ss)

	pass

if __name__ == '__main__':
	main(sys.argv)
