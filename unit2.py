# L2 lessons/problem set

# goal of this lesson is to build out the web crawler such that it can find all the links in a page,
# which requires the introduction of two new big programming concepts :
	# Procedures (JS: functions) - way to package up code for ease of use
	# Control (JS: loops) - provides structure that enables us to make decisions and perform repetition

# going back to unit 1, we did these in order to find the first link on a given page:

page = ...contents of some web page...

start_link = page.find ('<a href=')
start_quote = page.find ('"', start_link)
end_quote = page.find ('"', start_quote+1) #returns the first instance of a '"' after 'start_quote'
url = page[start_quote+1 : end_quote]
print url
# to find the 2nd link, we would repeat the process, redefining our starting point 'page' as = to the end_quote defined
# in the prior operation
page = page[end_quote:]

start_link = page.find ('<a href=')
start_quote = page.find ('"', start_link)
end_quote = page.find ('"', start_quote+1)
url = page[start_quote+1 : end_quote]

print url

#as you can see, this procedure exhibits significant repetition, making it a candidate for procedure & control methods
# the only thing differing from iterations #2 : end; being the page variable;
# we can define a procedure with an input=the thing that's changing (page variable, here), a procedure=what happens to the input,
# and an output=the desired end point (URL, in this case)

# the concept is no different (and in fact derives from) than that used in arithmetic and math in general, ie
# +(1,2) could be interpreted as performing the procedure (addition) upon the input values (1,2) and obtaining an output (sum)

# gen syntax:
def <name>(<parameters>):
	block #where block contains our procedures, and parameters are are input values or variables
# creating a procedure (prerq: understandwhat inputs and outputs should be)
# ex:

def get_next_target (page) # W.R.T. our procedure, we know the input should be a string giving the contents of the rest of the page,
# but what should the proc output such that we can continue to find the next URL?  'end_quote', as it is necessary for the first
# operation in the proc, that of substituting for the original value of page the value of page[end_quote:]

s=s[end_quote:]

def get_next_target (s):
	start_link = s.find ('<a href=')
	start_quote = s.find ('"', start_link)
	end_quote = s.find ('"', start_quote+1)
	url = s[start_quote+1 : end_quote]
	return url, end_quote

# there need not be outputs, as procs can do other things beisdes mapping inputs to outputs, such as printing items computed by the proc but not output by it

# USING Procedures
def rest_of_string(s):
	return s[1:]

print rest_of_string('audacity')
# returns udacity

# what does this proc do:
def sum(a,b):
	a=a+b
# sets the value of a equal to the sum of inputs a,b(?)

# sort of, but really in this form, the procedure does nothing; the value of
# 'a' is changed only inside the procedure sum.  To see this:

def sum(a,b):
	a = a + b
	return a

s = 'Hello'
t = 'Dave!'
print sum(s,t) #returns Hello Dave!
print s #returns Hello

# in other words, the variable s has both a global and a local scope, the latter of which holds only within the context of a procedure

def square(n):
	return n * n

x=37
y=square(x)
print square(y) #returns 1874161

# the idea of procedure composition refers only to the reality that most procedures are either components of another procedure or
# 'compound' procedures

# Quiz - def a proc , abbaize, that takes 2 strings as it's input, and outputs a string that is the first input, followed by two
# instances of the second input, followed by the first input

def abbaize(x,y):
	x=x+y
	y=y+x
	return x+y

abbaize(a,b) #returns abba

# also can use:
def abbaize(x,y):
	return x+y+y+x

# superstar quiz - def a proc, find_second, that takes two strings as its inputs: a search string and a target string.
# it should output a number=the position of the second occurence of the target string in the search string

# my answer

def find_second(search,target):
	first=search.find(target)
	second=search.find(target,first+1)
	return (second)

find_second("doggone","g")

# Dave's answer

def find_second(search,target):
	return search.find(target, search.find(target) + 1)

word = "doggone"
print find_second(word, 'g')

# Making decisions Conditionally (how to make code behave differently depending on which data is input)
# operators
<, > <= , >=, !=, == #last is equality comparator

# thus, how to make our code do something different based on the result of a comparison

# gen syntax:

if <test expression> :
	<block> #operations to perform if test expression evaluates to true, go here
i=21 #next left-justfied code will run regardless of the outcome of <test expression>
	def absoluteValue(x):
		if x<0:
			x = -x
		return x

# quiz - define a procedure, "bigger", that takes in two numbers as inputs, and outputs the greater of the
# two inputs

def bigger(x,y):
	if x > y
		return x
	if x < y
		return y
	if x=y
		return "neither"

bigger(2,6)

# or, per teacher Dave:

def bigger(x,y):
	if x > y:
		return x
	return b

	# or

def bigger(x,y):
	if x > y:
		return x
	else:
		return y

# else allows for a single return statement when the <block> is used to assign an addt'l VAR

def bigger(x,y):
	if x>y:
		r=a
	else:
		r=b
	return r

# def a proc that takes a string as its input and outputs a boolean (logical,T/F) indicating whether
# the input string is the name of a friend, where friends' names begin with 'D'

def is_friend(name):
	if name[0]=='D':
		return True
	else:
		return False
is_friend("dave")

# or, we can return the result of the equality test directly, w/o an if statement, like so:

def is_friend(name):
	return name[0] == 'D'

# define a similar proc such that names beginning with either 'D' or 'N'

def is_friend(name):
	return name[0] in ('D','N')

print is_friend("Ned")

# or assuming not having knowledge of "in" statement

def is_friend(name):
	if name[0] == 'D':
		return True
	else:
		if name[0] == 'N':
			return True
		else:
			return False

# or, using or:

def is_friend(name):
	return name[0] == 'D' or name[0] == 'N'

print (is_friend)('Doug')
print (is_friend)('Nicole')
print (is_friend)('Fred')

# to illustrate the logic, and keeping in mind that boolean expressions always check for 'truthness' in Python, at least :

print (True or False) # are either of the values 'True' or 'False' == True?
print (False or True)
print (True or True)
print (False or False)

# An 'or' expression will only evaluate as much as it needs to, e.g.:

print (True or this_is_an_error) #returns 'True'
print (False or this_is_an_error) #returns error/undefined

# super Quiz: def a proc, biggest, that takes 3 numbers as inputs, and outputs the greatest of the 3 numbers:

def biggest(x,y,z):
	if x > y:
		if x > z:
			return x
		else:
			return z
	else:
		if y > z:
			return y
		else:
			return z

# make sure this ^^ terminates, otherwise, "you've got a Dead Baby, and you get an F for the semester"

# or, using your 'bigger' procedure, which "composes two calls to proc 'bigger'" like so:

def biggest(x,y,z):
	return bigger(bigger(a,b),c)

or max() is True def biggest()

# Astounding truly, is that you could write every possible computer program with just the things we've seen up to this point

# specifically, procedures, arithmetic, comparisons and if statements are sufficient to simulate the computing capabilities of any machine

# --------------------------------------------------------------------------------------------------------------------------------------- #

# Loops, while, gen syntax:
	while <test expression>: #as in, while the test expression is true, perform statements in <block>; this will loop endlessly in absence of a false result
		<block>

# EX:

i = 0
while i<10:
	print i #the function needs the value of 'i' within the block...
	i = i + 1

# quiz: what does this program do?
i = 0
while i!=10:
	i=i+1
	print (i)

# def a proc, 'print_numbers', that takes as input a positive integer, and prints out all the whole numbers from 1 to the input number
# toolbox: procedure, while loop, and assignment(new var)

def print_numbers(d):
	i=1
	while i <= d:
		print (i) #the order of print w.r.t. operations changing your iterator matters ; if you had print after operation '1' would not be printed in call
		i = i + 1
print (print_numbers(7))

# Coding a factorial operation ie 5! = (5*4*3*2*1)

def factorial(x):
	result = 1
	while x >= 1:
		result = result * x
		x = x - 1
	return result

	print factorial(4)

# ... ugh

# break statement gives us a way to stop a loop regardless of while's <test expression> being met
# general syntax:

while <testExpression>:
	<Code>
	if <BreakTest>:
		break
	<not executed if breakTest is met>
<executed if breakTest is met>

# again , the goal of today's unit, to write the code that will extract all links from a webpage:

page = ...contents of some web page...

start_link = page.find ('<a href=')
start_quote = page.find ('"', start_link)
end_quote = page.find ('"', start_quote+1)
url = page[start_quote+1 : end_quote]
print url
page = page [end_quote:]

start_link = page.find ('<a href=')

def get_next_target (page):
	start_link = page.find ('<a href=')
	start_quote = page.find ('"', start_link)
	end_quote = page.find ('"', start_quote+1)
	url = page[start_quote+1 : end_quote]
	return url, end_quote # in order to return two values, must make use of multiple assignment, via

url, endpos = get_next_target(page) #assigns to url, endpos(ition) the output of the proc url, end_quote, respectively
print url


s , t = t , s #this is useful for swapping values that cannot be done in two sequential assignment statements,
# since:

s = t
t = s

# changes s to the value of t and does not change the value of t

# what our function is missing is instructions on how to respond to an absence of any links (below: 'if url: ... else: break'), and also a way to stop looking
# (below: 'if page.find == -1: return None, 0')

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

# Main Concepts so far
# unit 1 : variables, arithmetic
# unit 2 : procedures, if, while








