from sys import argv
import glob



#print(argv)
#script, input_file, output_file = argv

def Get_some_factors(input_file):
    lines = open(input_file).readlines()
    new_lines = list()
    line_num = len(lines)


    # process each line one by one
    for line in lines:
        tokens = line.split()
        # del tokens[0]  # to remove 2tag if necessary
        tokens = [tokens[0]]   # to extract only first token of each sentence
        new_line = list()
        
        # process each token one by one
        for token in tokens:   
            new_token = list()
            factor = token.split("|")
          #  new_token.append(factor[0])   # add word to new token
         #   new_token.append(factor[5])  # add sense to new token
          #  new_line.append("|".join(new_token))
          
           #to get more than one factors
            new_mul_fac = list()
            new_mul_fac.append(factor[0])     # pick the factor to be extracted
            new_mul_fac.append(factor[1])
            new_mul_fac.append(factor[4])
            new_line.append("|".join(new_mul_fac))
            
            # to get only one factor
            #new_line.append(factor[0])
            
        new_line.append("\n")
        new_lines.append(" ".join(new_line))
    return new_lines
    

    # open(output_file, 'w').writelines(new_lines)
    
def Get_line_num(input_file):
    lines = open(input_file).readlines()
    new_lines = list()
    line_num = len(lines)    
    return line_num

files = glob.glob("/home/stefan/Downloads/Babel3.7/corpus/buildBPE/train.wplmb/*.wplmb")
# files = glob.glob("/home/stefan/Downloads/Babel3.7/corpus/buildBPE/exp/*.wplmb") # test
input_files = list()
output_files = list()
files = sorted(files)

for file1 in files:
    segs = file1.split("/")
    new_infile = list()
    new_outfile = list()
    new_infile.append(segs[-1])
    new_outfile.append(segs[-1])
    new_outfile.append('014first')
    input_files.append(segs[-1])
    output_files.append("".join(new_outfile))
## for i in range(len(input_files)):
   ## Get_some_factors(input_files[i], output_files[i])

line_nums = list()

file_name_w = 'tst.wplmb.multi.extract5'

#with open(file_name_w, 'w') as outfile:
 #   for fname in files:
#        outfile.writelines(Get_some_factors(fname))
#        line_nums.append(str(Get_line_num(fname)))
#        print(line_nums[-1])
#with open(file_name_w+'num_list', 'w') as outfile:
#    outfile.writelines(' '.join(line_nums))

location = "/home/stefan/Downloads/Babel3.7/corpus/buildBPE/train.wplmb014first/"    # location to save output file

# create an output file for each input file

for i in range(len(files)):
    with open(location+output_files[i], 'w') as outfile:
        outfile.writelines(Get_some_factors(files[i]))
    line_nums.append(str(Get_line_num(files[i])))
    print(line_nums[-1])    

