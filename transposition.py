import math

def make_rail_fence(S,rail_size):
	rail = []
	for _ in range(rail_size):
		rail.append([])
	rail_index = 0
	rail_dx = 1
	for c in S:
		rail[rail_index].append(c)
		rail_index += rail_dx
		if(rail_index == 0 or rail_index==rail_size-1):
			rail_dx *= -1
	s = ""
	for r in rail:
		s += "".join(r)
	return s
	
def reverse_rail_fence(S,rail_size):
	rail = ["?"]*len(S)
	zig_len = 2*(rail_size-1)
	rules = []
	for _ in range(rail_size):
		rules.append([])
	on_rail = 0
	rail_dir = 1
	for i in range(zig_len):
		rules[on_rail].append(i)
		on_rail += rail_dir
		if(on_rail == 0 or on_rail == rail_size-1):
			rail_dir *= -1
	#print(rules)	
	offset = 0
	for r in range(rail_size):
		i = 0
		for n in range(offset,len(S)):
			while i%zig_len not in rules[r]:
				i+=1
			if(i >= len(S)):
				break
			rail[i] = S[n]
			#print("".join(rail))
			i += 1
			
			offset = n+1
	return "".join(rail)

def substring_reflection(S):
	for chunk in range(2,len(S)):
		if(len(S) % chunk != 0):
			continue
		z = []
		print("chunk size",chunk)
		for p in range(len(S)//chunk):
			print(p*chunk,(p+1)*(chunk))
			z.append("".join(reversed(S[p*chunk:(p+1)*chunk])))
		print()
		yield "".join(z)

#Read from left to right skipping N characters
#	move right 1 when an index has already been read		
def skip(S):
	for skip in range(1,len(S)):
		z = []
		used = set()
		index = 0
		for _ in range(len(S)):
			z.append(S[index])
			used.add(index)
			index += skip
			index = index % len(S)
			while(index in used and len(used) < len(S)):
				index = (index + 1) % len(S)
		yield "".join(z)


def modular(S):
	for mul in range(1,len(S)):
		print(mul)
		if(math.gcd(mul,len(S)) != 1):
			continue
		z = []
		for i in range(len(S)):
			z.append(S[(offset+(i*mul))%len(S)])
		yield "".join(z)
			

def main():
	s = "TEAUYUOSHNNTRRBTEPAIENROMLMNTTIL".lower()
	#s = "SNEJDGNTTEXARONEXXTDAIXXNHHEANRTOIESSXORXDASSEUUO".lower()
	s_r = "".join(reversed(s))
	#R = set(modular(s))
	R = set(substring_reflection(s))
	#R |= set(skip(s))
	#R |= set(skip(s_r))
	R = [(digram_score(x),x) for x in R]
	R.sort(reverse=True,key = lambda x: x[0])
	for score,z in R:
		print(score,z)
		input()
	#modular("".join(list(reversed(list(s)))))
	
if __name__ == "__main__":
	main()