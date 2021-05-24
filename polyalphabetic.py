import statistics
import re
import itertools
#polyalphabetic ciphers

def right_shift_char(c1,c2):
	alphabet = statistics.ALPHA
	d1 = alphabet.index(c1)
	d2 = alphabet.index(c2)
	return alphabet[(d1+(d2+1))%len(alphabet)]

def left_shift_char(c1,c2):
	alphabet = statistics.ALPHA
	d1 = alphabet.index(c1)
	d2 = alphabet.index(c2)
	return alphabet[(d1-(d2+1))%len(alphabet)]
	
def reverse_vigenere(S,key):
	key_index = 0
	z = []
	for c in S:
		#print(c,key[key_index])
		z.append(left_shift_char(c,key[key_index]))
		key_index = (key_index + 1) % len(key)
	return "".join(z)
	
	
def dictionary_attack_vigenere(S):
	best_score = -9999
	best_key = None
	best_plain = None
	
	words = [x.strip() for x in open("words.txt","r").readlines()]
	for word in words:
		w = re.sub(r"[^a-z]","",word.lower())
		if(len(w) == 0):
			continue
		z = reverse_vigenere(S,w)
		score = statistics.word_score(z)
		if(score > best_score):
			print("new best",w,z,score)
			best_score = score
			best_key = w
			best_plain = z
	return best_key,best_plain,best_score
	
def brute_force_vigenere(S):
	best_score = -9999
	best_key = None
	best_plain = None
	score_func = statistics.guess_fitness_func(S)
	finished = False
	for word_len in range(1,6+1):
		for w in itertools.product(statistics.ALPHA,repeat=word_len):
			w = "".join(w)
			#print(w)
			z = reverse_vigenere(S,w)
			score = score_func(z)
			if(score > best_score):
				print("new best",w,z,score)
				best_score = score
				best_key = w
				best_plain = z
				if(score > .19):
					finished = True
					break
		if finished:
			break
	return best_key,best_plain,best_score