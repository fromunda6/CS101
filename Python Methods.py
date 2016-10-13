Python Elements:

	variable
	string
	list - (known in JS as an array) - sequence of anything ['a','b','c','!']
	procedure

Python Methods learned thus far (a living reference):

	# create and assign a value to a variable
	var_name = constant, function, range, series, (...anything?)

	# return a character in position[#] from variable theta
	theta[0]

	# ret_Char from position[#] to the end of vari
	vari[0:]

	# ret_Char before position[#]
	var_name[:5]

	# return item in nested list [[a,b],[c,d]]
	nList[1][0]
	# returns 'c'

	# return position of specified value within list

	<list>.index(<value>)

		or p=['dog','cat','monkey'] >> p.index('monkey') >> 2

	# find and return the position of a substring in a string, with optional param = position at which to start searching
	var_name.find("certain string", 4)

	# display a variable in ui
	print (var_name)

	# define a procedure
	def proc_name(input1, input2):
		task1 = var_name.find("certain string")
		task2 = task1[2:4]
		return output1, output2 #must be something computed by the procedure, i.e. task1, task2

	# loop through a 'block' of operations while a condition(s) remains true, requiring
	# only that a way to exit the loop is built into the code block
	while i<10:
		print i
		i = i + 1

	# loop through a list:

	def print_all_elements(p):
		for e in p:
			print e

	# append 'wholesale' to an existing list

	<list>.append(<element>)

	[1,2].append[3,4] >> [1,2[3,4]]

	# integrated append

	[1,2].extend[3,4] >> [1,2,3,4]

	# pop

	x = [1,2,'b']
	x.pop() >> 'b'
	x= [1,2]

	# conditionals

	if <test expression>:
		<code to execute>

	# 'in' (outside of for loop) checks presence/absence of a target value
	# in a specified list, ie
	<value> in <list>
	<value> not in <list>
	p=[0,1,2]
	print (3 in p) #returns false

Python Color-Coding:

# 1). recognized non-string datatypes (numbers and boolean values, maybe othere(?)) are in purple:

	3.2, 2500, True, False #boolean values are only recognized in lowercase

# 2). strings, besides the obvious '' and "" identifiers, will always show up in

	"pale yellow"
