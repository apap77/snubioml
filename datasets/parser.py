DATA_PATH = "./mushroom_orig.txt"
OUT_PATH = "./mushroom.txt"

with open(DATA_PATH, 'r') as inFile:
	with open(OUT_PATH, 'w') as out:
		for line in inFile.readlines():
			tokens = line.strip().split("\t")
			tokens = tokens[1:] + [tokens[0]]
			print("\t".join(tokens), file=out)