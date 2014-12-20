print "Simple Cipher"
#ord()
#chr()
message = "Chips"

def alg(text):
	cipherString = [ord(text[0])]
	for x in range(1,len(text)):
		cipherString.append(ord(text[x])+cipherString[x-1])
	print cipherString
	reverse(cipherString)

def reverse(cipher):
	real = chr(cipher[0])
	for x in range(1,len(cipher)):
		real+= chr(cipher[x]-cipher[x-1])
	print real

alg(message)