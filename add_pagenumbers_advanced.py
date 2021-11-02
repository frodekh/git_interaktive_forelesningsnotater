

filename = '2D/interaktive_forelesningsnotater_2D.tex'

with open(filename) as file:
    lines = file.readlines()
    
pg = 0
nytemas = 0
pgnytemas = []
for line in lines:
    if ('frame' in line) and (not ('newcommand' in line)) and (not ('begin' in line)) and (not ('end' in line)): pg += 1
    if ('nytemaside' in line):
        nytemas += 1
        pgnytemas.append(pg)
totpg = pg
pgnytemas.append(totpg)

pg = 1
nytemas = 0
lineind = 0
inframe = False
for line in lines:
    line = line.rstrip()
    if line == '}': lastparan = lineind
    if ('frame' in line) and (not ('newcommand' in line)) and (not ('begin' in line)) and (not ('end' in line)) and (not ('.mp4' in line)) and not inframe:
        inframe = True
    elif ('frame' in line) and (not ('newcommand' in line)) and (not ('end' in line)) and (not ('.mp4' in line)) and inframe:
        ln = lines[lastparan].rstrip()
        lines[lastparan] = ln + '{SIDE '+str(pg)+'/'+str(pgnytemas[nytemas]-0)+'/'+str(totpg-0)+'}' + '\r'
        pg += 1
        if  ('frame' in line) and  ('begin' in line): inframe = False
    if ('nytemaside' in line): nytemas += 1
    lines[lineind] = line + '\r'
    lineind += 1




    
with open(filename, 'w') as f:
    for item in lines:
        f.write("%s\n" % item)

        
