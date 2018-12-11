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

split_files = ['train.de-it_de', 'train.de-it_it','train.de-nl_de', 'train.de-nl_nl', 'train.de-ro_de', 'train.de-ro_ro', 'train.en-de_de', 'train.en-de_en', 'train.en-it_en', 'train.en-it_it', 'train.en-nl_en', 'train.en-nl_nl', 'train.en-ro_en', 'train.en-ro_ro', 'train.it-nl_it', 'train.it-nl_nl', 'train.it-ro_it', 'train.it-ro_ro', 'train.nl-ro_nl', 'train.nl-ro_ro']

# positions to split
line_nums = [207092, 207092, 215121, 215121, 202963, 202963, 207702, 207702, 233382, 233382, 238900, 238900, 222213, 222213, 235046, 235046, 219203, 219203, 208507, 208507]

if len(split_files) != len(line_nums):
    print('line number not matched')
    
#split_pos = list()
#for line_num in line_nums:
#    split_pos.append(line_num*2)

tryfilewBPE50_swap = Swap(tryfilewBPE50)

lines = open('train.source.multi.BPE_w012345').readlines()

pos = 0
for i in range(len(line_nums)):
    with open(split_files[i], 'w') as outfile:
        outfile.writelines(lines[pos:pos+line_nums[i]])
    pos += line_nums[i]
