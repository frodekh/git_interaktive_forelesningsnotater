
import regex as re

filename = '1G/interaktive_forelesningsnotater_1G.tex'

with open(filename) as file:
    lines = file.readlines()

multistr = re.compile('.+_.}') ## check if label is of the form '*_?}' (i.e. (\label{ddd_a})
multistr2 = re.compile('.+_a}') ##exclude the first page with _a
pg = 0
nytemas = 0
pgnytemas = []
lastlabel = ''
lineind = 0

print

for line in lines:
    if ('\label' in line): lastlabel = lineind
    if ('lastpagebutton' in line) and (not ('newcommand' in line)) and (not ('#' in line)) and not (bool(re.match(multistr,lines[lastlabel])) and not bool(re.match(multistr2,lines[lastlabel]))): pg += 1 #; print(pg,line,lines[lastlabel])
    if ('nytemaside' in line):
        nytemas += 1
        pgnytemas.append(pg)
    lineind += 1
totpg = pg
pgnytemas.append(totpg)

pg = 0
nytemas = 0
lineind = 0
lastlabel = ''
for line in lines:
    if ('\label' in line): lastlabel = lineind
    line = line.rstrip()
    if ('lastpagebutton' in line) and (not ('newcommand' in line)) and (not ('#' in line)):
        if not (bool(re.match(multistr,lines[lastlabel])) and not bool(re.match(multistr2,lines[lastlabel]))): pg += 1 #; print(pg,line,lines[lastlabel])
        line += '{\\bf SIDE '+str(pg)+'/'+str(pgnytemas[nytemas])+'/'+str(totpg)+'}'+r"\\"
    if ('nytemaside' in line): nytemas += 1
    lines[lineind] = line + '\r'
    lineind += 1





    
with open(filename, 'w') as f:
    for item in lines:
        f.write("%s\n" % item)

        
