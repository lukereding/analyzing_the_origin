# text mine an origin of species
#

## getting a list of all the unique words and how many times each was used:

import re
from collections import Counter
cnt = Counter()

# read it in, make lowercase
text = open('/Users/lukereding/Desktop/analyzingTheOrigin/origin.txt').read().lower()

# get rid of digits
text = re.sub("\d+","",text)

# remove carriage returns and line breaks
text = text.replace('\n', ' ').replace('\r',' ')

# remove punctation
text = re.sub('[?!,.;:\]\[{}\'\"]+', "", text)
# if you want to preserve sentences, use:
# text = re.sub('[,;:\]\[{}\'\"]+', "", text)

words = re.findall('\w+',text)

# words = re.findall('\w+', open('/Users/lukereding/Desktop/origin.txt').read().lower())

# use counter from collections to create a dict where the key is the word and the answer is the count
Counter(words).most_common(1000)


# writing the results to a csv file

import csv
file = csv.writer(open("/Users/lukereding/Desktop/mostCommonWords.csv", "wb"))
for key, count in Counter(words).iteritems():
    file.writerow([key, count])


### idea: plot the position of the word i.e. 1000/907368 against the number of letters in that word, format like a manhattan plot

file2 = csv.writer(open("/Users/lukereding/Desktop/lengthVsPosition.csv", "wb"))
counter = 1
numberOfLetters = []

for word in words:
	numberOfLetters.append(len(word))
	file2.writerow([counter,word,len(word)])
	counter+=1

# to find the positions of chapters to alternate colors:
# re-read in the origin. perserve figits.
# chapters are labeled like '14. VARITATION.'
re.findall('[0-9]+\.\s[A-Z][A-Z\s]+\.',text) # should give the names of all the chapters

p = re.compile("[0-9]+\.\s[A-Z][A-Z\s]+\.")
for m in p.finditer(text):
    print m.start(), m.end(), m.group()



## actually makybe try this based on sentence length, which will be more variable. use .split() based on periods
import re
text = open('/Users/lukereding/Desktop/origin.txt').read()
# remove carriage returns and line breaks
text = text.replace('\n', ' ').replace('\r',' ')
# remove punctation except periods, ?, and!
text = re.sub('[,;:\]\[{}\'\"]+', "", text)

# find all the sentences by matches cases were you see a period followed by a space and a capital letter
# note this this isn't perfect; consider how it handles H. M. S, Beagle.
sentences = re.findall('[A-Z][^\.!?]*[\.!?]',text)

import csv
file = csv.writer(open("/Users/lukereding/Desktop/wordsBySentence.csv", "wb"))
counter = 1
for sentence in sentences:
	numberOfCharacters = len(sentence)
	numberOfWords = len(re.findall('\w+',sentence))
	file.writerow([counter,numberOfCharacters,numberOfWords])
	print counter,numberOfCharacters,numberOfWords
	counter+=1

# to find out the positions where the chapters start to color-code the manhattan plot is a little tricky
# remember that we said sentences had to start with A-Z, so the chapters are not included
joinedSentences = '. '.join(sentences)
# why doesnt this work?
re.findall('[^0-9]+\.\s[A-Z][A-Z\s]+\.',joinedSentences)


# instead, let's grab the text the follows the heading of each chapter like this:

p = re.compile("[0-9]+\.\s[A-Z][A-Z\s]+\..{50}")
for m in p.finditer(text):
    print m.start(), m.end(), m.group()

# ok, now we match the start of each chapter to where it occurs in our sentences object. I'll just do this one-by-one:
[i for i, x in enumerate(sentences) if re.search("Causes of Variability", x)] # chapter 1 starts at sentence 59
[i for i, x in enumerate(sentences) if re.search("Causes of Variability", x)] # chapter 2 at 416
[i for i, x in enumerate(sentences) if re.search("The term used in a", x)] # chapter 3 starts at 574
[i for i, x in enumerate(sentences) if re.search("Natural Selection its power compared with", x)] # chapter 4 starts at 753
[i for i, x in enumerate(sentences) if re.search("Effects of external conditions", x)] # chapter 5 begins at 1183
[i for i, x in enumerate(sentences) if re.search("Difficulties on the theory of descent with", x)] # chapter 6 begins at 1534
[i for i, x in enumerate(sentences) if re.search("Instincts comparable with habits but different", x)] # chapter 7 begins at 1822
[i for i, x in enumerate(sentences) if re.search(" Distinction between the sterility of first", x)] # chapter 8 beings at 2151
[i for i, x in enumerate(sentences) if re.search("On the absence of intermediate varieties", x)] # chapter 9 begins at 2458
[i for i, x in enumerate(sentences) if re.search("On the slow and successive appearance", x)] # chapter 10 begins at 2732
[i for i, x in enumerate(sentences) if re.search("Present distribution cannot be accounted for", x)] # chapter 11 begins at 3016
[i for i, x in enumerate(sentences) if re.search("??", x)] # chapter 12 begins at ??
[i for i, x in enumerate(sentences) if re.search("MORPHOLOGY  EMBRYOLOGY RUDIMENTARY ORGANS", x)] # chapter 13 begins at 3578
[i for i, x in enumerate(sentences) if re.search("Recapitulation of the difficulties on the", x)] # chapter 14 begins at 3977

# I'll import this list of starting points into R and color-code based on them

#### idea: make a dendrogram based on words that are mostly likely to be found near each other / network analysis


#### some sort of network analysis

#### Find some distance between top 100 words, make different plots

### basic histogram of word length of unique words, white on black background
