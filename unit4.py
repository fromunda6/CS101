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
# more than on/off functionality.  Namely, responding to user input, in the form
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


#given a single webpage, returns the first website encountered and its ending location

def get_next_target (page):
	start_link = page.find ('<a href=')
	if page.find == -1:  #return value of fruitless ".find" method
		return None, 0
	start_quote = page.find ('"', start_link)
	end_quote = page.find ('"', start_quote+1)
	url = page[start_quote+1 : end_quote]
	return url, end_quote

#given a single webpage, accumulates all links within a page

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

#given a starting url and a list of pages already crawled, accumulates all uncrawled material, crawls it for links, and repeats until no urls remain

def crawl_web(seed):
	tocrawl =[seed] #initialize tocrawl to the seed, a list containing just the seed
	crawled = []  #initialize crawled to empty list storage for pages
	while tocrawl: # read as while tocrawl is non-empty, execute block
		page = tocrawl.pop() #use last item in list tocrawl as var page
		if page not in crawled:
			union (tocrawl,get_all_links(get_page(page))) # UNION into tocrawl all the links we can find on that page
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

# Quiz: Define a procedure, add_to_index, that takes 3 inputs:
# an index (as decided previously), a keyword, and a url:
	#if keywird EXISTS, add url to list of url associated with that index
	#if keyword not_found, add an entry to the index, being:
		# [keyword, [url]]


index = []
def add_to_index(index,keyword,url):
	for entry in index:  #entry could be anything - here just represents a unique combo of two input vars, one of which contains the other ...
		if entry[0] == keyword: #equality-testing and if true means new url for keyword already listed
			entry[1].append(url)
			return
	#not found, add a new entry
	index.append([keyword,[url]]) #in the case where the keyword was not found in the index

# Lookup on the index

def lookup(index, keyword):
	for entry in index:  #in addition to setting the target through which to loop, what's crucial is the creation of entry as the name of each element in index;#this presupposes and requires that index be fed to the function in a appropriate form, in this case at a minimum that it is a list
		if entry[0]==keyword:		 #ENTRY must be a list as well, otherwise this means nothing
			return entry[1]
	return []

# In effect, what we now need to build is an index for our web crawler, such that we can encapsulate the functionality of the existing crawler inside a user-driven keyword search

index=[]

#define a function that adds to our index in the form defined in 'add_to_index' the entire text contents of a page - only new thing here is that where we formerly gave add_to_index a keyword, that input parameter is now derived...
def add_page_to_index(index,url,content):
	words = content.split()
	for word in words:
		add_to_index(index,word,url)  #don't get confused - the variable 'word' is here passed in to fxn as parameter 'keyword'


#alter crawl_web such that given only a seed, we can return the content of all pages linked to that url, retrievable as:
# an _index_ composed of organized _content_ that is searchable via ~lookup~ and archived in _crawled_

#also updated to pre-fetch contents of web pages

def crawl_web(seed):
	tocrawl=[seed]
	crawled=[]
	index=[]
	while tocrawl:
		page=tocrawl.pop()
		if page not in crawled:
			content=get_page(page)
			add_page_to_index(index, page, content) #where page is a URL
			union(tocrawl,get_all_links(content))
			crawled.append(page)
	return index

#The internet-how to we retrieve stuff from it; well, via Python, it would be:

	def get_page(url):
		try:
			import urllib
			return urllib.urlopen(url).read()
		except:		#exception handler
			return ""

#Network: a group of entities that can communicate, even though they are not all directly connected
#we use this definition for the purposes of discussing the internet

# A--B >not a network;  A--B--C >A network

#Components of a network:
	#a method of encoding and interpreting messages (smoke signals == specific message)
		#internet: message >> bits >> electrons/photons
	#selective rules of transmission (directing smoke signals)
		#routers
	#rules of access to the network (if you;re a general, your message has priority)
		#internet: best effort service

	#AND, Protocols - or how the client and server talk to each other
		#HTTP: GET <object> ; RESPONSE-CONTENTS OF <object>

#Latency-time that it takes for a message to get from source to a destination
	#measured in milliseconds

#Bandwidth-amount of information that can be transmitted per unit time
	#measured in bits per second or more like mbps

#TraceRoute (tracert hostname in terminal) will trace a network communication route

#-------------------------------------------------------------------------------------------------------------------

# Problem Set #4 (largely conceptual):

# 1) How to modify index to keep track of the # of times users click on a particular link?

	index = [['keyword1', ['url1','count1'],['url2','count2']],['keyword2',['url1','count1']]]

	# like so

# 2) how would certain changes to procs add_to_index and lookup affect our search engine?

	# Previous:

def add_to_index(index,keyword,url):
	for entry in index:
		if entry[0] == keyword:
			entry[1].append(url)
			return
	index.append([keyword,[url]])

def lookup(index, keyword):
	for entry in index:
		if entry[0]==keyword:
			return entry[1]
	return []


	# Proposed:

def add_to_index(index, keyword, url):
	index.append([keyword, url])

def lookup(index, keyword):
	result = []
	for entry in index:
		if entry[0] == keyword:
			result.append(entry[1])
	return result

# Difference is whether we modify locally the 'result' initialized in lookup V2...

# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.


def split_string(source,splitlist):
	output = []
	atsplit = True #indicates we're at a split, and Starts us there
	for char in source: #iterate through string by each letter
		if char in splitlist:
			atsplit = True
		else:
			if atsplit:
				output.append(char)
				atsplit = False
			else:
				output[-1] = output[-1] + char  #again, the [-1] item in a list is that in the last position
	return output

out = split_string("This is a test-of the,string separation-code!"," ,!-")
print out
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']

#4).

# The current index includes a url in the list of urls
# for a keyword multiple times if the keyword appears
# on that page more than once.

# It might be better to only include the same url
# once in the url list for a keyword, even if it appears
# many times.

# Modify add_to_index so that a given url is only
# included once in the url list for a keyword,
# no matter how many times that keyword appears.


# Mine
def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
        	if url != entry[1]:
				entry[1].append(url)
            return
    # not found, add new keyword to index
    index.append([keyword, [url]])

# TA's:

def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
        	if not url in entry[1]:
				entry[1].append(url)
            return
    # not found, add new keyword to index
    index.append([keyword, [url]])



