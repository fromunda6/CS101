# Unit1 Prob Set

# 2-Write code that prints out the # of hours in 7 weeks:
print (24*7*7)
# 3-Which of the following leaves the value of Var "X" unchanged, assuming
# both a and x are integer values?
# cant draw them here, but the important thing to remember is that you're
# assigning to the left-side variable the value currently assigned to the
# right-side variable,

# 4-write code that stores the distance in meters that light travels in
# one nanosecond in the variable 'nanodistance', where:

speed_of_light=299800000.
nano_per_sec=1000000000.
nanodistance=speed_of_light/nano_per_sec
print (nanodistance)

# strings

# 5-given any string 's', which of the following will always = 's'?

s='duck'
print (s[0]+s[1]) # >>only this one will not

# 6-Given the variables 's' and 't' defined as:
s='udacity'
t='bodacious'
# write code that prints out "udacious", without using quote chars:

print(s[:3]+t[4:])

# 7-use find correctly:

text='whoo'
print (text.find('hoo'))

# 8-assign to the var 'first_zip' the result of a text.find('zip')
# function and use first_zip+1 as the starting point in a second
# text.find('zip',first_zip+1), i think is the solution:

text='zip files are compressed'
first_zip=text.find('zip')

print (text.find('zip',first_zip+1))

# 9-new function 'str' is a format-transform function that turns any input
# into a string, ie

x=27.5
target_num=x+0.5
ex=str(target_num)
x_whole=ex[:ex.find('.')]
print (x_whole)


