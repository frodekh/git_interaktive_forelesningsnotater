# Notes to self
har endret html og css til huben, dette må tas hensyn til når hub genereres.

På nytema-html sidene virker det som noe tekst er forsvunnet under konverting, må sjekkes!
#
# Project status
## Kritiske
- [x] trenger readme for å vite hvordan bruke koden.

- [ ] Kritisk: gjelder de fleste forelesningsnotater. F.eks. i del 1A, del
2, for slidene under taggene 'ideelgass2' og 'ideelgass3' så er det
mange 'trykk her'-knapper hvor setningen skal dukke opp på sliden en
etter en ettersom man trykker. Dette ser ikke ut til å funke her...
Dette er en viktig funksjon i flere slider og i de aller fleste av
forelesningsnotatene.

- [ ] Kritisk:  Problemer med boksene (de forskjellige blocks, alterblock
etc.), noen ganger legger de seg over figurer, andre ganger blir teksten
konsentrert i en del av boksen, noen ganger får de feil tekst i fanenMarkdown Checkboxes
Markdown Checkboxes

over etc., se detaljer over hva og hvor for hver slide hvor problemet
dukker opp i lista under

- [ ] Kritisk:  Stort sett problemer med nesten alle linker til sider
utenfor forelesningsnotatene, jeg har tatt med en del eksempler i lista
under. Det beste hadde vært om disse åpnes i en ny tab.

- [x] Kritisk: Noe er rart med linkingen mellom sider (neste, og forrige
side-knapper) i del1b (mener Frode 1C? ingen rm2.html i 1b... -sondre), del 2 slik at man ikke kommer seg videre: FraMarkdown Checkboxes.
sliden med taggen rm2 går jeg tilbake igjen til siden før når jeg
trykker på 'neste side'. (dette skjer ikke i latex). Også 'forrige
side'-knappen leder til feil side. 

- [x] Kritisk: del 2A, del1, slide med tag tog26 OG del 2A, del 2, tag rep3,
på disse sidene ble det mye rart både med tekst, video og lenker

- [x] TODO!!!!!!!!!!! FIX: ny HTML OG CSS. Kritisk: del 3E får jeg ikke åpnet, tror dette er et problem med
menyen siden den står helt nederst og ikke dukker opp når jeg trykker på
pila. 

- [ ] skriftstørrelsen er den samme hele tiden på html-sidene mens den
endrer seg ganske mye i latex-dokumentet (brukes som pedagogisk virkemiddel)
MULIG FIX: https://stackoverflow.com/questions/27000906/how-to-set-the-font-size-for-code-blocks-in-pandoc-markdown

- [x] mulighet for å forstørre figurer ved å flytte markøren over (evt,
hadde vært enda bedre: kunne utnytte større andel av skjermen for
slidene slik at alt blir større) -forstørret forelesnigene, men ikke testet på alle skjermer så mulig det ikke funker overalt, sondre

- [ ] når jeg prøver å zoome inn og deretter scrolle oppover eller nedover
på siden så får jeg ikke scrollet. Jeg får altså kun forstørret det som
står midt på siden. Dette problemet er kun på IPAD, IKKE på laptoppen.

- [x] en eller annen måte å kjapt bla frem/tilbake i dokumentet slik at man
fort kan forsette der man slapp.
FIXED: implementert en historikkliste i dashboard.html
Sondre: kanskje gjøre landingssidene til hver forelesning en liste over alle slides? Kombinere dette med sidetall? Bruker kan se at den sist var på side 30 i en gitt slide, alle sidene med linker til riktig slide er lagt inn i landingssiden til gitt forelesning.
En annen måte: bruke lage en tab i huben som inneholder siste x forelesningsslidene man har besøkt, lagre dette i session eller cookie, neste gang man åpner siden (i samme browser), får man en liste over hvor man slapp sist liksom. 

- [ ] progressbar ELLER sidetall (det siste kan vi evt. få inn på måten jeg
skisserte ved at jeg legger inn stikkord med sidetall)



#
## Mindre/mer spesifikke feil:
### (mange er gjengangere, samme problem over flere slides/forelesninger)

- [ ] del1a, del 1, side 2: "har du gått gjennom disse etc" kommer i blå
fane over det brune. Alts skal stå i det brune. "VIKTIG" som egentlig
skulle stå i den blå fanen kommer ikke med. Samme skjer i andre
forelesningsnotater på den samme siden, for noen så forsvinner deler av
teksten.

- [ ] "trykk denne knappen"-knappen har blitt brun istedenfor grønn

- [ ] forum-knappen er rar (1A, del1)

- [ ] mangler blå bakgrunn runt temaet helt øverst

- [ ] mangler blå bakgrunn på nytema-side

- [ ] rød skriftfarge på 'feil'-sidene, skal være hvit

- [ ] del 1A, del 1, i sliden tagget 'gassstat' blir latexen litt rar for
uttrykket v_j(i) inne i teksten

- [ ] noen få sider skal ha rød bakgrunn (men har det ikke), kan vi få inn
et stikkord for å få til dette?

- [ ] del 1A, del2, sliden om sentralgrenseteoremet: "kall midlet a_j
(j=)??????"

- [ ] del 1A, del2, for sliden under taggen 'stat13' så funker ikke linken
for random.seed

- [ ] Mange linker åpner ikke i en ny tab, man må trykke 'tilbake' for å
komme tilbake til forelesningsnotatene. For eksempel i del 1A, del 2,
for sliden under taggen 'stat13'.

- [ ] del 1B, del1, sliden med taggen basicfysikk2a, her mangler figuren
samtidig som boksen veldig stor og tom på den ene siden.

- [ ] del 1B, del1, sliden med taggen hastighet6, P^2, her kommer indeksen 2
helt oppi bokstaven P.

- [ ] del 1B, del1, sliden med taggen kepler6, her er det problemer med
likningen, kommer opp melding "Missing dimension or its units for
\hspace", er dette feil fra pandoc?

- [ ] del 1B, del1,  sliden med taggen kepler7, noe ble veldig rart i denne
boksen

- [ ] del 1B, del2,  sliden med taggen oppgaver2, boksen kommer delvis over
teksten over

- [ ] del 1C, del1,  sliden med taggen litenvinkel4, linken til SNL, på
laptoppen får jeg beskjed om at SNL ikke tillater at siden embeddes og
må åpnes i separat vindu, på ipaden skjer ingenting når jeg trykker på
linken, Igjen så er der vel best om linken åpnes i egen tab

- [ ] del 1C, del1,  sliden med taggen vr5, noe rart skjer i latex-formelen,
kan det være kommandoen 'mathcircled'? (egendefinert, bruker tikz-pakken)

- [ ] del 1C, del1,  sliden med taggen mp5, boksen ligger over figuren og
halvparten av boksen er tom.

- [ ] del 1C, del1,  sliden med taggen mp11, link til animasjon funker ikke,
samme gjelder taggen mp13, ingen av 'her'-linkene funker.

- [ ] del 1C, del2,  slidene med taggen fv og rv, begge liker til samme
video men finner ikke linken

- [ ] del 1C, del2,  sliden med taggen stat2, feil knapp som gir riktig
resultat (bare sammenlikn med latex-fila, der er det en annen knapp som
fører til riktig resultat)

- [ ] del 1D, del1, alle slidene fra straling5 til straling8, igjen skjer
det rare ting med boksen, spesielt så står det nå plutselig 'Viktig' i
rammen over, men det står det ingen steder i latex-fila for den sliden.

- [ ] del 1D, del2,  sliden med taggen rrlambda mangler figur

- [ ] del 1D, del2,  sliden med taggen rmag, noe rart i latexen her (f_2100)
i tillegg til det vanlige problemet med boksen.

- [ ] del 1D, del2,  sliden med taggen magnitudes11, boksproblemer

- [ ] del 1F, slidene med taggen rotkurv0 og rotkurv4, mangler figur

- [ ] del 1F, slidene med taggen mm0 og hvamm6, linken til youtube, på
laptoppen får jeg beskjed om at youtube ikke tillater at siden embeddes
og må åpnes i separat vindu, på ipaden skjer ingenting når jeg trykker
på linken, Igjen så er der vel best om linken åpnes i egen tab (gjelder
alle youtube-videoer i alle forelesninger, f.eks. også del 2B del 1
slide td25)

- [ ] del 1G, under intro dukker 'neste side'-knappen opp to ganger

- [ ] del 1G, sliden prom4 og prom4b, mangler figur

- [ ] del 1G, her er det noen sider som har brun bakgrunn, det må vi få inn
på en eller annen måte

- [ ] del 1G, sliden prom10, her strekker liningene seg utenfor boksene

- [ ] alle del2-forelesningene har en link til de anbefalte bøkene i
introduksjonen. Denne linken funker ikke.

- [ ] del 2A, del1, slidene kr7 til kr10, mangler figur

- [ ] del 2A, del2 slide rep7, del 2B del 1 slide td12, er det mulig å
kopiere over videoene i dette tilfellet og få dem rett inn i sliden slik
som med forelesningsvideoene?

- [ ] del 2A, del2, slidene nytema2 og eks1 kommer sammen på en og samme slide.

- [ ] del 2B, del2, sliden pe12x, i nederste likning står det (hv,-hv) mens
det skal stå h\nu, virker som \nu blir oversatt til et tegn som er
identisk med v

- [ ] del 2B, del2, sliden pe19, det som skal være d'Almbert-operatoren,
altså et kvadrat som er tomt inne i (akkurat som nabla er en trekant),
\square i latex, blir til et fylt kvadrat isteden.

- [ ] del 2C, del1, OG del 2D, figuren i introduksjonssliden mangler

- [ ] I del 2C del 1, ca. 3 sider etter introduksjonen så plutselig dukker
det opp noen 'ab', 'cd', etc. rundt omkring. Dette fortsetter på de
etterfølgende sidene

- [ ] Dette er gjennomgående i hele 2C og 2D: F.eks. i del 2C del 2 også ca.
3 sider etter introduksjonen, så står det beta-geometri (der beta er den
greske bokstaven). Dette skulle vært "Schwarzschild-geometri'. Jeg har i
latex definert \ss til å være Schwarzschild. På en eller annen måte så
blir denne til en gresk beta... Dette er gjennomgående i hele 2C og 2D
der \ss-definisjonen brukes.

- [ ] I del 2D, slidene eu9, eu10, eu12, eu15, eu24, og deretter fra skra12
og gjennomgående frem til pause2 samt noen slides også etter det:
latex-problem, formeler kommer ikke opp (er nok formler med noen felles
elementer som den sliter med)

- [ ] I del 2D, skra36, link til Nature funker ikke

- [ ] I del 3A, slide paral18 og paral19a og fra msfit7 hele veien til
msfit18, mangler figur

- [ ] I del 3A, slide di16, uendelighetstegnet i integralt kommer veldig
langt vekk fra integralet

- [ ] I del 3B, slide jeans6, likningene strekker seg ut av boksene

- [ ] I del 3C, slide reak3, reak5, reak7, snp2 og snp3: her skjer det mye
rart, både med boksen, likninger og figurer...

- [ ] I del 3D, del 1, her er det store problemer med figurer som mangler
gjennom hele notatet

- [ ] I del 3D, del 2, slide ms16b2, figur mangler

- [ ] I del 3D del2, slidene fra se4 til se8, det vanlige 'block'-problemet,
'viktig' dukker opp i overskriften (uten at det finnes i latex)