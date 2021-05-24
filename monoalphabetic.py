import random
import statistics
import re
import itertools
#apply key to cipher-text
def sub(S,key):
	if(isinstance(key,list)):
		d = {}
		for i,c in enumerate(key):
			d[chr(ord("a")+i)] = c
		key = d
	return "".join(key.get(c,c) for c in S)
		
#hill climb substition algorithm
def search(S):
	score_func = statistics.guess_fitness_func(S)
	alphabet = list(statistics.ALPHA)
	
	key = statistics.etaoin(S)
	best_score = score_func(S)
	best_key = key.copy()
	improved = True
	while improved:
		print("KEY:","".join(best_key))
		print(sub(S,best_key),"\n")
		print(best_score)
		improved = False
		
		
		
		#swap 2
		for c1,c2 in itertools.combinations(range(len(alphabet)),2):
			key[c1],key[c2] = key[c2],key[c1]
			sub_s = sub(S,key)
			score = score_func(sub_s)
			if(score > best_score):
				best_score = score
				best_key = key.copy()
				improved = True
			else:
				key[c1],key[c2] = key[c2],key[c1]
				
		#swap 3 in cycle
		for c1,c2,c3 in itertools.combinations(range(len(alphabet)),3):
			key[c1],key[c2],key[c3] = key[c3],key[c1],key[c2]
			sub_s = sub(S,key)
			score = score_func(sub_s)
			if(score > best_score):
				best_score = score
				best_key = key.copy()
				improved = True
			else:
				key[c1],key[c2],key[c3] = key[c2],key[c3],key[c1]
		
		if not improved and best_score < .15:
			#last ditch effort, make 2 swaps without reset
			for c1,c2 in itertools.combinations(range(len(alphabet)),2):
				key[c1],key[c2] = key[c2],key[c1]
				for c3,c4 in itertools.combinations(range(len(alphabet)),2):
					key[c3],key[c4] = key[c4],key[c3]
					sub_s = sub(S,key)
					score = score_func(sub_s)
					if(score > best_score):
						best_score = score
						best_key = key.copy()
						improved = True
						break
					else:
						key[c3],key[c4] = key[c4],key[c3]
				if(improved):
					break
				key[c1],key[c2] = key[c2],key[c1]
		
	print("KEY:","".join(best_key))
	print(sub(S,best_key))
	return best_key