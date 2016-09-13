# Unit 2.5 - How to solve problems, in this case:

# Given your birthday and the current date, calculate your age in days?

# ¡¡ Before proceeding with ANYthing, making sure we understand the problem (or question posed) will put us
# on a solid foundation to develop a solution
	# What does this mean?  We can simplify the notion of problem if we
	# restrict ourselves to computational problems; in that case, a problem
	# is defined by possible inputs (a set), desired outputs, and the
	# relationship between the two
# Under this definition, a satisfactory solution is a procedure that can
# transform any input into an output that satisfies the relationship previously
# defined, in this case that the output is = to the # of days between your B'day
# and the current date

# Rules to understanding all problems in the Galaxy:

# 0. Don't Panic

# 1. Identify and constrain, as necessary,the inputs.  In this case two dates
	#1a. ID assumptions/restrictions on inputs; in this case "which calender"?,
		# the length of years in days/what a leap year entails, and "second date must
		# not occur before first date", respectively. Restrictions can be incorporated and/or
		# assumptions checked in what can be referred to as "defensive programming"
	#1b. How are inputs represented/what is the agreed-upon format?
		# in this case,
		def daysBetweenDates(year1,month1,day1,year2,month2,day2)

# 2. Identify the outputs
	#2a. QUIZ: how should we specify the output, PRINT or RETURN?
		# Looking again at the problem statement, we are told to "calculate your
		# age in days", thus we must output a count of days (rather than a count of
		# years, months, and days)
	#2b. Restate the problem sentence as a problem statement that incorporates
	# our greater understanding of the problem (ie inputs, outputs, restrictions
	# formats, assumptions, etc):
		# Define a procedure, daysBetweenDates, that takes two dates as inputs
		# and returns the number of days between the first date and the second
		# date.  Each date is passed in (parameterized) as three numbers giving
		# a valid year, month, and day in the Gregorian calendar.  The second
		# date must not be before the first.

# 3. Understand the relationship between inputs and outputs by working out
# some examples, ie.:
	# i) daysBetweenDates(2012, 12, 7, 2012, 12, 7) returns 0
	# ii) daysBetweenDates(2012, 12, 7, 2012, 12, 8) returns 1
	# iii) daysBetweenDates(2012, 12, 8, 2012, 12, 7) undefined (invalid dates-time moves forward)
	# iv) daysBetweenDates(2012, 6, 29, 2013, 6, 29) returns 365
	# v) daysBetweenDates(2012, 6, 29, 2013, 6, 31) undefined (invalid date-no June 31st in Gregorian calendar)

# 4. Consider systematically how a human solves the problem, and 'experiment'
# with specific instances of a systematic process, ie:
	# daysBetweenDates(2013, 1, 24, 2013, 6, 29)
	# I would...stack the dates as in a composite subtraction problem and approx-
	# imate the answer assuming 30 days in a month ie:
		# 2013 6 29
		# 2013 1 24
		# =000 5 05 =155
	# Teacher does...
		# days left in January = 7
		# count Feb, Mar, Apr, May = [28,31,30,31]
		# days incl in June = 29
	#4a. Consider whether we have enough information to codify, as an algorithm,
	# the steps we took as a human, in pseudoCode, which gives leeway to code
	# precision in order to capture the central ideas quickly, in a notational format of some sort:

		# account for month in which counting begins:
			# days = # of days in month1 - day1 >> 31 - 24 = 7
		# indicate having accounted for days in month 1:
			# month1 += 1
		# repeat the process of counting nearly identical day-groups(months)
			# while current month < target month:
				# days += # of days in month1
				# month1 += 1
		# increment the days included in the ending month, from 1 to enddate:
			# days += day2
		# account for years, (unnecessary for this particular prob)
			# while year1 < year2:
				# days += days in year1
# 5. Don't optimize prematuraly!! Simple and correct is always preferable to
# 'elegant' or fast

# This procedure does not account for many cases:
	# -input dates in same month -month2 < month1, year2 > year1, leap years
# So we begin again...as a computer would/at the other extreme, by maximizing systematization:

	days = 0
	while date1 < date2:  # how is this operationalized
		date1 = day after date1
		days += 1

# the upshot: humans like to take shortcuts, account for special cases as
# they arise, and bring as much formula to a prob as possible, but this can
# make for needlessly complex code; fully simplified, explicit, as-much-detail
# as necessary instruction-following is what computers are good at, so we take
# advantage of that in the 2nd solution immediately above ^

# at this point it is recommended to "divide and conquer" - breaking up the
# problem into 1)logical and 2)manageable parts will enable us to make
# progress and TO KNOW that we're making progress rather than potentially
# becoming frustrated trying to solve the whole problem in one go, so (and
# again using our fully-explicated problem statement):

	#a) define a procedure nextDay(year, month, day) that takes as input a
	# valid date in the Gregorian calendar encoded as the year, month, and
	# day as numbers, and returns the next day as a [year, month, day]
	# assume: all months have 30 days

def nextDay(year,month,day):
	if month < 12:
		if day < 30:
				day = day + 1
		else:
			day = 1
			month = month + 1
	else:
		if day < 30:
			day = day + 1
		else:
			day = 1
			month = month + 1
			year = year + 1

	return year, month, day

nextDay(2016,8,8)

# functionally equivalent yet way simpler Instructor solution:

def nextDay(year, month, day):
	"""warning: this version incorrectly assumes all months have 30 days"""
	# ^ is a docString, a special comment that will show up in code runners where
	# the associated function, (in this case "nextDay") is invoked
	if day < 30:
		return year, month, day + 1
	else:
		if month < 12:
			return year, month + 1, 1
		else:
			return year + 1, 1, 1

nextDay(2016,8,8)

_________________________________________________________________________

# Cool - next, and rather than refining to completion "nextDay", it is recommended
# (and Greg learns better) that we tackle other major conceptual gray areas and become
# sure in the process that the problem is solveable and that we're on the right track

# Define an(approximate) daysBetweenDates procedure that would produce the correct
# results given a correct nextDay procedure.  With a "draft" nextDay fxn, our
# results will be approximately correct

# my attempt:
def daysBetweenDates(year1,month1,day1,year2,month2,day2):  # ex. values: (2016,8,1,2016,8,8)
	days = 0
	while year1 < year2:
		# send to results the days remaining in year1
		year1 = year1 + 1
	if year1 == year2:
		while month1 < month2:
			# add to results the # of days remaining in month1
			month1 = month1 + 1
		day2 - day1 #+ add this to "results"


# Teacher's pseudocode:

days = 0
while date1 is before date2: #helper procedure will define the condition needed to evaluate the relative positions of date1/date2
	date1 = date after date1 #this is accomplished with nextDay procedure
	days += 1
return days

def dateIsBefore(year1,month1,day1,year2,month2,day2):
	"""Returns True if year1-month1-day1 is before year2-month2-day2.  Otherwise, returns False."""
	if year1 < year2:
		return True
	if year1 == year2:
		if month1 < month2:
			return True
		if month1 == month2:
			return day1 < day2 #effectively, if day1 < day2, TRUE >> dateIsBefore() = TRUE, otherwise false
		return False
# at this point we can build the daysBetweenDates excepting leap year/heterogenous
# month length adjustments

def daysBetweenDates(year1,month1,day1,year2,month2,day2):
	"""Returns the number of days between year1/month1/day1
	and year2/month2/day2.  Assumes inputs are valid dates in
	Gregorian calendar, and the first date is not after the second."""
	assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
	# ^ gen Exception, stops the code if dateIsBefore() is False
	days = 0
	while dateIsBefore(year1,month1,day1,year2,month2,day2): #READ: while the value
	# of dateIsBefore is True
		year1, month1, day1 = nextDay(year1, month1, day1) #set to tomorrow
		days += 1
	return days

# not all months are 30 days; benefit to having waited to solve this bit is
# that we've built the majority of the solution, gained momentum, and isolated
# what the code is still missing

# order of ops for dealing with special cases:
	# in general, it is better to write smaller bits of code and breaking,
	# so that we can test code in piecemeal and in turn isolate potential bugs
	# right off; this approach is also more systematic, easier to reproduce and
	# relate the steps of, etc

def daysInMonth(year, month):
	if month == 1 or month == 3 or month == 5 or month == 7 \
		or month == 8 or month == 10 or month == 12:
			return 31
	else:
		if month == 2:
			return 28
		else:
			return 30
	return 30
def isLeapYear(year):
	# from wikipedia:
	# if (year is not divisible by 4) then (it is a common year)
	# else if (year is not divisible by 100) then (it is a leap year)
	# else if (year is not divisible by 400) then (it is a common year)
	# else (it is a leap year)
	if year % 400 == 0:
		return True
	if year % 100 == 0:
		return False
	if year % 4 == 0:
		return True
	else:
		return False

