import transposition
import statistics
import trie
import monoalphabetic
import polyalphabetic
import re

def mono_p1():
	s = """THSWQD THZ RBXP GWXP HG XL ZWRNBRHK UTPQ WQ KBQZBQ, W THZ SWRWGPZ GTP IOWGWRT XMRPMX, HQZ XHZP RPHOFT HXBQD GTP IBBVR HQZ XHNR WQ GTP KWIOHOL OPDHOZWQD GOHQRLKSHQWH; WG THZ RGOMFV XP GTHG RBXP ABOPVQBUKPZDP BA GTP FBMQGOL FBMKZ THOZKL AHWK GB THSP RBXP WXNBOGHQFP WQ ZPHKWQD UWGT H QBIKPXHQ BA GTHG FBMQGOL.""".lower()
	key = monoalphabetic.search(s)
	print(statistics.ALPHA)
	print("-"*26)
	print("".join(key))
	
def mono_p2():
	s = """LGGK VHZXJ RP VJJCEVO CK ZMX MGEXO C SCLDGEXJXS LGRX IVIXJL CK ZMX IGDQXZ GH ZMX SJXLL UMCDM C MVS ZVQXK HJGR PGBJ (OVWGJVZGJP). VZ HCJLZ C MVS KXNOXDZXS ZMXR, WBZ KGU ZMVZ C UVL VWOX ZG SXDCIMXJ ZMX DMVJVDZXJL CK UMCDM ZMXP UXJX UJCZZXK, C WXNVK ZG LZBSP ZMXR UCZM SCOCNXKDX.""".lower()
	key = monoalphabetic.search(s)
	print(statistics.ALPHA)
	print("-"*26)
	print("".join(key))

def mono_p3():
	s = """	ABCDC EF CGCD H IJHK BLKCGCD EM ABC NCFA JHEO LI
			BPQHM RJHMF CMO ABC QPDOCDCDF LI SLBM LRCMFBHK KCDC
			MCGCD AL DCTCEGC ABC LDHMWC RERF KBETB KLPJO FBLK ABCQ
			ABHA HMLABCD HF TPMMEMW HMO HF DCFLJPAC HF ABCQFCJGCF
			KHF PRLM ABCED ADHTX GCDU JLMW HMO GCDU FCGCDC KCDC ABC
			CVPEMLTAEHJ WHJCF ABHA UCHD KC KHEACO JLMW ILD MCKF
			LI ABC JLMC FAHD LI FHGHMMHB NPA MLMC CGCD DCHTBCO PF""".lower()
	s = re.sub(r"\s+"," ",s)
	key = monoalphabetic.search(s)
	print(statistics.ALPHA)
	print("-"*26)
	print("".join(key))
def mono_p4():
	s = """AJLPNYRJZJKLZYASGSKQGSMMEJKEJPFSVLPJLKKEJELNNSPZKYNNYGNSGASGYZJGAKEYZYGASVWNJKSWSKECNLUJZKEJZEYCYZWSVOEKLGAHYKKJAZEJNYJZLKLGUESPPJLAFHSPZJLFSVGJRJPYTLOYGJALZMJJKJPZUESSGJPLUEYNATYOEKZLYNEJPKMSEVGAPJAKSGZGLTJ(EYZCLGYSNL)""".lower()
	key = monoalphabetic.search(s)
	print(statistics.ALPHA)
	print("-"*26)
	print("".join(key))
	
def tran_p6():
	s = "TEAUYUOSHNNTRRBTEPAIENROMLMNTTIL"
	#s = "TUTTMOWSIHINOSMRNEPIEEUZLXSESZ"
	for r in transposition.skip(s):
		print(r)
		input()
	print(transposition.make_rail_fence(s,3))
	while True:
		s = transposition.reverse_rail_fence(s,3)
		print(s)
		#input()
def poly_p1():
	key = "flash"
	s = "ztvglkdbglruhabtuoz"
	print(polyalphabetic.reverse_vigenere(s,key))
	
def poly_p2():
	s = "jcwsvlivlvgsjjfjcwcvl"
	polyalphabetic.brute_force_vigenere(s)
	
def poly_p3():
	s = """	LAFLUIWOYWPADUFHSNBVSWVNDZQDUF
			RBPLUYQPLWLPHZRLUEDUBSYMIPRDIJ
			HTYQUCUZYLKFRSKHZBUHULUEKPQFOY
			LYSSAMWOCWHZOLGDTDDPPOFDDTGOPY
			UDGWOYOSDRYKVVDVLAULRZYGWPLJZY
			QKYPTWVLJIAFHHSWOMUVDDAPLMJLUE
			PVLRNPDWFXWMQAFHZSEQCFAGQDFLJF
			LHLDSWCLMQLFXUBULBDUBVPVWFQHWY
			UHRHJGSOCUZZXAGFVLILQVAFDARKPQ
LZCQAGULJBUCZAMPL""".lower()
	s = re.sub(r"\s+","",s)
	polyalphabetic.brute_force_vigenere(s)
def challenge_p7():
	def leftRotate(n,d):
		return (n << d)|(n >> (7 - d)); 
	x=4
	y=19
	z=3
	A = [50,20,37,95,74,0,25,51,5,78,34,32,72]
	base = ord("a")
	index = 0
	for i in range(len(A)):
		r = ((A[i]) % y) + z
		print(chr(r+base),chr(r+base+1),chr(r+base-1),r)

def challenge_p11():
	a = "ABCCDE"
	b = "FGHCCG"
	l1 = a+b
	code = "TT AA AG AG CG TG AC AT GA AG AG AT".split()
	code_unique_len = len(set(code))
	import itertools
	for order in itertools.permutations("ATCG",4):
		print(order)
		order_pair = []
		
		for p in itertools.product(order,repeat=2):
			order_pair.append("".join(p))
		print(order_pair)
		code_order = list(set(code))
		code_order.sort(key=lambda x: order_pair.index(x))
		
		
		print(code_order)
		
		for comb in itertools.combinations("abcdefghijklmnopqrstuvwxyz",code_unique_len):
			s = "".join(comb[code_order.index(x)] for x in code)
			results = list(statistics.TRIE.substrings(s))
			r_len = sum(len(x) for x in results)
			if(r_len == 12 and any(len(r) >= 5 for r in results)):
				print(comb)
				print(",".join(results))
				print()
		
	
	"""
	for e in statistics.PATTERN.match(a):
		if("ee" in e and "u" not in e):
			print(e)
	print("-")
	for e in statistics.PATTERN.match(b):
		print(e)
	print("-")
	"""
	
	#e = 5
	#u = 21
	#u - e = 16
	#span
	#ATCG
	#A = 0
	#T = 1
	#C = 2
	#G = 3
	"""
	#u = AC
	#e = AG
	f = TA
	g	TT
	h	TC
	i	TG
	j	CA
	k	CT
	l	CC
	m	CG
	n	GA
	o	GT
	p	GC
	q	GG
	r	AA
	s	AT
	"""
	#tuvwxyz
	
def mono_all():
	#print("monoalphabetic problem #1")
	#mono_p1()
	
	print("monoalphabetic problem #2")
	mono_p2()
	
	print("monoalphabetic problem #3")
	mono_p3()
	
	print("monoalphabetic problem #4")
	mono_p4()
	
def poly_all():
	print("polyalphabetic problem #1")
	poly_p1()
	
	print("polyalphabetic problem #2")
	poly_p2()
	
	print("polyalphabetic problem #3")
	poly_p3()
def main():
	#mono_all()
	
	#poly_all()
	#challenge_p7()
	#challenge_p11()
	#tran_p6()
	
	
if __name__ == "__main__":
	main()
