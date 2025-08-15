def traduce(f):
	''' Traduce de carácter a símbolo '''
	# '♟♜♞♝♛♚' #

	f = f.replace('R', '♜')
	f = f.replace('N', '♞')
	f = f.replace('B', '♝')
	f = f.replace('Q', '♛')
	f = f.replace('K', '♚')
	f = f.replace('P', '♟')

	f = f.replace('r', '♜')
	f = f.replace('n', '♞')
	f = f.replace('b', '♝')
	f = f.replace('q', '♛')
	f = f.replace('k', '♚')
	f = f.replace('p', '♟')

	return f
