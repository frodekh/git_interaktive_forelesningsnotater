

filename = '3C/interaktive_forelesningsnotater_3C.tex'

with open(filename) as file:
    lines = file.readlines()
    
pg = 0
nytemas = 0
pgnytemas = []
for line in lines:
    if ('lastpagebutton' in line) and (not ('newcommand' in line)) and (not ('#' in line)): pg += 1
    if ('nytemaside' in line):
        nytemas += 1
        pgnytemas.append(pg)
totpg = pg
pgnytemas.append(totpg)

pg = 0
nytemas = 0
lineind = 0
for line in lines:
    line = line.rstrip()
    if ('lastpagebutton' in line) and (not ('newcommand' in line)) and (not ('#' in line)):
        pg += 1
        line += '{\\bf SIDE '+str(pg)+'/'+str(pgnytemas[nytemas])+'/'+str(totpg)+'}'+r"\\"
    if ('nytemaside' in line): nytemas += 1
    lines[lineind] = line + '\r'
    lineind += 1





    
with open(filename, 'w') as f:
    for item in lines:
        f.write("%s\n" % item)

        
