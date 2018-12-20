
lines = open('tst.source.multi.BPE_w01234mfreBb4').readlines()
DEnum = 0
ENnum = 0
ITnum = 0
NLnum = 0
ROnum = 0
for i in range(len(lines)):
    if lines[i][2:4] == 'de':
        DEnum += 1
    elif lines[i][2:4] == 'en':
        ENnum += 1
    elif lines[i][2:4] == 'it':
        ITnum += 1
    elif lines[i][2:4] == 'nl':
        NLnum += 1
    elif lines[i][2:4] == 'ro':
        ROnum += 1


print(DEnum, ENnum, ITnum, NLnum, ROnum)
print(DEnum+ENnum+ITnum+NLnum+ROnum)


#lines = open('xae').readlines()

#print(lines[171750])
#print(lines[171751])

