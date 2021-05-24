class Pattern:
	def __init__(self):
		self.patterns = {}
		
	def add(self,word):
		w = word.lower()
		size = len(w)
		p = self._normalize_pattern(w)
		if size not in self.patterns:
			self.patterns[size] = {}
		if p not in self.patterns[size]:
			self.patterns[size][p] = set()
		self.patterns[size][p].add(w)
	
	def _normalize_pattern(self,w):
		d = {}
		used = ord("a")
		pat = []
		for c in w:
			if c not in d:
				d[c] = chr(used)
				used += 1
			pat.append(d[c])
		return "".join(pat)
	
	def load(self,file_path):
		print(f"Loading {file_path} into patterns")
		with open(file_path,"r") as fp:
			for word in (x.strip() for x in fp.readlines()):
				self.add(word)
			
	def load_itr(self,itr):
		for w in itr:
			self.add(w)
			
	def match(self,pattern):
		size = len(pattern)
		if(size not in self.patterns):
			return set()
		p = self._normalize_pattern(pattern)
		if p not in self.patterns[size]:
			return set()
		return self.patterns[size][p]
		
	def potential_subs(self,pattern):
		keys = set()
		for p in self.match(pattern):
			for i,c in enumerate(p):
				keys.add((pattern[i],c))
		return keys