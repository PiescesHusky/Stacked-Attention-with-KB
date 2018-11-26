from sys import argv

## to swap position of language paired corpuses to turn source to target
## for example, ["en-de.en", "en-de.de"] becomes ["en-de.de", "en-de.en"]

def Swap(filenames):
    fnew = list()
    for i in range(len(filenames)):
        if i % 2 == 1:
            fnew.append(filenames[i-1])
        else:
            fnew.append(filenames[i+1])
    return(fnew)


filenames = ['train.en-de.lema.en.wplmb.w', 'train.en-it.lema.en.wplmb.w', 'train.en-nl.lema.en.wplmb.w', 'train.en-ro.lema.en.wplmb.w']

tryfilewBPE50 = ['train.de-it.lema.de.wplmb.w.BPE50', 'train.de-it.lema.it.wplmb.w.BPE50', 'train.de-nl.lema.de.wplmb.w.BPE50', 'train.de-nl.lema.nl.wplmb.w.BPE50', 'train.de-ro.lema.de.wplmb.w.BPE50', 'train.de-ro.lema.ro.wplmb.w.BPE50', 'train.en-de.lema.de.wplmb.w.BPE50', 'train.en-de.lema.en.wplmb.w.BPE50', 'train.en-it.lema.en.wplmb.w.BPE50', 'train.en-it.lema.it.wplmb.w.BPE50', 'train.en-nl.lema.en.wplmb.w.BPE50', 'train.en-nl.lema.nl.wplmb.w.BPE50', 'train.en-ro.lema.en.wplmb.w.BPE50', 'train.en-ro.lema.ro.wplmb.w.BPE50', 'train.it-nl.lema.it.wplmb.w.BPE50', 'train.it-nl.lema.nl.wplmb.w.BPE50', 'train.it-ro.lema.it.wplmb.w.BPE50', 'train.it-ro.lema.ro.wplmb.w.BPE50', 'train.nl-ro.lema.nl.wplmb.w.BPE50', 'train.nl-ro.lema.ro.wplmb.w.BPE50']

tryfilewBPE50_swap = Swap(tryfilewBPE50)

with open('train.target.wsdBPE50', 'w') as outfile:
    for fname in tryfilewBPE50_swap:
        with open(fname) as infile:
            outfile.write(infile.read())
