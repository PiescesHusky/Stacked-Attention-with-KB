from sys import argv
import glob



#print(argv)
#script, input_file, output_file = argv

def Get_some_factors(input_file):
    lines = open(input_file).readlines()
    new_lines = list()


    # process each line one by one
    for line in lines:
        tokens = line.split()
        new_line = list()
        
        # process each token one by one
        for token in tokens:   
            new_token = list()
            factor = token.split("|")
          #  new_token.append(factor[0])   # add word to new token
         #   new_token.append(factor[5])  # add sense to new token
          #  new_line.append("|".join(new_token))
            new_line.append(factor[3])
        new_line.append("\n")
        new_lines.append(" ".join(new_line))
    return new_lines
    

    # open(output_file, 'w').writelines(new_lines)
    
files = glob.glob("/home/stefan/Downloads/Babel3.7/corpus/buildBPE/single/*.source")
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


with open('wplmb.multi.extract3deit_de', 'w') as outfile:
    for fname in files:
        outfile.writelines(Get_some_factors(fname))
