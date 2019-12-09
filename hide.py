from PIL import Image
from bitarray import bitarray
import struct
import sys

class textColors:
	ERROR = '\033[1;31;48m'
	SUCCES = '\033[1;32;48m'

	END = '\033[1;37;48m'


def encode(inFile):
	try:
		inImage = Image.open(inFile)
	except:
		print(textColors.ERROR+"No such file: "+inFile+'!'+textColors.END)
		exit()

	maxMessSize = inImage.size[0]*inImage.size[1]*3/8
	if maxMessSize > 65535:
		maxMessSize = 65535

	print("Max character capacity of "+inFile+" image: " + str(maxMessSize))

	m = input("Enter message to hide: ")

	if len(m) > 65535:
		print(textColors.ERROR+"Message is to long!"+textColors.END)
		exit()

	if maxMessSize < len(m):
		print(textColors.ERROR+"Message is to long!"+textColors.END)
		exit()

	mb = bitarray()
	mb.fromstring(m)
	mbSize = mb.length()

	c = 0 # counter

	oldPixels = inImage.load()

	newImage = Image.new( 'RGB', (inImage.size[0], inImage.size[1]), "black")
	pixels = newImage.load()

	for i in range(newImage.size[0]):    # for every col
		for j in range(newImage.size[1]):    # For every row
			r,g,b = oldPixels[i,j]

			if c < mbSize:
				if mb[c] == 1:
					r = r | 1
				else:
					r = r & 254

				c += 1

			if c < mbSize:
				if mb[c] == 1:
					g = g | 1
				else:
					g = g & 254

				c += 1

			if c < mbSize:
				if mb[c] == 1:
					b = b | 1
				else:
					b = b & 254

				c += 1

			pixels[i,j] = (r,g,b)

	newImage.save("r.png")

	try:
		size = struct.pack('H', len(m)).decode("utf-8")
	except:
		print(textColors.ERROR+"Something went wrong! r.png does not contain hidden message"+textColors.END)
		exit()

	try:
		f = open("r.png", "a+")
	except:
		print(textColors.ERROR+"Something went wrong! r.png does not contain hidden message"+textColors.END)
		exit()

	f.write(size)
	f.close()

	print(textColors.SUCCES+"Succes! Message encrypted in file r.png"+textColors.END)


def decode(inFile):
	try:
		f = open(inFile, "rb")
	except:
		print(textColors.ERROR+"No such file: "+inFile+'!'+textColors.END)
		exit()

	fstr = f.read()
	strLen = fstr[-2:]
	length = struct.unpack('H', strLen)
	length = int(length[0])
	f.close()
	length = length*8

	try:
		inImage = Image.open(inFile)
	except:
		print(textColors.ERROR+"No such file: "+inFile+'!'+textColors.END)
		exit()

	pixels = inImage.load()

	bc = 0 # bit counter
	mb = bitarray() # array for string

	for i in range(inImage.size[0]):    # for every col
		for j in range(inImage.size[1]):    # For every row
			r,g,b = pixels[i,j]

			if bc < length:
				mb.append(r & 1)
				bc+=1
			else:
				break

			if bc < length:
				mb.append(g & 1)
				bc+=1
			else:
				break

			if bc < length:
				mb.append(b & 1)
				bc+=1
			else:
				break

	decodedMessage = mb.tostring()
	print(textColors.SUCCES+"Succes! Decoded message:")
	print(decodedMessage+textColors.END)


def main():
	try:
		operation = sys.argv[1]
	except:
		print(textColors.ERROR+"Incorrect input!"+textColors.END)
		print("Usage: python3 hide.py -e(to encode)/-d(to decode) input_file")
		exit()

	try:
		inFile = sys.argv[2]
	except:
		print(textColors.ERROR+"Incorrect input!"+textColors.END)
		print("Usage: python3 hide.py -e(to encode)/-d(to decode) input_file")
		exit()

	if operation == '-e':
		encode(inFile)
	elif operation == '-d':
		decode(inFile)
	else:
		print(textColors.ERROR+"Incorrect input!"+textColors.END)
		print("Usage: python3 hide.py -e(to encode)/-d(to decode) input_file")
		exit()


if __name__ == "__main__":
    main()
