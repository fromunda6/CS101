life = [1,2,3,4]

def unit_4(time,attention):
	name="Responding to Queries"
	while (learning):
		time --
		attention --
		mkt_value ++
	return mkt_value

life.count()

# In completing the web crawler, redefined below, we have left out how to respond
# to queries; or more fundamentally, how to make our program behave with anything
# more than on/off functionality.  Namely, responding to user input, in the for
# of web queries.  CS: How to use and build complex data structures such that, with
# respect to our web-crawler-soon-to-be-search-engine, an efficient traversal of all
# data comprising our hypothetical www can be achieved

# involves:
	# an inverted index (allows for a MAPPING between keywords and pages
	# containing those kehywords)

# so for our Search engine, we want to build an index that allows for
# mapping between keywords, and the pages on which those keywords can be found

# the crawler, in order of increasing dependency

page = "contents of some ancient, text-only webpage"

def get_next_target (page):
	start_link = page.find ('<a href=')
	if page.find == -1:  #return value of fruitless ".find" method
		return None, 0
	start_quote = page.find ('"', start_link)
	end_quote = page.find ('"', start_quote+1)
	url = page[start_quote+1 : end_quote]
	return url, end_quote

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

def Crawler:
	tocrawl =[seed]
	crawled = []
	while tocrawl: # read as while tocrawl is non-empty, execute block
		page = tocrawl.pop()
		if page not in crawled:
			union (tocrawl,get_all_links(get_page(page)))
			crawled.append(page)
	return crawled


# How to represent the index for our web content corpus (what's the best
# data structure (chosen from amongst Python data structures)):

# the data structures of 4.03, in words:

#1: a single list, with every element subscripted to required specificity
#2: a list for each occassion of keyword/url as individual elements
#3,4: further separation of data..

# Conceptually, and in constructing our index, a series of lists where element
# 0 is the keyword in each list, and element 1 is a list of all URLs in which tha
# keyword is found
#
