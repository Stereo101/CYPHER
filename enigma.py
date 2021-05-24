#enimga mechanical cipher


class Enigma:
	alpha = "abcdefghijklmnopqrstuvwxyz"
	def __init__(self,reflector,plug_list = None,scramblers = None):
		self.plugs = {}
		if(plug_list is not None):
			for a,b in plug_list:
				a = Enigma.alpha.index(a)
				b = Enigma.alpha.index(b)
				self.plugs[a] = b
				self.plugs[b] = a
		
		self.scramblers = []
		for scram in scramblers:
			self.scramblers.append(scram.copy())
		
		#convert scramblers to letter indexs
		for scram in self.scramblers:
			for i in range(len(scram)):
				scram[i] = Enigma.alpha.index(scram[i])
		
		#set each scrambler state to 0
		self.scrambler_state = []
		for scram in self.scramblers:
			self.scrambler_state.append(0)
		
		self.reflector = reflector.copy()
		#self.reflector_state = 0
		
		for i in range(len(self.reflector)):
			self.reflector[i] = Enigma.alpha.index(self.reflector[i])
		
		
	def advance_scramblers(self):
		index = 0
		self.scrambler_state[index] = (self.scrambler_state[index]+1) % 26
		while index+1 < len(self.scramblers) and self.scrambler_state[index] == 0:
			index += 1
			self.scrambler_state[index] = (self.scrambler_state[index]+1) % 26
		"""
		if index == len(self.scramblers):
			self.reflector_state = (self.reflector_state + 1) % 26
		"""
	def press(self,letter):
		k = Enigma.alpha.index(letter)
		#advance scrambler state
		if(len(self.scramblers) > 0):
			self.advance_scramblers()
			
		#TEMP	
		#self.scrambler_state[0] = 0
		
		
		#plug substitution
		if k in self.plugs:
			k = self.plugs[k]
			
		#go through each scrambler forward
		for i in range(len(self.scramblers)):
			k = (k+self.scrambler_state[i])%26
			k = self.scramblers[i].index(k)
			k = (k-self.scrambler_state[i])%26
		
		#go through reflector
		k = self.reflector.index(k)
		
		#go through each scrambler backwards
		for i in range(len(self.scramblers)-1,-1,-1):
			k = (k+self.scrambler_state[i])%26
			k = self.scramblers[i][k]
			k = (k-self.scrambler_state[i])%26
	
		#plugs again
		if k in self.plugs:
			k = self.plugs[k]
		
		#turn back into a letter
		return Enigma.alpha[k]
		
	def decrypt(self,message):
		z = []
		for c in message:
			z.append(self.press(c))
		return "".join(z)

if __name__ == "__main__":
	scrambler_1 = list("UWYGADFPVZBECKMTHXSLRINQOJ".lower())
	reflector = list("YRUHQSLDPXNGOKMIEBFZCWVJAT".lower())

	e = Enigma(reflector,scramblers=[scrambler_1])
	a1 = e.decrypt("zydni")
	print(a1)
	for initial in range(26):
		e_2 = Enigma(reflector,scramblers=[scrambler_1])
		e_2.scrambler_state[0] = initial
		a2 = e_2.decrypt("QHSGUWIG".lower())
		if(a2.startswith("xv")):
			print(a2)

	scrambler_2 = list("AJPCZWRLFBDKOTYUQGENHXMIVS".lower())
	scrambler_3 = list("TAGBPCSDQEUFVNZHYIXJWLRKOM".lower())

	plugs = "AB SZ UY GH LQ EN".lower().split()

	e_3 = Enigma(reflector,scramblers=[scrambler_2,scrambler_1,scrambler_3],plug_list=plugs)
	e_3.scrambler_state[0] = 0
	e_3.scrambler_state[1] = 4
	e_3.scrambler_state[2] = 1
	a3 = e_3.decrypt("GYHRVFLRXY".lower())
	print(a3)