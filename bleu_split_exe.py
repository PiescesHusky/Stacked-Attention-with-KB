"""
A simple python wrapper for the standard mult-bleu.perl 
script used in machine translation/captioning models.
References
     NeuralTalk (https://github.com/karpathy/neuraltalk)
"""
from os import system
from os import popen
from sys import argv
import os

"""
 perl $HOME/Downloads/Babel3.7/corpus/buildBPE/moses_trial/multi-bleu.perl ded < ded.dtok_it
"""
def Get_bleu(ref_file, output_file):
    cmd_base = ['perl', '$HOME/Downloads/Babel3.7/corpus/buildBPE/moses_trial/multi-bleu.perl']
    cmd_base.append(ref_file)
    cmd_base.append('<')
    cmd_base.append(output_file)
    cmd = ' '.join(cmd_base)
    bleu_return = popen(cmd).read()
    bleu_return_list = bleu_return.split()
    bleu = bleu_return_list[2].split(',')[0]
    bleu = float(bleu)
    return bleu
'''
perl $HOME/Downloads/mosesdecoder/mosesdecoder-master/scripts/tokenizer/detokenizer.perl  < ded.dtc > ded.dtok -l en
'''
def Detok(input_file, output_file, lang):

    cmd_base = ['perl', '$HOME/Downloads/mosesdecoder/mosesdecoder-master/scripts/tokenizer/detokenizer.perl', '<']
    cmd_base.append(input_file)
    cmd_base.append('>')
    cmd_base.append(output_file)  
    cmd_base.append('-l')
    cmd_base.append(lang)   
    cmd = ' '.join(cmd_base)
    dtok_return = popen(cmd).read()
    print('dtok_return',dtok_return)

def Combine_files(input_files, output_file):
    with open(output_file, 'w') as outfile:
        for fname in input_files:
            with open(fname) as f:
                for line in f:
                    outfile.write(line)
            f.close()
    outfile.close()

def Get_line_number(num_file, split_files):
    print('num_file', num_file) #test 
    lines_for_num_file = open(num_file).readlines()
    line_nums = lines_for_num_file[0]
    line_nums = line_nums.split()
    line_nums = list(map(int, line_nums))
    # print('line_nums',line_nums)
    if len(split_files) != len(line_nums):
        print('line number not matched')
    else:
        return line_nums
        
def Split_file(num_file, split_files, input_file, split_files_location, suffix = '.ref'):
    line_nums = Get_line_number(num_file, split_files)
    i = 0
    file_id = 0
    file_open_pos = list()
    file_open_pos.append(0)
    for t in range(len(line_nums)):
        file_open_pos.append(sum(line_nums[:t+1]))
    print(file_open_pos)
    with open(input_file) as f:
        print('start')
        split_files_output = list()
        for line in f:
            #print(i, file_id)
            if i == file_open_pos[file_id]:
                # print(i,file_id)
                if i >0:f_write.close()
                f_write = open(split_files[file_id] + suffix, "w")  #split_files_location + 
                split_files_output.append(split_files[file_id] + suffix)
                file_id += 1
            f_write.write(line)
            i+=1
        f_write.close()
    return split_files_output

def Detok_files(input_files):
    detok_files = list()
    for i in range(len(input_files)):
        input_file_name_split = input_files[i].split('.')
        lang = input_file_name_split[-2][6:]
        print(lang)
        Detok(input_files[i], input_files[i]+'.dtok', lang)
        detok_files.append(input_files[i]+'.dtok')
    return detok_files


def Delete(split_files_location, split_files, suffix=''):
    for i in range(len(split_files)):
        os.remove(split_files[i] + suffix) # split_files_location + 


def Get_all_bleu(num_file, split_files, input_file_ref, input_file_tst, split_files_location):
    split_files_output1 = Split_file(num_file, split_files, input_file_ref, split_files_location, suffix = '.ref')
    split_files_output2 = Split_file(num_file, split_files, input_file_tst, split_files_location, suffix = '.tst')
    split_files_output1_dtok = Detok_files(split_files_output1)
    split_files_output2_dtok = Detok_files(split_files_output2)
    bleu_list = list()
    for i in range(len(split_files_output1_dtok)):
        bleu = Get_bleu(split_files_output1_dtok[i], split_files_output2_dtok[i])
        bleu_list.append(bleu)
        
    Combine_files(split_files_output1_dtok, 'combine_dtok_ref')
    Combine_files(split_files_output2_dtok, 'combine_dtok_tst')
    bleu_combine = Get_bleu('combine_dtok_ref', 'combine_dtok_tst')
    
    Delete(split_files_location, split_files, '.ref')
    Delete(split_files_location, split_files, '.tst')
    Delete(split_files_location, split_files, '.ref.dtok')
    Delete(split_files_location, split_files, '.tst.dtok')
    return bleu_list, bleu_combine

    
    
    

    


split_files = ['tst.de-en_de', 'tst.de-en_en', 'tst.de-it_de', 'tst.de-it_it','tst.de-nl_de', 'tst.de-nl_nl', 'tst.de-ro_de', 'tst.de-ro_ro',  'tst.en-it_en', 'tst.en-it_it', 'tst.en-nl_en', 'tst.en-nl_nl', 'tst.en-ro_en', 'tst.en-ro_ro', 'tst.it-nl_it', 'tst.it-nl_nl', 'tst.it-ro_it', 'tst.it-ro_ro', 'tst.nl-ro_nl', 'tst.nl-ro_ro']

# split_files = ['tst.de-en_en', 'tst.de-en_de', 'tst.de-it_it', 'tst.de-it_de','tst.de-nl_nl', 'tst.de-nl_de', 'tst.de-ro_ro', 'tst.de-ro_de',  'tst.en-it_it', 'tst.en-it_en', 'tst.en-nl_nl', 'tst.en-nl_en', 'tst.en-ro_ro', 'tst.en-ro_en', 'tst.it-nl_nl', 'tst.it-nl_it', 'tst.it-ro_ro', 'tst.it-ro_it', 'tst.nl-ro_ro', 'tst.nl-ro_nl']

input_file_ref = 'tst.wplmb.multi.source_word'
input_file_tst = 'tst.wplmb.multi.source_lem'
num_file = 'tst.wplmb.multi.source_wordnum_list'
directory = '$HOME/Downloads/Babel3.7/corpus/buildBPE/moses_trial/'





#ed = popen('perl ./multi-bleu.perl ded < ded.dtc').read()
bleu = Get_bleu(directory+'ded', directory+'ded.dtc')
#print('ed', Get_bleu(directory+'ded', directory+'ded.dtc'), bleu+1.11)
#ed_l = ed.split()
#bleu = ed_l[2].split(',')[0]
#print(float(bleu)+1)
input_file = 'tst.wplmb.multi.source_word'
lang = 'it'
Detok(input_file, input_file+'.dtok_'+lang, lang)

bleu_list, bleu_combine = Get_all_bleu(num_file, split_files, input_file_ref, input_file_tst, directory)
print('bleu_list', bleu_list, 'bleu_combine', bleu_combine)
