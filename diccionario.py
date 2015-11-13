import itertools
res = itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=2) # 2 is the length of your result.

for i in res:
	varA = ''.join(i)
	res2 = itertools.product('0123456789', repeat=4) # 4 is the length of your result.
	for x in res2:
		varB = ''.join(x)
		print varA + varB

#for i in res:
#	print ''.join(i)
