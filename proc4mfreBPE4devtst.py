import glob
import os

def ProcMa_with_orig(ofile, input_file, st):

    lines = open(input_file).readlines()  ## file with senses
    olines = open(ofile).readlines()    ## file with tokens/BPE
    
    # find out suitable target language
    loc_segs = input_file.split('/')
    name_segs = loc_segs[-1].split('.')
    langs = name_segs[3].split('-')
    if langs[0] == name_segs[4]:
        tolan = langs[1]
    elif langs[1] == name_segs[4]:
        tolan = langs[0]
	# totag sample <2it>
    totag = "<2"+tolan+">"+"￨"+"-"
    print("num_lines pre", len(lines))
    print("num_lines bpe", len(olines))
    print(input_file, ofile)
    new_lines = list()
    if len(olines) == len(lines):
        line_num =  len(olines)
    else:
        print('line number mismatch between two files')
        return('Error')
    for i in range(line_num):
        otokens = olines[i].split()
        tokens = lines[i].split()
        tokens_factored = list()
        new_line = list()
        del tokens[0]
        
        # formatting tokens|sense as lists
        for token in tokens:
            factor = token.split("|")  
            new_token_factored = list()  
            new_token_factored.append(factor[0]) 
            new_token_factored.append(factor[1]) 
            tokens_factored.append(new_token_factored)
        
        
         
        
        # if it's source side, tag such as "<2en>" is added at
        # the beginning of a sentence.
        if st == 's':
            new_line.append(totag)
     #   print(tokens_factored)
      #  print(olines[i])
      
      ## annotation with sense 
      
        deduct = 0  
        
        # after BPE, a word could become several segments, as well as their positions
        # the increase in position will be moderated by "deduct" to match that from 
        # tokens_factored
        
        for t in range(len(otokens)):
            new_token = list()
            new_token.append(otokens[t])
            
            double_AT_found = 0    
            ## check if "@@" is at the end of current token and mark it for modifying 
            ## position from next token onwards
            
            sense_f = 0  
            ## check if sense is found, 1:found  0:not found
            
            if otokens[t][-2:] == "@@":
                double_AT_found = 1
             ## if "@@" is found, mark it as one
             
             ## loop through senses available to check if sense is annotated for 
             ## current token
            new_token.append(tokens_factored[t-deduct][1])
            
            # print(new_token)
            new_line.append("￨".join(new_token))
            if double_AT_found == 1:
                deduct += 1
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
                
infiles15 = glob.glob("/home/stefan/Downloads/Babel3.7/corpus/dev_tst/15mfre/tst/*source15")
infilesbpe = glob.glob("/home/stefan/Downloads/Babel3.7/corpus/dev_tst/bpe_w/tst/*wBPE50")
print(infiles15)
print(infilesbpe)
infiles15 = sorted(infiles15)
infilesbpe = sorted(infilesbpe)

## List of most-frequent-sense corpuses
tryfile = ['train.de-it.lema.de.wplmb.source.15', 'train.de-it.lema.it.wplmb.source.15', 'train.de-nl.lema.de.wplmb.source.15', 'train.de-nl.lema.nl.wplmb.source.15', 'train.de-ro.lema.de.wplmb.source.15', 'train.de-ro.lema.ro.wplmb.source.15', 'train.en-de.lema.de.wplmb.source.15', 'train.en-de.lema.en.wplmb.source.15', 'train.en-it.lema.en.wplmb.source.15', 'train.en-it.lema.it.wplmb.source.15', 'train.en-nl.lema.en.wplmb.source.15', 'train.en-nl.lema.nl.wplmb.source.15', 'train.en-ro.lema.en.wplmb.source.15', 'train.en-ro.lema.ro.wplmb.source.15', 'train.it-nl.lema.it.wplmb.source.15', 'train.it-nl.lema.nl.wplmb.source.15', 'train.it-ro.lema.it.wplmb.source.15', 'train.it-ro.lema.ro.wplmb.source.15', 'train.nl-ro.lema.nl.wplmb.source.15', 'train.nl-ro.lema.ro.wplmb.source.15']

## List of BPE50 corpuses
tryfilewBPE50 = ['train.de-it.lema.de.wplmb.w.BPE50', 'train.de-it.lema.it.wplmb.w.BPE50', 'train.de-nl.lema.de.wplmb.w.BPE50', 'train.de-nl.lema.nl.wplmb.w.BPE50', 'train.de-ro.lema.de.wplmb.w.BPE50', 'train.de-ro.lema.ro.wplmb.w.BPE50', 'train.en-de.lema.de.wplmb.w.BPE50', 'train.en-de.lema.en.wplmb.w.BPE50', 'train.en-it.lema.en.wplmb.w.BPE50', 'train.en-it.lema.it.wplmb.w.BPE50', 'train.en-nl.lema.en.wplmb.w.BPE50', 'train.en-nl.lema.nl.wplmb.w.BPE50', 'train.en-ro.lema.en.wplmb.w.BPE50', 'train.en-ro.lema.ro.wplmb.w.BPE50', 'train.it-nl.lema.it.wplmb.w.BPE50', 'train.it-nl.lema.nl.wplmb.w.BPE50', 'train.it-ro.lema.it.wplmb.w.BPE50', 'train.it-ro.lema.ro.wplmb.w.BPE50', 'train.nl-ro.lema.nl.wplmb.w.BPE50', 'train.nl-ro.lema.ro.wplmb.w.BPE50']




with open('tst.source.mfreBPE50', 'w') as outfile:
    for i in range(len(infiles15)):
     #       print(fname, len(infile.readlines()))
        outfile.writelines(ProcMa_with_orig(infilesbpe[i], infiles15[i], 's'))


