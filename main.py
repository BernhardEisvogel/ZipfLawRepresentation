import matplotlib.pyplot as plt
import numpy as np

# Thanks to the following website
# https://scipython.com/book/chapter-4-the-core-python-language-ii/problems/p42/the-most-100-frequent-words-in-moby-dick/
# for the first verison of the code

from os import walk

filenames = next(walk("data"), (None, None, []))[2]

for bookname in filenames:
    print("Currently reading:" + bookname)
    if bookname.split(".")[-1] != "txt":
        continue
    f =  open("data/" + bookname, 'r', encoding='utf-8')

# wordcount is a dictionary of word-counts, keyed by word
    wordcount = {}
    for line in f:
        line = line.strip().lower()
        line = line.replace('--', ' ').replace('\'s', '').replace('&', 'and')
        # Strip any of the following punctuation
        for c in '!?":;,()\'.*[]':
            line = line.replace(c, '')

        words = line.split(' ')
        for word in words:
            if not word:
                continue
            try:
                wordcount[word] += 1
            except KeyError:
                wordcount[word] = 1

    wc = []
    for k,v in wordcount.items():
        wc.append((v,k))
    # Sort it into decreasing order
    wc.sort(reverse=True)

# Output the 100 most frequent words from the top of the wc list
for i in range(100):
    print('{:10s}: {:d}'.format(wc[i][1], wc[i][0]))

# Graphical comparison with Zipf's Law: log f(w) = log C - a log r(w)
max_rank = 30
rank = np.linspace(1, max_rank, max_rank)
freq = np.array([ wc[i][0] for i in range(max_rank) ])
# Plot the data: log(f) against log(r)
plt.plot(rank, freq, "x", color = "r", label="Observed")

# Plot the Zipf's law prediction
plt.plot(rank, 1/rank * (freq[0] + freq[1]*2 + freq[0]*3)/3, label="Predicted")
plt.xlabel('rank of word')
plt.ylabel('frequency of word')
plt.title("Word frequency rank and comparison with Zipf's Law")
plt.legend()
plt.savefig('result.png')
plt.show()