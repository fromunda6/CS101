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
# such that days_in_month[1] = 28, not 29 (ignoring leap year)

# Nested lists

mixed_up = ['apple', 3, 'oranges', 27, [1,2['alpha', 'beta']]]

beatles = [['John', 1940], ['Paul', 1942], ['George', 1943], ['Ringo', 1940]]

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
# a lists' ability to handle MUTATION,

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

# Ex, a string cannot be mutated in the same way as a list

s = 'Hello'
s[0] = 'Y' #invalid python

# When we have two names for the same thing...enter
# ALIASING
# Quiz: suppose we run:

spy = [0,0,7]
agent = spy
spy[2] = agent[2] + 1

# what, now, is the value of:

agent[2] >>> 8

# when element 2 of spy is changed, agent is changed and agent[2] is changed

# Def a proc, replace_spy, that takes a list of 3 and modifies 3rd
# to be one more than previous

def replace_spy([n1,n2,n3]):  #INVALID SYNTAX - CANNOT PASS LIST AS INPUT PARAMETER
	return [n1,n2,n3+1]

replace_spy(0,0,7)

def replace_spy(p):
	p[2] = p[2] +1

# to pass a list to a function, must first assign that list to
# a singular variable

# this should be recognized as distinct from methods like:

def inc(n):
	n = n+1
a = 3
inc(a) #does not change the value 'a' refers to

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

#what is the value of len (p) after running this code:

p = [1,2]
p.append (3)
p = p + [4,5]  #this is a bit confusing, but this is a concatenation of two lists, not an append operation
# que es len(p) ?
5

# and:

p=[1,2]
q=[3,4]
p.append(q)
len(p) #evaluates to 3
print(p) # [1,2[3,4]]

# How Computers Store Data

# fastest access memory is stored in 'Switches' somewhere;
# next quickest is right on the processor, only a few kbs, stored on the CPU 'Register'
# the slower kind (your RAM) is stored in 'Capacitors' as DRAM
# slowest is disk memory

# Units of Memory

2 ** 10 # 1 024 b, 1kb
2 ** 20 # 1 048 576 b, 1mb
2 ** 30 # 1 073 741 824 b, 1gb
2 ** 40 # 1 099 411 627 776 B, 1tb

# and 1 byte = 8 bits...a 2gb ram stick represents ~ 17 billion 'buckets'

# Looping through a list

while <test expr> :
	<block>

# how to loop through a list, quiz:

def print_all_elements(p):
	i = 0
	while i < len(p):
		print p[i]
		i = i + 1

# FOR loops

for <name> in <list>:
	<block>

# Quiz: Def a proc, sum_list, thjat takes as its input a list of numbers and produces
# as outsup the sum of all the elements in the input list. i.e.

def sum_list(p):
	result = 0
	for e in p:  #read as "each time we execute the block,
	# the value of element (e) will equal the current value of p"
		result = result + e
	return result

#Teacher's:

def measure_udacity(U):
	count = 0
	for e in U:
		if e[0] == 'U':
			count = count+1
	return count

# quiz : Define a procedure, find_element, that takes as
# its inputs a list and a value of any type, and outputs the
# index of the first element in the input list that matches the
# value; if no match, output -1

# Teacher-while loop

def find_element(p,t):
	i=0
	while i<len(p):
		if p[i] == t:
			return i
		i = i+1
	return -1

# Teacher-for loop

def find_element(p,t):
	i=0
	for e in p:
		if == t:
			return i
		i=i+1
	return -1

def find_element(l,n):
	if(n in l):
		return l.index(n)
	else:
		return -1

def find_element(l,n):
	if n not in p:
		return -1
	return l.index(n)

# Define a proc, union, that takes as inputs two lists.  It
# should modify the first input list to be the set union of
# the two lists

def union(l,s):
	for e in s:
		if e not in l:
			l.extend(e)

# Assume p refers to a list with at least two elements.  which of
# these code fragments does not change the final value of p:

# ___________________________________________________________________ #
# Web Crawler:
	# Collecting links:

# as of the end of unit#2:

def get_next_target (page):
	start_link = page.find ('<a href=')
	if page.find == -1:
		return None, 0
	start_quote = page.find ('"', start_link)
	end_quote = page.find ('"', start_quote+1)
	url = page[start_quote+1 : end_quote]
	return url, end_quote


def print_all_links (page):
	while True:
		url, endpos = get_next_target(page)
		if url:
			print url
			page=page[endpos:]
		else:
			break

# rather than simply printing the links as we go, how do we collect them in a
# way that makes them usable:

# def a proc 'get_all_links' that does more or less what print_all_links does but
# collects (i'm thinking append/extend lists) all the links inside a list(I'm assuming)

links = get_all_links(get_page('hhtp://www.udacity.com/cs101x/index.html'))
print links

# lets break this apart a little bit - print_all_links needs a few changes in any case
	# a list variable to collect links in
	# a method for accumulating links inside that list
	# produce output

#a)what should the initial value of 'links' be set to

def get_all_links(page):
	links = []
	while True:
		url,endpos = get_next_target(page)
		if url:
			links.append(url)
			page = page[endpos:]
		else:
			break
	return links

	# ______________________ Finishing the web crawler #

# We must also bring some order to the sequential crawling that is sensible
# traceable, and non-random.  Rather, do we crawl every branch of the first link
# or crawl every link of the seed page  . . .

# Method chosen here is known as a "Depth-First Search"

seed = 'http://www.udacity.com/cs101x/index.html'

# however the current test group of sites is a closed loop, as is much of the web

def Crawler:
	tocrawl =[seed]
	crawled = []
	while tocrawl: # read as while tocrawl is non-empty, execute block
		page = tocrawl.pop()
		if page not in crawled:
			# update the value of tocrawl
			# update crawled
	return crawled

	def Crawler:
	tocrawl =[seed]
	crawled = []
	while tocrawl: # read as while tocrawl is non-empty, execute block
		page = tocrawl.pop()
		if page not in crawled:
			union (tocrawl,get_all_links(get_page(page)))
			crawled.append(page)
	return crawled

# Awesome.  We have taken what would have been a daunting task asnd broken it into manageable
# components.  This ability is essential to pushing personal limits/learning and applying new
# skills...



# _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ PROBLEM SET #3_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ #


# given an empty set [p] and three transformations,
# populate the set such that p = [1,2,3] after the execution
# of three transformations:

p[0] = p[0]+p[1] = 1
p[1] = p[0]+p[2] = 2
p[2] = p[0]+p[1] = 3 #known from final values

# Example p = [1,1,1] //>>

#Mutating lists:

#beginning with p = [1,2,3], we perform some operations

# terrible presenter is the TA . . .

# def proc product_list(p) such that the list elements in p are multiplied together
#regardless of the composition of p:

def product_list(p):
	total = 1
	for i in p:
		total = total*i
	return total

# def a proc, greatest, that takes as input a list of positive #s
# and outputs the greatest # in that list; if the list is empty , output=0

list_of_numbers = [2,5,7]

def greatest(p):
	big = 0
	for i in p:
		if i>big:
			big = i
	return big























