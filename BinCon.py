#file name == BinCon.py
#Binary converter by Menux

try:
	dec = int(input('Enter decimal number: '))
	two = 2
	dec *= two
	binarray = []

	if dec > 1:
		while dec > 1:
			dec //= two
			rem = dec % two
			binarray.append(rem)
		binarray.reverse()
		print (binarray)
	else:
		print ('Values lesser than 1 are not supported!')

	except NameError:
		print ('Error: Incorrect decimal value entered!')
	except ValueError:
		print ('Error: Incorrect decimal value entered!')


# Improvised array reverse function------------------------------------------------------------------------
'''
arlen = len(binarray)
modlen = arlen + 1
nlen = arlen - modlen
binlist = []

while arlen>=1:
	binlist.append(binarray[nlen])
	arlen -= 1
	nlen = arlen - modlen
print 'The binary equivalent of ', num, ' is ' , binlist
'''
#----------------------------------------------------------------------------------------------------------
