

def ProcMa_with_orig(ofile, input_file, st):

    lines = open(input_file).readlines()
    olines = open(ofile).readlines()
    name_segs = input_file.split('.')
    langs = name_segs[1].split('-')
    if langs[0] == name_segs[3]:
        tolan = langs[1]
    elif langs[1] == name_segs[3]:
        tolan = langs[0]
	# totag sample <2it>
    totag = "<2"+tolan+">"+"|"+"-"
    print("num_lines pre", len(lines))
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
        
        # formatting pos_start|pos_end|tokens|sense as lists
        for token in tokens:
            factor = token.split("|")
            diff = int(factor[1]) - int(factor[0])
            if diff == 1:
                new_token_factored = list()
               # if st == 's':
               #     new_token.append(totag)
                new_token_factored.append(int(factor[0]))
                new_token_factored.append(int(factor[1]))
                new_token_factored.append(factor[2])
                new_token_factored.append(factor[3])
                tokens_factored.append(new_token_factored)
              #  new_line.append("|".join(new_token))
            elif diff > 1:
                words = factor[2].split("_")
              #  new_tokens = list()
                for i in range(diff):
                    new_token_factored = list()
                #    if st == 's':
                #        new_token.append(totag)
                    new_token_factored.append(int(factor[0])+i)
                    new_token_factored.append(int(factor[0])+i+1)
                    new_token_factored.append(words[i])
                    new_token_factored.append(factor[3])
                    tokens_factored.append(new_token_factored)
                #    new_line.append("|".join(new_token))
         
        
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
            for token_factored in tokens_factored:
                if token_factored[0] == t - deduct:   ## adjusted by "deduct"
                    new_token.append(token_factored[3])
                    sense_f = 1
                    break
                elif token_factored[0] > t - deduct:   ## adjusted by "deduct"
                    break
            if sense_f == 0:
                new_token.append('-')
            # print(new_token)
            new_line.append("|".join(new_token))
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
filenames = ['train.de-it.lema.de.wplmb.out', 'train.de-it.lema.it.wplmb.out', 'train.de-nl.lema.de.wplmb.out', 'train.de-nl.lema.nl.wplmb.out', 'train.de-ro.lema.de.wplmb.out', 'train.de-ro.lema.ro.wplmb.out', 'train.en-de.lema.de.wplmb.out', 'train.en-de.lema.en.wplmb.out', 'train.en-es.lema.en.wplmb.out', 'train.en-es.lema.es.wplmb.out', 'train.en-fr.lema.en.wplmb.out', 'train.en-fr.lema.fr.wplmb.out', 'train.en-it.lema.en.wplmb.out', 'train.en-it.lema.it.wplmb.out', 'train.en-nl.lema.en.wplmb.out', 'train.en-nl.lema.nl.wplmb.out', 'train.en-ro.lema.en.wplmb.out', 'train.en-ro.lema.ro.wplmb.out', 'train.it-nl.lema.it.wplmb.out', 'train.it-nl.lema.nl.wplmb.out', 'train.it-ro.lema.it.wplmb.out', 'train.it-ro.lema.ro.wplmb.out', 'train.nl-ro.lema.nl.wplmb.out', 'train.nl-ro.lema.ro.wplmb.out']

ori_files = ['train.de-it.lema.de.wplmb.w', 'train.de-it.lema.it.wplmb.w', 'train.de-nl.lema.de.wplmb.w', 'train.de-nl.lema.nl.wplmb.w', 'train.de-ro.lema.de.wplmb.w', 'train.de-ro.lema.ro.wplmb.w', 'train.en-de.lema.de.wplmb.w', 'train.en-de.lema.en.wplmb.w', 'train.en-es.lema.en.wplmb.w', 'train.en-es.lema.es.wplmb.w', 'train.en-fr.lema.en.wplmb.w', 'train.en-fr.lema.fr.wplmb.w', 'train.en-it.lema.en.wplmb.w', 'train.en-it.lema.it.wplmb.w', 'train.en-nl.lema.en.wplmb.w', 'train.en-nl.lema.nl.wplmb.w', 'train.en-ro.lema.en.wplmb.w', 'train.en-ro.lema.ro.wplmb.w', 'train.it-nl.lema.it.wplmb.w', 'train.it-nl.lema.nl.wplmb.w', 'train.it-ro.lema.it.wplmb.w', 'train.it-ro.lema.ro.wplmb.w', 'train.nl-ro.lema.nl.wplmb.w', 'train.nl-ro.lema.ro.wplmb.w']
fnew = Swap(filenames)

#print(fnew)

ofnew = Swap(ori_files)

print(ofnew)

tryfile = ['train.de-it.lema.de.wplmb.out', 'train.de-it.lema.it.wplmb.out', 'train.de-nl.lema.de.wplmb.out', 'train.de-nl.lema.nl.wplmb.out', 'train.de-ro.lema.de.wplmb.out', 'train.de-ro.lema.ro.wplmb.out', 'train.en-de.lema.de.wplmb.out', 'train.en-de.lema.en.wplmb.out', 'train.en-it.lema.en.wplmb.out', 'train.en-it.lema.it.wplmb.out', 'train.en-nl.lema.en.wplmb.out', 'train.en-nl.lema.nl.wplmb.out', 'train.en-ro.lema.en.wplmb.out', 'train.en-ro.lema.ro.wplmb.out', 'train.it-nl.lema.it.wplmb.out', 'train.it-nl.lema.nl.wplmb.out', 'train.it-ro.lema.it.wplmb.out', 'train.it-ro.lema.ro.wplmb.out', 'train.nl-ro.lema.nl.wplmb.out', 'train.nl-ro.lema.ro.wplmb.out']
tryfilew = ['train.de-it.lema.de.wplmb.w', 'train.de-it.lema.it.wplmb.w', 'train.de-nl.lema.de.wplmb.w', 'train.de-nl.lema.nl.wplmb.w', 'train.de-ro.lema.de.wplmb.w', 'train.de-ro.lema.ro.wplmb.w', 'train.en-de.lema.de.wplmb.w', 'train.en-de.lema.en.wplmb.w', 'train.en-it.lema.en.wplmb.w', 'train.en-it.lema.it.wplmb.w', 'train.en-nl.lema.en.wplmb.w', 'train.en-nl.lema.nl.wplmb.w', 'train.en-ro.lema.en.wplmb.w', 'train.en-ro.lema.ro.wplmb.w', 'train.it-nl.lema.it.wplmb.w', 'train.it-nl.lema.nl.wplmb.w', 'train.it-ro.lema.it.wplmb.w', 'train.it-ro.lema.ro.wplmb.w', 'train.nl-ro.lema.nl.wplmb.w', 'train.nl-ro.lema.ro.wplmb.w']
tryfile_s = Swap(tryfile)
tryfilew_s = Swap(tryfilew)
tryfile_s = ['train.de-it.lema.de.wplmb.out']
tryfilew_s = ['train.de-it.lema.de.wplmb.w.BPE35']
with open('try4wsdBPE', 'w') as outfile:
    for i in range(len(tryfile_s)):
     #       print(fname, len(infile.readlines()))
        outfile.writelines(ProcMa_with_orig(tryfilew_s[i], tryfile_s[i], 't'))


