#first come first serve
"""

seen = set()
a = []

w1 = "onetimepad"
w2 = "thegreatcipher"
#w2 = "LEGRANDCHIFFRE".lower()
alpha = "abcdefghiklmnopqrstuvwxyz"

def load(s):
	for c in s:
		if c not in seen:
			seen.add(c)
			a.append(c)
	
load(w1)
load(w2)
load(alpha)
print("".join(a))

ON ET IM EP AD
CO QY LS GY LZ

TH EG RE AT CI PH ER
FK QX AQ RY BN FW QA
#LE GR AN DC HI FF RE


IL SQ CS KF FK AQ QY KC CO GY
?? ?? ?? ?? TH RE ET ?? ON EP
			LE AN ET ?? ON EP


NI NE		4
SE VE N		5
SI X		3
FI VE		4
FO UR		4
#TH RE E		5
TW O		3
#ON E		3
ZE RO		4
EI GH T
THERE T ONEP

COQYLSGYLZ FKQXAQRYBNFWQA ILSQCSKFFKAQQYKCCOGY

ivetonedofthepreathewherwoneightthreeturived
ONETIMEPADTHEGREATCIPHER--------THREETWOONEP
--------------------------------THREETWOONEP
ONETIMEPADTHEGREATCIPHER--------------------
ONETIMEPADLEGRANDCHIFFRE--------------------

ILSQCSKFFKAQQYKCCOGY
OUTMATCHEDTHREETOONE

https://bionsgadgets.appspot.com/ww_forms/playfair_ph_web_worker3.html











#PRIORY PARK? 
1.72km
51.28541 N 00.16367 W

1.33km
51.28454 N 00.15016 W


#midpoint
51.284975
0.156915
"""

A = [0xFF0000,
0xFF7900,
0xFFFF00,
0x13DD17,
0x304FFF,
0x7B20A3,
0xD500FA]

B = [0,0,0]
pix = []
for n in A:
	a = (n & 0xFF0000) >> 16
	b = (n & 0x00FF00) >> 8
	c = (n & 0x0000FF) >> 0
	B[0] ^= a
	B[1] ^= b
	B[2] ^= c
	pix.append(a)
	pix.append(b)
	pix.append(c)
	
from PIL import Image
img = Image.new("grayscale",(3,7),"black")
pixels = img.load()

i=0
while i < len(pix):
	if(i % 3 == 0):
		print()
	print(pix[i],end=" ")
	
	i+=1

print(img.size[0],img.size[1])
for i in range(img.size[0]):
	for j in range(img.size[1]):
		print(i,j,"=",pix[i*3 + j])
		pixels[i,j] = (i,j,pix[i*3 + j])
print(pixels)
img.show()
print()
print(B)