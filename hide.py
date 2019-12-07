from PIL import Image
from bitarray import bitarray
import struct
import sys


def encode(inFile):
	m = input("Enter message to hide: ")

	if len(m) > 8190:
		print("Message to long!")
		exit()

	mb = bitarray()
	mb.fromstring(m)
	mbSize = mb.length()

	c = 0 # counter

	inImage = Image.open(inFile)

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
	size = struct.pack('H', mbSize).decode("utf-8")
	f = open("r.png", "a+")
	f.write(size)
	f.close()

def decode(inFile):
	f = open(inFile, "rb")
	fstr = f.read()
	strLen = fstr[-2:]
	length = struct.unpack('H', strLen)
	length = int(length[0])
	f.close()

	inImage = Image.open(inFile)
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
	print("Succes!")
	print(decodedMessage)


def main():
	try:
		operation = sys.argv[1]
	except:
		print("Incorrect input!")
		print("Usage: -e(to encode)/-d(to decode) input_file")
		exit()

	try:
		inFile = sys.argv[2]
	except:
		print("Incorrect input!")
		print("Usage: -e(to encode)/-d(to decode) input_file")
		exit()

	if operation == '-e':
		encode(inFile)
	elif operation == '-d':
		decode(inFile)
	else:
		print("Incorrect input!")
		print("Usage: -e(to encode)/-d(to decode) input_file")
		exit()


if __name__ == "__main__":
    main()