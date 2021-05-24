import trie
import word_pattern
import re
import gram

MONOGRAMS = gram.Gram(1)
MONOGRAMS.load("grams/monograms.txt")

BIGRAMS = gram.Gram(2)
BIGRAMS.load("grams/bigrams.txt")

TRIGRAMS = gram.Gram(3)
TRIGRAMS.load("grams/trigrams.txt")

QUADGRAMS = gram.Gram(4)
QUADGRAMS.load("grams/quadgrams.txt")

FREQ = {}
with open("frequency.txt","r") as fp:
	for line in fp.readlines():
		if(line.startswith("#")):
			continue
		rank,word,count,percent,cumulative = re.split("\s+",line.strip())
		FREQ[word.lower()] = (rank,count,percent,cumulative)

TRIE = trie.Trie()
TRIE.load_itr(FREQ.keys())
#TRIE.load("words.txt")

ALPHA = "abcdefghijklmnopqrstuvwxyz"

PATTERN = word_pattern.Pattern()
PATTERN.load_itr(FREQ.keys())
#PATTERN.load("words.txt")

#Guess at which fitness function will work best
def guess_fitness_func(S):
	#Is the plain text delimited?
	space,punctuation = 0,0
	for c in S:
		if c in " \t\n":
			space += 1
		elif c in ".,;()\"\'?!":
			punctuation += 1
	
	if(space >= len(S) / 10):
		#there are many spaces in this text, likely delimited words
		print("Fitness Function: Delimited words, using gram + word_score")
		return lambda x: gram_score(x)*.95 + word_score(x)*.05
	else:
		#few spaces found, just use gram
		print("Fitness Function: No Delimited words, using gram")
		return gram_score
		
#Count character n-grams of 2,3,4 in text to judge fitness
def gram_score(S):
	r = 0
	r += MONOGRAMS.score(S)
	r += BIGRAMS.score(S) * 3
	r += TRIGRAMS.score(S) * 3
	r += QUADGRAMS.score(S)
	return r/8

def word_score(S):
	return _word_score(re.split(r"[^a-zA-Z]",S))
	
def _word_score(words):
	score = 0
	total = 0
	for w in words:
		if(TRIE.has(w)):
			score += len(w)
		else:
			score -= len(w)
		total += len(w)
	return score/total
	
def substrings_score(S,delimit=False):
	words = list(TRIE.substrings(S,delimit=delimit))
	#for w in words:
	#	if(len(w) > 1):
	#		print(w)
	return sum(len(w) for w in words)/len(S)
	
def frequency(S):
	if(isinstance(S,list)):
		S = "".join(S)
	L = []
	for c in ALPHA:
		L.append((S.count(c),c))
	L.sort(reverse=True,key=lambda x: x[0])
	return [x[1] for x in L]

#create a first guess for monoalphabetic based on common english letter frequencies
def etaoin(S):
	order = "etaoinshrdlucmfgypwbvkxjqz"
	key = {}
	for i,f in enumerate(frequency(S)):
		key[f] = order[i]
	return [key[c] for c in ALPHA]