import os


chapters_1 = ['1A/interaktive_forelesningsnotater_1A_del1_av_2.tex','1A/interaktive_forelesningsnotater_1A_del2_av_2.tex','1B/interaktive_forelesningsnotater_1B_del1_av_2.tex','1B/interaktive_forelesningsnotater_1B_del2_av_2.tex','1C/interaktive_forelesningsnotater_1C_del1_av_2.tex','1C/interaktive_forelesningsnotater_1C_del2_av_2.tex','1D/interaktive_forelesningsnotater_1D_del1_av_2.tex','1D/interaktive_forelesningsnotater_1D_del2_av_2.tex','1E/interaktive_forelesningsnotater_1E.tex','1F/interaktive_forelesningsnotater_1F.tex','1G/interaktive_forelesningsnotater_1G.tex']

bu_1 = ['1A/bu1', '1A/bu2', '1B/bu1', '1B/bu2', '1C/bu1', '1C/bu2', '1D/bu1', '1D/bu2', '1E/bu', '1F/bu', '1G/bu']

chapters_2 = ['2A/interaktive_forelesningsnotater_2A_del1_av_2.tex','2A/interaktive_forelesningsnotater_2A_del2_av_2.tex','2B/interaktive_forelesningsnotater_2B_del1_av_2.tex','2B/interaktive_forelesningsnotater_2B_del2_av_2.tex','2C/interaktive_forelesningsnotater_2C_del1_av_2.tex','2C/interaktive_forelesningsnotater_2C_del2_av_2.tex','2D/interaktive_forelesningsnotater_2D.tex']

bu_2 = ['2A/bu1', '2A/bu2', '2B/bu1', '2B/bu2', '2C/bu1', '2C/bu2', '2D/bu']

chapters_3 = ['3A/interaktive_forelesningsnotater_3A.tex', '3B/interaktive_forelesningsnotater_3B.tex', '3C/interaktive_forelesningsnotater_3C.tex', '3D/interaktive_forelesningsnotater_3D_del1_av_2.tex', '3D/interaktive_forelesningsnotater_3D_del2_av_2.tex', '3E/interaktive_forelesningsnotater_3E.tex']

bu_3 = ['3A/bu', '3B/bu', '3C/bu', '3D/bu1', '3D/bu2','3E/bu']

os.system('pwd')

for i in range(len(chapters_1)):
    print('cp '+bu_1[i]+' '+chapters_1[i])
    os.system('cp '+bu_1[i]+' '+chapters_1[i])
    if i > 0:
        os.system('python make_scroll.py '+ chapters_1[i])
    else:
        os.system('python make_scroll_advanced.py '+ chapters_1[i])
    

for i in range(len(chapters_2)):
    print('cp '+bu_2[i]+' '+chapters_2[i])
    os.system('cp '+bu_2[i]+' '+chapters_2[i])
    os.system('python make_scroll_advanced.py '+ chapters_2[i])

for i in range(len(chapters_3)):
    print('cp '+bu_3[i]+' '+chapters_3[i])
    os.system('cp '+bu_3[i]+' '+chapters_3[i])
    if i > 2:
        os.system('python make_scroll_advanced.py '+ chapters_3[i])
    else:
        os.system('python make_scroll.py '+ chapters_3[i])

    
