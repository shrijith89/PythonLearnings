text = "learn and practice learn and practice"

words = []
words = text.split()
wfreq = [words.count(w) for w in words]
print(dict(zip(words,wfreq)))