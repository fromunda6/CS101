# this unit introduces the next big idea needed for a web crawler,
# which is structured data, comprising:
	# Strings - a sequence of characters, i.e: s = 'yabba'

		# s[0] >> 'y' ; s[2:4] >> 'bb'

	# Lists - a sequence of anything, i.e: p = ['y','a','b','b','a']

		# p[0] >> 'y' ; p[2:4] >> ['b','b']

# Generalized grammar for lists:
	# <list> >> [<Expression>,<Expression>,<Expression>]

stooges = ['Moe','Larry','Curly']

# Given the variable
	days_in_month = [31,28,31,30,31,30,
						31,31,30,31,30,31]
# define a proc how_many_days that takes as input a
# number representing a month, and outputs the number of days
# in that month

days_in_month = [31,28,31,30,31,30,
						31,31,30,31,30,31]

def how_many_days(month):
	return days_in_month[month - 1]

#accounting for the fact that indexing begins at 0, not 1
# such that days_in_month[1] = February, nor January

# Nested lists

mixed_up = ['apple', 3, 'oranges', 27, ['alpha', 'beta']]

beatles = [['John', 1940], ['Paul', 1942], ['George', 1943], ['Ringo', 1940]]
			]
>>> print(beatles[1])
 ['Paul', 1942]
>>> print(beatles[0][1])
1940
>>>

# Given the variable countries defined as:
countries = [['China', 'Beijing', 1350],
			['India', 'Delhi', 1210],
			['Romania', 'Bucharest', 21],
			['United States', 'Washington', 307]]
# write code to print out the capital of india:

print (countries[1][1])

def multiple():
	c = countries[0][2]
	r = countries[2][2]
	return c/r

print (multiple())

# The other important difference between strings and lists concerns
# a lists' ability to handle Mutation,

# Mutation, simply put, refers to the ability of a variable to
# change after being created; dynamic, in motion, etc
# this is conceptually distinct from reassignment; when a VAR
# s initially refers to one string value, and thru reassignment now
# refers to another string value, or a concatenation of strings, we've not
# really changed the string, only the assignment value of the VAR to which
# it was heretofore attached.  With lists, the values themselves can
# change

p = ['H','e','l','l','o']
p[0] = 'Y' #this mutates the list into:
p = ['Y','e','l','l','o']

# Suppose that:

q = p
q[4] = '!'  ,

# since q = p, p[4] = '!'

# All this touches on the broader idea of mutability.  So...Immutability
# means a thing can't be mutated; not that it can't be muted/silenced?

# When we have two names for the same thing...enter
# ALIASING
# Quiz: suppose we run:

spy = [0,0,7]
agent = spy
spy[2] = agent[2] + 1

# what, now, is the value of:

agent[2] >>> 8

# when element 2 of spy is changed, agent is changed and agent[2] is changed

# Def a proc, replace_spy, that takes a likst of 3 and modifies 3rd
# to be one more than previous

def replace_spy([n1,n2,n3]):  #INVALID SYNTAX - CANNOT PASS LIST AS INPUT PARAMETER
	return [n1,n2,n3+1]

replace_spy(0,0,7)

def replace_spy(p):
	p[2] = p[2] +1

# to pass a list to a function, must first assign that list to
# a singular variable

# the important idea in this section is mutable v immutable objexts
# List operations:
	#appending, perhaps: <list>.append(<element>)

			stooges = ['Moe','Larry','Curly']

			stooges.append('Shemp')

			stooges >> ['Moe','Larry','Curly','Shemp']

	# + operator:
			[0,1] + [2,3] >> [0,1,2,3] #this is not concatenation
	# len operator:
			len(<list>) #returns the # of elements in the input
			len([0,1]) >> 2
			len(['a', ['b',['c']]]) >> 2
			len("Udacity") >> 7

# Quizzes: List operators:


