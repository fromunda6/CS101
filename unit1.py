# write a program that prints out the number of
# minutes there are in seven weeks
print (60*24*7*7)

# how far, in cm, does light travel in one nansecond?
print ((299792458*100)/1000000000)

# variable assignment example
speed_of_light = 299792458 # meters per second
billionth = 1.0/1000000000
nanostick = speed_of_light * billionth * 100
print (nanostick)
cycles_per_second = 2700000000 # or 2.7ghz

# ? How far does light travel, in metres, in a single computer cycle?

print (speed_of_light/cycles_per_second)

# illustrating the essential characteristic of variables, namely that they
# can vary:

cycles_per_second = 2800000000 # or 2.8ghz
lightmetres_per_cpu_cycle = (speed_of_light/cycles_per_second)

print (lightmetres_per_cpu_cycle)

# illustrating reassignment:

hours = 9
hours = hours + 1
hours = hours * 2
print (hours)

# VAR quiz lesson #34:
# print out the number of days you've been alive,
# defining variables to the maximum accurate granularity

age = 32
days_per_year = 365.25
days_elapsed_since_bday = 108

age_in_days = (age*days_per_year+days_elapsed_since_bday)

print (age_in_days)

# Strings

print ('this is a string')
print ("I'm also a string")

name='Greg'
print (name[2]) #eval to 'e'
print (name[-1]) #evaluates to 'g'

word = 'assume'

print (word[3]) # returns 'u'
print (word[3:4]) # returns 'u'
print (word[3:3]) # returns nothing
print (word[4:6]) # returns me
print (word[4:]) # returns me
print (word[:2]) # returns
print (word[:])

s='audacity'
print ('U'+s[2:])

test='ab'
print (test[0:-1+1])

# quiz lesson #49
# For Any string, s='<any string>', which of these is always equivalent to s:
# s[:] >> true
# s + s[0:-1+1] >> true
# s[0:] >> true
# s[:-1] >> false

print (s[:-1]) # being that substr stops one position before that given
# on the right side of the colon, this will always truncate the last char

# s[:3] + s[3:] >> true
# this might explain why s[:5] will stop at position 4, as when the start
# of one substr is also the beginning of another...

# FIND - a proc built-in to python that operates on strings, ex:

# General form: <string>.find (<string>) >> returns the position
# in the first string where the second string begins, if it is found.
# Where multiple occurrences of the target string exist within
# the search string, only the first is returned; if it is not found
# [-1] is returned

pythagoras = 'There is geometry in the humming of the strings, there is music in the spacing of the spheres'
print (pythagoras.find('string'))
print (pythagoras[40:])

# lesson #55 - find pt.2

# we can pass the procedure a second parameter, namely the <number> in
# the string at which you want to begin searching, ie:
# <string>.find(<string>,<number>)

friskem = 'word donkey word'
print (friskem.find ('word', 4)) #returns 12, as the fxn begins looking at position 4,
# the space between the first 'word' and 'donkey'

# at this point we know enough to start building our web crawler,
# which can be made to extract links from websites; what we're replicating
# is a search of any webpage the giveawway string '<a href="url" indicating an
# external link

# assume we've already extracted the entire source code of a given page and
# stored it in the variable 'page'

# my first idea:

start_link = page.find("<a href=")
end_link = start_link.find('"',1)
url =[start_link:end_link]

# the right answer:

start_link = page.find("<a href=")
start_quote = page.find('"',start_link)
end_quote = page.find('"',start_quote+1)
url = page[start_link+1:end_link]
