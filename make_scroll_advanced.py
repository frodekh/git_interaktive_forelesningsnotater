
####NOTE implementation for not changing page number when _b, _c, etc. not finished, missing check in last part

import regex as re
import sys


def find_in_paran(linein):

    start_paran = False
    strout = ''
    i = 0
    found = False
    while(not found and (i < len(linein))):
        if linein[i:i+1] == '{' and not start_paran:
            start_paran = True
        elif (linein[i:i+1] == '{' and start_paran) or (linein[i:i+1] == '}' and not start_paran):
            print('STOP!',lineind,linein)
            exit()
        elif linein[i:i+1] == '}' and start_paran: found = True
        elif start_paran: strout += linein[i:i+1]
        i += 1
    if strout == '':
        print('STOP!',lineind,linein)
        exit()
    return strout
        
def remove_command_with_paran(com,linein):

    pos = re.search(com,linein)
    pos = pos.start()
    linkinfo = find_in_paran(linein[pos:])
    lineout = linein[0:pos-1] + linein[pos+2+len(com)+len(linkinfo):]
    return lineout

def remove_all_command_with_paran(com,linein):

    lineout = linein
    while(com in lineout):
        lineout = remove_command_with_paran(com,lineout)
    return lineout

#filename = '2A/interaktive_forelesningsnotater_2A_del1_av_2.tex'
filename = sys.argv[1]

with open(filename) as file:
    lines = file.readlines()
lines0=lines.copy()


#filename = '2A/interaktive_forelesningsnotater_2A_del1_av_2_scroll.tex'

found_start = False
i = 0
while(not found_start):
    if 'begin{document}' in lines[i]:
        found_start = True
        firstline = i+1
    i += 1

pg = 0
nytemas = 0
pgnytemas = []
multistr = re.compile('.+_.}.+') ## check if label is of the form '*_?)*' (i.e. (\label{ddd_a})
lineind = 0
for line in lines:
#    if ('frame' in line) and (not ('newcommand' in line)) and (not ('number' in line)) and (not ('begin' in line)) and (not ('end' in line)) and not bool(re.match(multistr,lines[lineind + 1])): pg += 1
    if ('frame' in line) and (not ('newcommand' in line)) and (not ('number' in line)) and (not ('begin' in line)) and (not ('end' in line)): pg += 1
    if ('nytemaside' in line):
        nytemas += 1
        pgnytemas.append(pg)
    lineind += 1
totpg = pg
pgnytemas.append(totpg)

pg = 1
nytemas = 0
lineind = 0
inframe = False
lastlab = ''
for line in lines:
    line = line.rstrip()
    #if line == '}': lastparan = lineind
    if ('frame' in line) and (not ('newcommand' in line)) and (not ('number' in line)) and (not ('begin' in line)) and (not ('end' in line)) and (not ('.mp4' in line)) and not inframe:
        lastlab = find_in_paran(line)
        line = '{'
        inframe = True
        #print(line)
    elif ('frame' in line) and (not ('newcommand' in line)) and (not ('end' in line)) and (not ('.mp4' in line)) and inframe:
        pg += 1
        if  ('frame' in line) and  ('begin' in line): inframe = False
        lastlab = find_in_paran(line)
        line = '{'
    if ('frame' in line) and (not ('newcommand' in line)) and (not ('.mp4' in line)) and ('begin' in line): line = '{'
    if ('frame' in line) and (not ('newcommand' in line)) and (not ('.mp4' in line)) and ('end' in line): line = '}'
    if line[0:6] == '\label': line = ''
    line = remove_all_command_with_paran('hyperlink',line)
    if (line[0:6] == '}{SIDE') and not ('X/Y/Z' in line): line = '\hyperlink{'+lastlab+'}{\pagebutton' + line[1:] + '}}'
    if ('nytemaside' in line): nytemas += 1
    if 'pagebuttonolink' in line: line = re.sub(r"\\"+'pagebuttonolink','',line)
    lines[lineind] = line# + '\r'
    lineind += 1


addlnk = "\ \ \ \ \hyperlink{scroll}{\pagebutton{Scroll gjennom hele dokumentet for ?? finne side}}\\\\"+r"\\"
checklnk = '\hyperlink{front3}{\pagebutton{Forrige side}'
repl = r"\\\\"

addlnk2 = "\ \ \ \ \hyperlink{scroll}{\pagebutton{Scroll gjennom hele dokumentet for ?? finne side}}"
checklnk2 = '\hyperlink{intro}{\choicebutton{Neste side}}'
checklnk2b = '\hyperlink{blue_intro}{\choicebutton{Neste side}}'
checklnk2c = '\hyperlink{feil_intro}{\choicebutton{Neste side}}'


with open(filename, 'w') as f:
    for item in lines0:
        if checklnk in item: item = re.sub(repl,addlnk,item)
        if (checklnk2 in item) or (checklnk2b in item) or (checklnk2c in item): item = item.rstrip() + addlnk2 + '\n'
        if (not 'end{document}' in item): f.write("%s" % item)
    f.write("%s\n" % '\\begin{frame}')
    f.write("%s\n" % '\\label{scroll}')
    f.write("%s\n" % '\\htmlcom{huge}{Her kan du scrolle gjennom hele forelesningsnotatet men merk at dette kun er for ?? {'+r"\bf"+' finne frem til en side}, en del tekst mangler og formatteringen er ofte rar s?? det er {'+r"\bf"+' ikke meningen at man skal bruke denne scrollen til l??ring.} \\textcolor{red}{Ved ?? klikke p?? SIDE-linken p?? den gitte siden under vil du g?? rett inn p?? det stedet du ??nsker i forelesningsnotatene og begynne/fortsette l??ringen der.}}')

    for item in lines[firstline:]:
        if ('end{document}' in item): f.write("%s\n" % '\end{frame}')
        f.write("%s\n" % item)

        
