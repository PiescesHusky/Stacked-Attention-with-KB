from collections import Counter, defaultdict

# corpus_lines = open('dev.source.multi.BPE_w012345').readlines()
input_file = 'train.wplmb.multi.source_Bb37'

words = Counter()
with open(input_file) as f:
    for line in f:
        words.update(line.split())

ncount_freq = defaultdict(int)                              

for word in words:
    if words[word] == 1:
        ncount_freq['1'] += 1
    elif words[word] == 2:
        ncount_freq['2'] += 1
    elif words[word] == 3:
        ncount_freq['3'] += 1
    elif words[word] == 4:
        ncount_freq['4'] += 1
    elif words[word] == 5:
        ncount_freq['5'] += 1
    elif words[word] == 6:
        ncount_freq['6'] += 1

for i in range(6):
    print(ncount_freq[str(i+1)])

#print(words)
print(words['-'])
print(words['3'])
print(len(words))
# print(len(set(w for w in open('trainCorpus.all.langSep.w').read().split())))

# print(len(set(w for w in open('wplmb.multi.extract2').read().split())))

