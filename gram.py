#grams
class Gram:
	def __init__(self,length):
		self.length = length
		self.d = {}
		self.max_freq = None
		
	def load(self,filename):
		print("Loading gram",self.length)
		count = 0
		with open(filename,"r") as fp:
			for line in fp.readlines():
				gram,occurs = line.strip().split()
				occurs = int(occurs)
				count += occurs
				self.d[gram.lower()] = occurs
		for k,v in self.d.items():
			self.d[k] = v/count
		self.max_freq = max(self.d.values())
		
	def score(self,S):
		#S = S.lower()
		r = 0
		offset = 0
		max_possible = 0
		while offset < len(S)-self.length+1:
			substring = S[offset:offset+self.length]
			max_possible += self.max_freq
			if substring in self.d:
				r += self.d.get(substring)
				
				offset += self.length
			else:
				offset += 1
		return r/max_possible