import glob

def ProcMa_with_orig(fac_file, input_file, st):
# fac_file: file with a single factor for annotation
# input_file: 


    lines = open(input_file).readlines()  ## file with senses
    fac_lines = open(fac_file).readlines()    ## file with tokens/BPE
    name_segs = input_file.split('.')
    langs = name_segs[1].split('-')
   # if langs[0] == name_segs[3]:
   #     tolan = langs[1]
   # elif langs[1] == name_segs[3]:
   #     tolan = langs[0]
	# totag sample <2it>
   # totag = "<2"+tolan+">"+"￨"+"-"   # new pipe used
    print("num_lines pre", len(lines))
    new_lines = list()
    if len(fac_lines) == len(lines):
        line_num =  len(fac_lines)
    else:
        print('line number mismatch between two files')
        return('Error')
    for i in range(line_num):
        factors = fac_lines[i].split()
        tokens = lines[i].split()
        tokens_factored = list()
        new_line = list()
        # del tokens[0]
        
        # formatting tokens|sense as lists
        for token in tokens:
            factor = token.split("￨")  # new pipe
            new_token_factored = list()
            for t in range(len(factor)):
                new_token_factored.append(factor[t])   # create a list for factors of a token
            tokens_factored.append(new_token_factored)
       # print(tokens_factored)  # check
        
         
        
        # if it's source side, tag such as "<2en>" is added at
        # the beginning of a sentence.
        #  changed to be inserted when matching finished
       # if st == 's':          
        #    new_line.append(totag)
     #   print(tokens_factored)
      #  print(fac_lines[i])
      
      ## annotation with sense 
      
        deduct = 0  
        deduct_fac = 0
        
        ## remove '-' from <2en> tag
        # del factors[0]
        
        # after BPE, a word could become several segments, as well as their positions
        # the increase in position will be moderated by "deduct" to match that from 
        # tokens_factored
        
        for t in range(len(tokens)):
        
            # copy original factors
            new_token = tokens_factored[t].copy()
            
            
            
            
            double_AT_found = 0    
            ## check if "@@" is at the end of current token and mark it for modifying 
            ## position from next token onwards
            
            double_AT_found_fac = 0 
            ## check if "@@" is at the end of current factor and mark it for modifying 
            ## position from next factor onwards  
            
            sense_f = 0  
            ## check if sense is found, 1:found  0:not found
            
            ## if "@@" is found, mark it as one
            if len(tokens_factored[t][0]) >2:
                if tokens_factored[t][0][-2:] == "@@":
                    double_AT_found = 1            
             
             ## if "@@" is found, mark it as one
            if len(factors[t-deduct+deduct_fac]) >2:
                if factors[t-deduct+deduct_fac][-2:] == "@@":                 
                    double_AT_found_fac = 1
                    len_to_fac = len(tokens_factored[t][0])
                    
                    ## if factor(stem/lemma) is longer than token, keep the factor for 
                    ## matching next token
                    if tokens_factored[t][0][-2:] == "@@" and \
                    len(factors[t-deduct+deduct_fac]) - len(tokens_factored[t][0]) > 1 and \
                    tokens_factored[t][0][:-2].lower() == factors[t-deduct+deduct_fac][:len_to_fac-2]:
                        double_AT_found_fac = 0
             
             
             ## Add corresponding factor
            new_token.append(factors[t-deduct+deduct_fac])
            
            # print(new_token)
            # add new token and factor to current line
            new_line.append("￨".join(new_token))  # new pipe used
            if double_AT_found == 1:
                deduct += 1
            if double_AT_found_fac == 1:
                deduct_fac += 1 
                
        # if it's source side, tag such as "<2en>" is added at
        # the beginning of a sentence.        
        if st == 's':
            new_line.insert(0, totag)  
        new_line.append("\n")
        # print(new_line)
        new_lines.append(" ".join(new_line))
    return(new_lines)
         

def Swap(filenames):
    fnew = list()
    for i in range(len(filenames)):
        if i % 2 == 1:
            fnew.append(filenames[i-1])
        else:
            fnew.append(filenames[i+1])
    return(fnew)

def Check_swap_result(filenames, fnew):
    for i in range(len(filenames)):
        if i % 2 == 1:
            if filenames[i-1] == fnew[i]:
                print('yes')
            else:
                print(filenames[i-1], fnew[i])
        else:
            if filenames[i+1] == fnew[i]:
                print('yes')
            else:
                print(filenames[i+1], fnew[i])
                


## List of most-frequent-sense corpuses
tryfile = ['train.de-it.lema.de.wplmb.source.15', 'train.de-it.lema.it.wplmb.source.15', 'train.de-nl.lema.de.wplmb.source.15', 'train.de-nl.lema.nl.wplmb.source.15', 'train.de-ro.lema.de.wplmb.source.15', 'train.de-ro.lema.ro.wplmb.source.15', 'train.en-de.lema.de.wplmb.source.15', 'train.en-de.lema.en.wplmb.source.15', 'train.en-it.lema.en.wplmb.source.15', 'train.en-it.lema.it.wplmb.source.15', 'train.en-nl.lema.en.wplmb.source.15', 'train.en-nl.lema.nl.wplmb.source.15', 'train.en-ro.lema.en.wplmb.source.15', 'train.en-ro.lema.ro.wplmb.source.15', 'train.it-nl.lema.it.wplmb.source.15', 'train.it-nl.lema.nl.wplmb.source.15', 'train.it-ro.lema.it.wplmb.source.15', 'train.it-ro.lema.ro.wplmb.source.15', 'train.nl-ro.lema.nl.wplmb.source.15', 'train.nl-ro.lema.ro.wplmb.source.15']

## List of BPE50 corpuses
tryfilewBPE50 = ['train.de-it.lema.de.wplmb.w.BPE50', 'train.de-it.lema.it.wplmb.w.BPE50', 'train.de-nl.lema.de.wplmb.w.BPE50', 'train.de-nl.lema.nl.wplmb.w.BPE50', 'train.de-ro.lema.de.wplmb.w.BPE50', 'train.de-ro.lema.ro.wplmb.w.BPE50', 'train.en-de.lema.de.wplmb.w.BPE50', 'train.en-de.lema.en.wplmb.w.BPE50', 'train.en-it.lema.en.wplmb.w.BPE50', 'train.en-it.lema.it.wplmb.w.BPE50', 'train.en-nl.lema.en.wplmb.w.BPE50', 'train.en-nl.lema.nl.wplmb.w.BPE50', 'train.en-ro.lema.en.wplmb.w.BPE50', 'train.en-ro.lema.ro.wplmb.w.BPE50', 'train.it-nl.lema.it.wplmb.w.BPE50', 'train.it-nl.lema.nl.wplmb.w.BPE50', 'train.it-ro.lema.it.wplmb.w.BPE50', 'train.it-ro.lema.ro.wplmb.w.BPE50', 'train.nl-ro.lema.nl.wplmb.w.BPE50', 'train.nl-ro.lema.ro.wplmb.w.BPE50']

fac_files = glob.glob("/home/stefan/Downloads/Babel3.7/corpus/buildBPE/single/*.source")
main_files = glob.glob("/home/stefan/Downloads/Babel3.7/corpus/buildBPE/single/*.source")
fac_files = sorted(fac_files)
main_files = sorted(main_files)
fac_files = ['wplmb.multi.extract5a', 'wplmb.multi.extract5b', 'wplmb.multi.extract5c', 'wplmb.multi.extract5d', 'wplmb.multi.extract5e']
main_files = ['train.source.multi.BPE_w01234a', 'train.source.multi.BPE_w01234b', 'train.source.multi.BPE_w01234c', 'train.source.multi.BPE_w01234d', 'train.source.multi.BPE_w01234e']
with open('train.source.multi.BPE_w012345', 'w') as outfile:
    for i in range(len(main_files)):
     #       print(fname, len(infile.readlines()))
        outfile.writelines(ProcMa_with_orig(fac_files[i], main_files[i], 't'))


