

Under hver mappe finnes filene bu1/bu2 eller bare bu som er original tex-filene (ble laget med make_backups.py.

Det er disse som skal endres hvis det skal gjøres endringer.

Fila create_scroll_from_bu.py kopierer disse back-up-filene til tex-filene med fulle navn som f.eks. interaktive_forelesningsnotater_1B_del1_av_2.tex.
Deretter går den gjennom og lager en scroll som legges til på slutten av fila for å gi mulighet til å scrolle gjennom forelesningsnotet (muligheten dukker opp under table of contents)

create_scroll_from_bu.py benytter seg av kodene make_scroll.py og make_scroll_advanced.py, noen av forelesningsnotatene er laget i gammelt format med \begin{frame} og andre i oppdatert format med makroer for framene, make_scroll_advanced.py er for de siste.

Helt tilsvarende finnes python-koder for å lage sidenummerene, add_pagenumbers.py og add_pagenumbers_advanced.py som har blitt brukt til å lage sidenummere (men filer uten sidenummer kreves for å bruke disse, filer uten sidenummer eksisterer ikke lenger (evt. må de fjernes).

MERK compile_pdf (bruk bash compile_pdf.sh) brukes for å endre tex-filene til å kunne bli kompilert med pdflatex mens compile_html lager tex-filene i formatet slik at de kan kompileres til html via main.py (se README.md)
