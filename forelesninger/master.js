window.MathJax = {
    tex: {
        inlineMath: [['$', '$'], ['\\(', '\\)']],
        macros: {
            atom: ["^{#1}_{#2}{\\rm #3}", 3],
            VEV: ["\\langle#1\\rangle", 1],
            sst: "\\left(1-\\frac{2M}{r}\\right)",
            sh: "\\mathrm{shell}",
            be: "\\begin{equation}",
            ee: "\\end{equation}",
            bue: "\\begin{equation}",
            eue: "\\end{equation}",
            bc: "\\begin{center}",
            ec: "\\end{center}",
            bea: ["\\begin{eqnarray}\\label{#1}", 1],
            eea: "\\end{eqnarray}",
            bua: "\\begin{eqnarray*}",
            eua: "\\end{eqnarray*}",
            dd: ["{{d#1}\\over{d#2}}", 2],
            ddt: ["\\dd{#1}{t}", 1],
            dddt: ["\\dd{^2#1}{t^2}", 1],
            aver: ["\\langle{#1}\\rangle", 1],
            electron: "\\atom{~0}{-1}{e}",
            positron: "\\atom{0}{0}{\\bar{e}}",
            neutrino: "\\atom{0}{0}{\\nu_e}",
            photon: "\\atom{0}{0}{\\gamma}",
            antineutrino: "\\atom{0}{0}{\\bar{\\nu}}",
            neutron: "\\atom{1}{0}{n}",
            proton: "\\atom{1}{1}{p}",
            hydrogen: "\\atom{1}{1}{H}",
            deuterium: "\\atom{2}{1}{H}",
            tritium: "\\atom{3}{1}{H}",
            helium: "\\atom{4}{2}{He}",
            hethree: "\\atom{4}{3}{He}",

            ss: "Schwarz\-schild",
            densu: ""
        }
    }
};

window.addEventListener('DOMContentLoaded', (event) => {
    //fix for image size
    const nmbimgtags = document.querySelectorAll('img').length
    console.log(nmbimgtags)
    if (nmbimgtags > 1) {
        let image_tags = document.querySelectorAll('img')
        for (let i = 0; i < nmbimgtags; i++) {
            image_tags[i].classList.add("float-image-fix");
        }
    }

    //check if page title should be a right or wrong answer 
    //by asserting the page title, sets bg color thereafter
    let title = document.title
    if(title.includes("feil")){
        document.body.style.backgroundColor = "black";
    }
    if(title.includes("riktig") || title.includes("rett")){
        document.body.style.backgroundColor = "yellow";
    }
})