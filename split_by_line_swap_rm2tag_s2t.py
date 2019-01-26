from sys import argv
import os


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
    
def Extract_Write_Remove2tag(input_file, outfile):
    with open(input_file) as f:
        for line in f:
            tokens = line.split()
            new_line = tokens.copy()
          #  print('new_line',new_line)
            del new_line[0]
          #  new_line.append('-') 
            #for i in range(len(tokens)-1):   
                #new_token = list()
                #factor = token.split("￨")
                #  new_token.append(factor[0])   # add word to new token
         #   new_token.append(factor[5])  # add sense to new token
          #  new_line.append("|".join(new_token))
               # new_line.append(tokens[i+1])     # pick the factor to be extracted
            outfile.write(' '.join(new_line)+'\n')


filenames = ['train.en-de.lema.en.wplmb.w', 'train.en-it.lema.en.wplmb.w', 'train.en-nl.lema.en.wplmb.w', 'train.en-ro.lema.en.wplmb.w']

tryfilewBPE50 = ['train.de-en.lema.de.wplmb.w.BPE50', 'train.de-en.lema.en.wplmb.w.BPE50', 'train.de-it.lema.de.wplmb.w.BPE50', 'train.de-it.lema.it.wplmb.w.BPE50', 'train.de-nl.lema.de.wplmb.w.BPE50', 'train.de-nl.lema.nl.wplmb.w.BPE50', 'train.de-ro.lema.de.wplmb.w.BPE50', 'train.de-ro.lema.ro.wplmb.w.BPE50',  'train.en-it.lema.en.wplmb.w.BPE50', 'train.en-it.lema.it.wplmb.w.BPE50', 'train.en-nl.lema.en.wplmb.w.BPE50', 'train.en-nl.lema.nl.wplmb.w.BPE50', 'train.en-ro.lema.en.wplmb.w.BPE50', 'train.en-ro.lema.ro.wplmb.w.BPE50', 'train.it-nl.lema.it.wplmb.w.BPE50', 'train.it-nl.lema.nl.wplmb.w.BPE50', 'train.it-ro.lema.it.wplmb.w.BPE50', 'train.it-ro.lema.ro.wplmb.w.BPE50', 'train.nl-ro.lema.nl.wplmb.w.BPE50', 'train.nl-ro.lema.ro.wplmb.w.BPE50']

split_files = ['tst.de-en_de', 'tst.de-en_en', 'tst.de-it_de', 'tst.de-it_it','tst.de-nl_de', 'tst.de-nl_nl', 'tst.de-ro_de', 'tst.de-ro_ro',  'tst.en-it_en', 'tst.en-it_it', 'tst.en-nl_en', 'tst.en-nl_nl', 'tst.en-ro_en', 'tst.en-ro_ro', 'tst.it-nl_it', 'tst.it-nl_nl', 'tst.it-ro_it', 'tst.it-ro_ro', 'tst.nl-ro_nl', 'tst.nl-ro_ro']

# positions to split
line_nums = [207092, 207092, 215121, 215121, 202963, 202963, 207702, 207702, 233382, 233382, 238900, 238900, 222213, 222213, 235046, 235046, 219203, 219203, 208507, 208507]
#
# /raid/data/yanzhe/lattice/corpus/corpus_10senseBb40/train.source.multi.BPE_wordBPE100k_pos_lemBPE80k_mfreBb40
lines_for_num_file = open('/raid/data/yanzhe/lattice/corpus/corpus_10senseBb40/train.wplmb.multi.source_wordnum_list').readlines()
line_nums = lines_for_num_file[0]
line_nums = line_nums.split()
line_nums = list(map(int, line_nums))
print('line_nums',line_nums)
if len(split_files) != len(line_nums):
    print('line number not matched')
    
#split_pos = list()
#for line_num in line_nums:
#    split_pos.append(line_num*2)

tryfilewBPE50_swap = Swap(tryfilewBPE50)

#lines = open('/home/stefan/Downloads/Babel3.7/corpus/buildBPE/dev.wplmb.multi.source_lem').readlines()
#  /raid/data/yanzhe/lattice/corpus/corpus_10senseBb40/dev.wplmb.multi.source_wordBPE100k
#num_lines_in = len(lines)
i = 0
file_id = 0
file_open_pos = list()
file_open_pos.append(0)
for t in range(len(line_nums)):
    file_open_pos.append(sum(line_nums[:t+1]))

split_files_location = '/raid/data/yanzhe/lattice/corpus/corpus_10senseBb40/'
# '/home/stefan/Downloads/Babel3.7/corpus/buildBPE/'

# /raid/data/yanzhe/lattice/corpus/corpus_10senseBb40/dev.wplmb.multi.source_wordBPE100k
with open('/raid/data/yanzhe/lattice/corpus/corpus_10senseBb40/train.wplmb.multi.source_wordBPE100k') as f:
    print('start')
    for line in f:
        #print(i, file_id)
        if i == file_open_pos[file_id]:
            if i >0:f_write.close()
            f_write = open(split_files_location+split_files[file_id],"w")
            # /raid/data/yanzhe/lattice/corpus/corpus_10senseBb40/
            
            print(split_files[file_id])
            file_id += 1
        f_write.write(line)
        i+=1
        
print('yes not yet')
#pos = 0
#for i in range(len(line_nums)):
 #   with open('/raid/data/yanzhe/lattice/corpus/corpus_10senseBb40/'+split_files[i], 'w') as outfile:
  #      outfile.writelines(lines[pos:pos+line_nums[i]])
   # pos += line_nums[i]
    
split_files = Swap(split_files)   

with open('/raid/data/yanzhe/lattice/corpus/corpus_10senseBb40/train.wplmb.multi.target_wordBPE100k', 'w') as outfile:
    for i in range(len(split_files)):
     #       print(fname, len(infile.readlines()))
        Extract_Write_Remove2tag( split_files_location +split_files[i], outfile)

for i in range(len(split_files)):
    os.remove( split_files_location + split_files[i] )
    # /raid/data/yanzhe/lattice/corpus/corpus_10senseBb40/
