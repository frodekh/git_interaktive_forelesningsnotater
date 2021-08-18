import re, os

buttons = """\\\\hyperlink\{(.*?)\}\{(.*button)\{(.*?)\}\}"""
frames = """<div class="frame">(.*?)<\/div>\s?(?=<div class="frame">|\Z)"""

ascii = """                   
                            _____ _    _  _____ _____ ______  _____ _____ _  
                     .::.  / ____| |  | |/ ____/ ____|  ____|/ ____/ ____| | 
                  .:'  .: | (___ | |  | | |   | |    | |__  | (___| (___ | | 
        ,MMM8&&&.:'   .:   \___ \| |  | | |   | |    |  __|  \___ \\\___ \| | 
       MMMMM88&&&&  .:'    ____) | |__| | |___| |____| |____ ____) |___) |_|  
      MMMMM88&&&&&&:'     |_____/ \____/ \_____\_____|______|_____/_____/(_) 
      MMMMM88&&&&&&                                                             
    .:MMMMM88&&&&&&    _  _ _   _ ___                              _          _ 
  .:'  MMMMM88&&&&    | || | | | | _ )  __ _ ___ _ _  ___ _ _ __ _| |_ ___ __| |
.:'   .:'MMM8&&&'     | __ | |_| | _ \ / _` / -_) ' \/ -_) '_/ _` |  _/ -_) _` |
:'  .:'               |_||_|\___/|___/ \__, \___|_||_\___|_| \__,_|\__\___\__,_|
'::'                                   |___/
                       _         ___         _           _   _         _
                  __ _| |_      / (_)_ _  __| |_____ __ | |_| |_ _ __ | |
                 / _` |  _|  _ / /| | ' \/ _` / -_) \ /_| ' \  _| '  \| |_
                 \__,_|\__| (_)_/ |_|_||_\__,_\___/_\_(_)_||_\__|_|_|_|_(_)

"""

def find_buttons(string):
    return re.findall(buttons, string)

def find_frames(string):
    return re.findall(frames, string, re.M|re.S)

def create_html_start(first_file):
    pass

def create_file_tree(fpath):
    dictCategoryFileTree = {}
    for root, dirs, files in os.walk(fpath, topdown=False):
        for name in dirs:
            split = os.path.join(root, name).split('/')

            
            split_category = str(split[2]) #split[2] = kategori, split[3] = underkategori/forelesningsdel

            #gitt at spliten lager en array med mer enn 3 entries, legg til i dictionary
            #os.walk henter alle mulige paths uten mulighet for å sette en length, vi vil ha de lengste pathene den henter
            if len(split) > 3:
                    
                if split_category not in dictCategoryFileTree:
                    dictCategoryFileTree[split_category] = []
                    dictCategoryFileTree[split_category].append(split[3])
                else:
                    dictCategoryFileTree[split_category].append(split[3])
    return dictCategoryFileTree

def create_html_file(fname: str, title: str, body: str) -> None:
    fopen = open(fname, 'w')
    file_str = r'<!DOCTYPE html>' + '\n'
    file_str += r'<html lang="en">' + '\n'
    file_str += r'<head>' + '\n'
    file_str += r'    <meta charset="UTF-8">' + '\n'
    file_str += r'    <meta http-equiv="X-UA-Compatible" content="IE=edge">' + '\n'
    file_str += r'    <meta name="viewport" content="width=device-width, initial-scale=1.0">' + '\n'
    file_str += f"    <title>{title}</title>" + '\n'
    file_str += r'    <link rel="stylesheet" href="../../style.css">' + '\n'
    file_str += r'    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>' + '\n'
    file_str += r'    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>' + '\n'
    file_str += r'    <script src="../../master.js"></script>' + '\n'
    file_str += r'</head>' + '\n'
    file_str += r'<body>' + '\n'
    file_str += body + '\n'
    file_str += r'</body>' + '\n'
    file_str += r'</html>' + '\n'
    
    fopen.write(file_str)
    fopen.close()

def create_hub_nav_html(fname: str) -> None:
    fopen = open("./index.html", 'w')
    html_start = """

        <!DOCTYPE html>
        <html lang="en" dir="ltr">

        <head>
            <meta charset="UTF-8">
            <link rel="stylesheet" href="hub_style.css">
            <link rel="stylesheet" href="lecture.css">
            <link href='https://unpkg.com/boxicons@2.0.7/css/boxicons.min.css' rel='stylesheet'>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
        </head>

        <body>
            <div class="sidebar">
                <div class="logo-details">
                    <div class="home-content">
                        <i class='bx bx-menu'></i>
                    </div>
                    <span class="logo_name">Interactive Lectures</span>
            
                    
                </div>
                <ul class="nav-links" id="nav-links">
                    <li>
                        <a href="#" onclick="setIframe()">
                            <i class='bx bx-grid-alt'></i>
                            <span class="link_name">Dashboard</span>
                        </a>
                        <ul class="sub-menu blank">
                            <li><a class="link_name" href="#">Dashboard</a></li>
                        </ul>
                    </li>
        """

    html_end = """
            <script>
                        let overflow;
                        let element = document.getElementById("nav-links");
                        element.addEventListener("click", () => {overflow = element.scrollHeight > element.clientHeight; console.log(overflow)});
                        
                        if(overflow){
                            
                        }

                    </script>
                    
                </ul>
                <nav class="nav-footer" id="nav-footer">
                        
                    <div class="container">
                        <input type="checkbox" class="checkbox" id="chk" />
                        <label class="label" for="chk">
                            <i class="fas fa-moon"></i>
                            <i class="fas fa-sun"></i>
                            <div class="ball"></div>
                        </label>
                        <p>Frodifiser</p>
                    </div>

                    <div class="container">
                        <input type="checkbox" class="checkbox" id="grayscale" />
                        <label class="label" for="grayscale">
                            <i class="fas fa-moon"></i>
                            <i class="fas fa-sun"></i>
                            <div class="ball"></div>
                        </label>
                        <p>Grayscale</p>
                    </div>

                    <div class="container">
                        <input type="checkbox" class="checkbox" id="music" />
                        <label class="label" for="music">
                            <i class="fas fa-moon"></i>
                            <i class="fas fa-sun"></i>
                            <div class="ball"></div>
                        </label>
                        <p>Konsemusikk</p>
                    </div>
                </nav>
            </div>



            <section class="home-section">
                <article class="lecture">
                    <div class="lecture-container" id="lecture-container">
                        <iframe class="iframe" src="forelesninger/dashboard.html" title="W3Schools Free Online Web Tutorials"></iframe>
                    </div>
                </article>
                <div id="player" style="position: fixed; left: -100%;"></div>

            <script>
            // 2. This code loads the IFrame Player API code asynchronously.
            var tag = document.createElement('script');

            tag.src = "https://www.youtube.com/iframe_api";
            var firstScriptTag = document.getElementsByTagName('script')[0];
            firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

            // 3. This function creates an <iframe> (and YouTube player)
            //    after the API code downloads.
            var player;
            function onYouTubeIframeAPIReady() {
                player = new YT.Player('player', {
                height: '300',
                width: '500',
                videoId: '5qap5aO4i9A',
                playerVars: {
                    'playsinline': 1
                },
                events: {
                    'onReady': onPlayerReady,
                    'onStateChange': onPlayerStateChange
                }
                });
            }

            // 4. The API will call this function when the video player is ready.
            function onPlayerReady(event) {
                
            }
            // 5. The API calls this function when the player's state changes.
            //    The function indicates that when playing a video (state=1),
            //    the player should play for six seconds and then stop.
            var done = false;
            function onPlayerStateChange(event) {
                if (event.data == YT.PlayerState.PLAYING && !done) {
                done = true;
                }
            }
            function stopVideo() {
                player.stopVideo();
            }
            </script>
            </section>

            <script>

                let arrow = document.querySelectorAll(".arrow");
                for (var i = 0; i < arrow.length; i++) {
                    arrow[i].addEventListener("click", (e) => {
                        let arrowParent = e.target.parentElement.parentElement;
                        arrowParent.classList.toggle("showMenu");
                    });
                }

                let sidebar = document.querySelector(".sidebar");
                let sidebarBtn = document.querySelector(".bx-menu");
                sidebarBtn.addEventListener("click", () => {
                    sidebar.classList.toggle("close");
                    document.getElementById('nav-footer').classList.toggle("close")
                });

                //lectures
                
                let lecturesButtons = document.querySelectorAll(".lecture-link");
                const iframe = document.getElementById("lecture-container");

                for (var i = 0; i < lecturesButtons.length; i++) {
                    lecturesButtons[i].addEventListener("click", (e) => {
                        setIframe(e);
                    });
                }
                function setIframe(e){
                    iframe.classList.add("global-fade-animation");

                    let src = e ? e.target.value : 'forelesninger/dashboard.html';
                    console.log(src)

                    setTimeout(() => {
                            
                            iframe.innerHTML = `<iframe class="iframe" src="${src}" title="W3Schools Free Online Web Tutorials"></iframe>`
                            iframe.classList.remove("global-fade-animation");

                        }, 300);
                }

                //frodifiser
                const frodifiserToggleSwitch = document.getElementById('chk');
                const grayscaleToggleSwitch = document.getElementById('grayscale');
                const musicToggleSwitch = document.getElementById('music');

                frodifiserToggleSwitch.addEventListener('change', () => {
                    frodifiser();
                });
                grayscaleToggleSwitch.addEventListener('change', () => {
                    grayscale();
                });
                musicToggleSwitch.addEventListener('change', () => {
                    lofibeatsGOGOGO();
                });
                function frodifiser(){
                    if(frodifiserToggleSwitch.checked){
                        document.documentElement.style.setProperty('--main-dark', 'orange');
                        document.documentElement.style.setProperty('--main-accent', 'green');
                        document.documentElement.style.setProperty('--main-white', 'red');
                        document.documentElement.style.setProperty('--body', 'yellow');
                    document.documentElement.style.setProperty('--active', 'blue');
                        
                        return;
                    }
                    document.documentElement.style.setProperty('--main-dark', '#11101d');
                    document.documentElement.style.setProperty('--main-accent', '#1d1b31');
                    document.documentElement.style.setProperty('--main-white', '#fff');
                    document.documentElement.style.setProperty('--body', '#e4e9f7');
                    document.documentElement.style.setProperty('--active', 'green');
                
                }

                function grayscale(){
                    if(grayscaleToggleSwitch.checked){
                        iframe.classList.add('lecture-grayscale')
                        return;
                    }
                    iframe.classList.remove('lecture-grayscale');
                }
                function lofibeatsGOGOGO(){
                    if(musicToggleSwitch.checked){
                        player.playVideo();
                        return;
                    }
                    player.stopVideo();

                }

            </script>
        </body>

        </html>
    """
    html_items = ""

    value = create_file_tree("./forelesninger/")
    keys = list(value.keys())
    keys.sort()

    for key in keys:
        value[key].sort()
        #print("key: ", key)
        #print("value: ", value[0])
        category = r"<!-- CATEGORY: "+key+r"  -->"+'\n'
        category += r'<li>' + '\n'
        category += r'    <div class="iocn-link">' + '\n'
        category += r'        <a href="#">' + '\n'
        category += r'        <i class="bx bx-collection" ></i>' + '\n'

        category += r'        <span class="link_name">'
        category += key #add category name
        category += r'</span>' + '\n'
        category += r'        </a>' + '\n'
        category += r'        <i class="bx bxs-chevron-down arrow"></i>' + '\n'
        category += r'    </div>' + '\n\n'

        #add files
        category += r'    <ul class="sub-menu">'  + '\n'
        for file in value[key]:
            if file == "media":
                continue
            category += r'        <li><button value="./forelesninger/'
            category += key
            category += "/"
            category += file
            category += r'/front.html'
            category += r'" class="lecture-link">'
            category += file
            category += r'</button></li>'  + '\n'
        category += r'     </ul>' + '\n'
        category += r'</li>' + '\n\n'
        category += r'<!-- ############################################# --->'+'\n\n'
        html_items += category + '\n'

    out = html_start + html_items + html_end
    try:
        fopen.write(out)
        fopen.close()
        print(ascii)
    except:
        print("Something went wrong when trying to generate HTML... ")
        exit()

def main():
    # Check requirement and print error if pandoc is missing
    import sys, subprocess
    from shutil import which
    
    if which("pandoc") is None:
        print("This script requires Pandoc to work.")
        print("Please install Pandoc by running 'brew install pandoc'")
        print("Exiting...")
        exit()

    if len(sys.argv) > 1:
        files_list = sys.argv[1:]
    else:
        files_list = [input("Please enter a file name:\n")]

    for fname in files_list:
        fname_list = fname.split('_')
        if len(fname_list) > 3:
            pathname = "forelesninger/" + fname_list[2] + '/' + fname_list[3]
        else:
            pathname = "forelesninger/" + fname_list[2][:-4] + '/' + fname_list[2][:-4]
        if not os.path.exists(pathname + "/"):
            os.makedirs(pathname)
        if fname[-4:] != ".tex":
            print(f"Warning! File {fname} is not a .tex file! This could cause problems, or just weird output file names!")
        file_latex = open(fname, 'r')
        latex_file_str = file_latex.read()
        file_latex.close()
        #latex_file_str = re.sub('%.*', "", latex_file_str)
        # remove all mini-pages, as they mean the frame won't be translated
        # redefine button commands to return plain text
        
        latex_substitutions = [
            ('\\\\(?:begin|end)\{minipage\}(?:\{.*?\})?', ''),
            ('\\\\newcommand\{\\\\padletbutton\}\{(.*?)\}.*', '\\\\newcommand{\\\\padletbutton}{\\1}{PADLET}}'),
            ('\\\\Changey\[1\]\[yellow\]\{2\}', '🙂'),
            ('\\\\Changey\[1\]\[yellow\]\{-2\}', '🙁'),
            ('(\\\\newcommand{\\\\(?:d?next|cur)page).*', '\\1}{}'),
            ('\\\\newcommand\{(\\\\(?:.*?)button)\}\[1\]\{\\\\setbeamer.*', '\\\\newcommand{\\1}[1]{#1}'),
            #('\\\\setbeamercolor.*', '')
            ('\{\n\\\\setbeamercolor.*', '{\n')
            #('\\\\end\{frame\}\n\}', '\\\\end{frame}')
        ]
        
        for subpair in latex_substitutions:
            latex_file_str = re.sub(subpair[0], subpair[1], latex_file_str)

        """
        latex_file_str = re.sub('\\\\(?:begin|end)\{minipage\}(?:\{.*?\})?', '', latex_file_str)
        latex_file_str = re.sub('\\\\newcommand\{\\\\padletbutton\}\{(.*?)\}.*', '\\\\newcommand{\\\\padletbutton}{\\1}{PADLET}}', latex_file_str)
        latex_file_str = re.sub('\\\\Changey\[1\]\[yellow\]\{2\}', '🙂', latex_file_str)
        latex_file_str = re.sub('\\\\Changey\[1\]\[yellow\]\{-2\}', '🙁', latex_file_str)
        latex_file_str = re.sub('(\\\\newcommand{\\\\(?:d?next|cur)page).*', '\\1}{}', latex_file_str)
        latex_file_str = re.sub('\\\\newcommand\{(\\\\(?:.*?)button)\}\[1\]\{\\\\setbeamer.*', '\\\\newcommand{\\1}[1]{#1}', latex_file_str)
        """

        hypertargets = re.findall('\\\\hyperlink\{(.*?)\}\{.*?\}+\s\\\\hypertarget<\.>\{(.*?)\}', latex_file_str)
        for target in hypertargets:
            latex_file_str = re.sub('\\\\hyperlink\{%s\}' % target[1], '\\\\hyperlink{%s}' % target[0], latex_file_str)
        
        #latex_file_str = re.sub('\\\\newcommand\{(\\\\(?:d?next|cur)page).*', '\\\\newcommand{dnextpage}{test}', latex_file_str)
        latex_tmp = open(fname + '_tmp', 'w')
        latex_tmp.write(latex_file_str)
        latex_tmp.close()
        output = subprocess.run(["pandoc", "-f", "latex", "-t", "html5", fname + '_tmp'], capture_output=True, text=True).stdout
        #os.remove(fname + '_tmp')

        debug_singlefile = ""

        for frame in find_frames(output):
            frame_id = re.findall('<span id="(.*?)" label', frame)[0]

            html_substitutions = [
                ('\[.*?\]', ''),
                ('<img src="(.*?)"', '<img src="../media/\\1"'),
                ('<a href="(https:\/\/www.uio.*?.mp4)">(.*?)<\/a>', '\\2 <video width="320" height="240" controls><source src="\\1" type="video/mp4">Your browser does not support the video tag.</video><br>'),
                ('<a href="#(.*?)">(.*?)</a>', '<a href="\\1.html">\\2</a>'),
                (' ', ' '),
                ('<a href="(.*?)">Trykk her (.*?)<\/a>', '<a href="\\1" class="trykkher">Trykk her \\2</a>'),
                ('<a href="(.*?)">(Forrige|Neste) side<\/a>', '<a href="\\1" class="nesteforrigeside">\\2 side</a>'),
                ('<a href="(.*?)">(Forrige|Neste) side<\/a>', '<a href="\\1" class="nesteforrigeside">\\2 side</a>'),
                ('<a href="(.*?)">(Ja|Nei)<\/a>', '<a href="\\1" class="janei">\\2</a>'),
                ('<a href="(.*?)">🙂 🙁<\/a>', '<a href="\\1" class="🙂🙁">🙂 🙁</a>'),
                ('style="color: white"', 'style="color: red"')
            ]

            for subpair in html_substitutions:
                frame = re.sub(subpair[0], subpair[1], frame)

            debug_singlefile += frame
            create_html_file(f"{pathname}/{frame_id}.html", frame_id, frame)

        if len(fname_list) > 3:
            create_html_file(f"{pathname}/{fname_list[2] + '_' + fname_list[3]}.html", "Entire file", debug_singlefile)
        else:
            create_html_file(f"{pathname}/{fname_list[2][:-4]}.html", "Entire file", debug_singlefile)

        try:
            os.mkdir(f"{'/'.join(pathname.split('/')[:-1])}/media")
        except FileExistsError:
            # We can't get the file path outside this loop, and creating the dir twice raises an exception
            pass

    print("Converting latex...")
    print('[' + 78 * '#' + ']')
    create_hub_nav_html("index.html")

if __name__ == "__main__":
    main()