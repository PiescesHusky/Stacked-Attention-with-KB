from sys import argv
import glob



#print(argv)
#script, input_file, output_file = argv

def Extract_Write(input_file, outfile):
    no_sense = 10   # number of senses
    # no_fac = no_sense + 2
    with open(input_file) as f:
        for line in f:
            tokens = line.split()
            new_line = list()
            new_token = list()
            for i in range(no_sense):
                new_token.append('-') 
            new_line.append("￨".join(new_token))
         #   new_line.append('-') 
            for token in tokens:   
                new_token = list()
                factor = token.split("|")
                #  new_token.append(factor[0])   # add word to new token
                for i in range(no_sense):
                    if len(factor)<=i+3:
                        new_token.append('-') 
                    else:
                        new_token.append(factor[3+i])  # add sense to new token
                new_line.append("￨".join(new_token))
                
            outfile.write(' '.join(new_line)+'\n')




    

    # open(output_file, 'w').writelines(new_lines)
    
def Get_line_num(input_file):
    lines = open(input_file).readlines()
    new_lines = list()
    line_num = len(lines)    
    return line_num

#file directory 
# "/home/stefan/Downloads/Babel3.7/corpus/buildBPE/tst.wplmb.source/*.source"

files = glob.glob("/home/stefan/Downloads/Babel3.7/corpus/buildBPE/original_mfre.test.wplmb.source/*wplmb.source")
# /raid/data/yanzhe/babelWE/dev.wplmb014bcom
files = glob.glob("/raid/data/yanzhe/lattice/corpus/corpus_10senseBb40/tst.wplmb014bcom/*.wplmb014bcom")

input_files = list()
output_files = list()
files = sorted(files)

for file1 in files:
    segs = file1.split("/")
    new_infile = list()
    new_outfile = list()
    new_infile.append(segs[-1])
    new_outfile.append(segs[-1])
    new_outfile.append('1')
    input_files.append(segs[-1])
    output_files.append("".join(new_outfile))
## for i in range(len(input_files)):
   ## Get_some_factors(input_files[i], output_files[i])

line_nums = list()

file_name_w = 'train.wplmb.multi.source_Bb37_2'
# /raid/data/yanzhe/babelWE/
file_name_w = '/raid/data/yanzhe/lattice/corpus/corpus_10senseBb40/tst.wplmb.multi.source_Bb40_1to10'

with open(file_name_w, 'w') as outfile:
    for fname in files:
        Extract_Write(fname, outfile)
  #      outfile.writelines(Get_some_factors(fname))
        line_nums.append(str(Get_line_num(fname)))
        print(line_nums[-1])
        #print(fname)
with open(file_name_w+'num_list', 'w') as outfile:
    outfile.writelines(' '.join(line_nums))
