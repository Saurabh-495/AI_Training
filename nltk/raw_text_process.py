path = "raw-text.txt"
f = open(path)
rawText = f.read()

f.close()

print(rawText[:165])