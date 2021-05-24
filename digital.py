#digital

if __name__ == "__main__":
	a = [0b01100100,0b01100001,0b01110100,0b01100001]
	p1 = "".join(chr(x) for x in a)
	print(p1)
	
	
	b = [0b01100010,0b01110101,0b01111001,0b01100011,0b01110101,0b01100110,0b01101001]
	index = [2,1,3,1,2,5,7,2]
	index.reverse()
	for i in range(8):
		r = 0
		for x in b:
			x = x >> (index[i]-1)
			x = x & 1
			print(x)
			r = (r << 1) + x
		print("::",chr(r))
	m = 0b01100101
	print(chr(m))
	p3 = "".join(chr(x) for x in b)
	print(p3)
	
	c = [0b01100010,0b01101101,0b01110100,0b01110011,0b01101001,0b01110111,0b01100001]
	for x in c:
		print("::",chr(x))