import glob



def ProcMa_with_orig(fac_file, input_file, st, outfile):
# fac_file: file with a single factor for annotation
# input_file: 

    with open(input_file) as f_main, open(fac_file) as f_fac:
       # if len(f_main.readlines()) != len(f_fac.readlines()):
          #  print('line number mismatch between two files')
          #  return('Error')
        for main_sent, fac_sent in zip(f_main, f_fac):
            #print(main_sent)
            new_line = list()
            factors = fac_sent.split()
            tokens = main_sent.split()
            if len(tokens[0].split("￨")) > 1:  # if main_sent has more than word, return 1, otherwise, 0
                main_fac_num = 1
            else: 
                main_fac_num = 0
            words = list()
            if main_fac_num == 1:
                for i in range(len(tokens)):
                    word_facs = tokens[i].split("￨")
                    words.append(word_facs[0])
            else:
                words = tokens.copy()
            #print(words)#test

            deduct_words = 0  # deduction for words
            deduct_fac = 0  # deduction for factors

 
            
   
            for i in range(len(words)):
                double_AT_found_main = 0    
            ## check if "@@" is at the end of current token and mark it for modifying 
            ## position from next token onwards
            
                double_AT_found_fac = 0 
            ## check if "@@" is at the end of current factor and mark it for modifying 
            ## position from next factor onwards 
                if main_fac_num == 1:
                    new_token = tokens[i].split("￨")
                else:
                    new_token = list()
                    new_token.append(words[i])
                if len(words[i]) > 2 and words[i][-2:] == "@@":
                    double_AT_found_main = 1   
              #  print(factors[i-deduct_words+deduct_fac])
                if len(factors[i-deduct_words+deduct_fac]) > 2 and factors[i-deduct_words+deduct_fac][-2:] == "@@":
                    double_AT_found_fac = 1
                    
                   ## if factor(stem/lemma) is longer than token, keep the factor for 
                    ## matching next token
                    len_to_fac = len(words[i])
                    if words[i][-2:] == "@@" and \
                    len(factors[i-deduct_words+deduct_fac]) - len(words[i]) > 1 and \
                    words[i][:-2].lower() == factors[i-deduct_words+deduct_fac][:len_to_fac-2]:
                        double_AT_found_fac = 0
                        
                ## Add corresponding factor
                new_token.append(factors[i-deduct_words+deduct_fac])                
             # add new token and factor to current line
                new_line.append("￨".join(new_token))  # new pipe used  
                if double_AT_found_main == 1:
                    deduct_words += 1
                if double_AT_found_fac == 1:
                    deduct_fac += 1   
            outfile.write(' '.join(new_line)+'\n')          
                
                
             
      
         

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
#fac_files = ['wplmb.multi.extract5a', 'wplmb.multi.extract5b', 'wplmb.multi.extract5c', 'wplmb.multi.extract5d', 'wplmb.multi.extract5e']
#main_files = ['train.source.multi.BPE_w01234a', 'train.source.multi.BPE_w01234b', 'train.source.multi.BPE_w01234c', 'train.source.multi.BPE_w01234d', 'train.source.multi.BPE_w01234e']
#fac_files = ['xaa1', 'xab1','xac1','xad1','xae1']
#main_files = ['xaa', 'xab','xac','xad','xae']
fac_files = ['dev.wplmb.multi.source_lemBPE80k']
main_files = ['dev.source.multi.BPE_word100k_pos']


with open('dev.source.multi.BPE_word100k_pos_lem80k', 'w') as outfile:
    for i in range(len(main_files)):
     #       print(fname, len(infile.readlines()))
        ProcMa_with_orig(fac_files[i], main_files[i], 't', outfile)


