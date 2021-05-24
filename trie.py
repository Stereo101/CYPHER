class Trie:
	def __init__(self):
		self.root = {}
		self.root["word"] = False
		self.root["prefix"] = ""
		
	def add(self,word):
		current = self.root
		s = ""
		for c in word:
			s += c
			if not c in current:
				current[c] = {}
				current[c]["word"] = False
				current[c]["prefix"] = s
			current = current[c]
		current["word"] = True
	
	def load_itr(self,itr):
		count = 0
		for w in itr:
			self.add(w.strip().lower())
			count += 1
		print(f"Loaded {count} words into Trie")
		
	def load(self,file_path):
		count = 0
		with open(file_path,"r") as fp:
			for w in fp.readlines():
				self.add(w.strip().lower())
				count += 1
		print(f"Loaded {count} words")
		
	def has(self,word):
		current = self.root
		for c in word.lower():
			if c not in current:
				return False
			current = current[c]
		return current["word"]
	
	#find all in-order words in S which are in Trie
	def in_order(self,S):
		L = list(set(self._in_order(S.lower(),self.root)))
		L.sort()
		L.sort(key=lambda x: len(x),reverse=True)
		return L
	
	def _in_order(self,S,node):
		current = node
		if(current["word"]):
			yield current["prefix"]
		if(len(S) == 0):
			return
		
		yield from self._in_order(S[1:],node=current)
		if(S[0] in current):
			yield from self._in_order(S[1:],node=current[S[0]])
	
	#greedy find all non-overlapping substrings of S which are in Trie
	def substrings(self,S,delimit=False):
		index = 0
		out = []
		while index < len(S):
			#match longest string from here
			longest = ""
			longest_i = 0
			i = 0
			current = self.root
			while i+index < len(S):
				c = S[index+i]
				if c not in current:
					break
				current = current[c]
				if(current["word"]):
					longest = current["prefix"]
					longest_i = i
				i += 1
				
			if(longest != ""):
				yield longest
			#advance index
			index += (longest_i+1)
			if(delimit):
				i = 0
				while index+i-1 < len(S) and S[index+i-1] in "abcdefghijklmnopqrstuvwxyz":
					i += 1
				if(i > 0):
					index += i
	

