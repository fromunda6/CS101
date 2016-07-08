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
		if x<0
			x = -x
		return x



