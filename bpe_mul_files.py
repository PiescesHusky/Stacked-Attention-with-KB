import glob
import os


#os.system('subword-nmt apply-bpe -c code.multi --vocabulary vocab.de1 --vocabulary-threshold 50 < IWSLT17.TED.dev2010.de-en.de.xml.raw.lema.wplmb.w > IWSLT17.TED.dev2010.de-en.de.xml.raw.lema.wplmb.w.BPE50')

cmd = 'subword-nmt apply-bpe -c code.multi --vocabulary vocab.de1 --vocabulary-threshold 50 < IWSLT17.TED.dev2010.de-en.de.xml.raw.lema.wplmb.w > IWSLT17.TED.dev2010.de-en.de.xml.raw.lema.wplmb.w.BPE50'

infiles = glob.glob("/home/stefan/Downloads/Babel3.7/corpus/dev_tst/w_only/*w")
outfiles = list()
outfile_loc = "/home/stefan/Downloads/Babel3.7/corpus/dev_tst/bpe_w/"
for infile in infiles:
    segs = infile.split('/')
    outfile = list()
    outfile.append(outfile_loc)
    outfile.append(segs[-1])
    outfile.append('BPE50')
    outfiles.append(''.join(outfile))
    

cmd_l = cmd.split()
for i in range(len(infiles)):
    print(infiles[i])
    print(outfiles[i])
    segs = infiles[i].split('/')
    name_segs = segs[-1].split('.')
    vocab = 'vocab.' + name_segs[4] + '1'
    cmd_l[5] = vocab
    cmd_l[9] = infiles[i]
    cmd_l[11] = outfiles[i]
    #os.system(' '.join(cmd_l))
    print(' '.join(cmd_l))



# os.system(' '.join(cmd_l))




