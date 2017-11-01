#max = 0

def maximum_value(foo):
	#global max
	max = 0
	for i in range(len(foo)):
		if max < foo[i]:
			max = foo[i]
	return max


#foo = ('a', 'b', 'c')
foo = ['dinesh', 'alessandra']
#maximum_value(foo)
highest = maximum_value(foo)
print(highest)

