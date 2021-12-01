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
            hethree: "\\atom{3}{2}{He}",

            ss: "Schwarz\-schild",
            densu: ""
        }
    }
};


// const imagezoom = (element) =>{

//     //i programmet har iframen en ID (tror det er #iframe?). 
//     // bruk document.getElementById(**iframe id-en**).width
//     //eks:  const iframeWidth = document.getElementById(**iframe id-en**).width
    
//     const iframeWidth = document.getElementById('iframe')
//     console.log(iframeWidth, "WDITH")
//     const scale = iframeWidth / (element.width / 0.8)
//     const scale = 1
    
//     if(element.classList.contains('active-js')){
//         element.classList.remove('active-js')
//         element.style.transform = `scale(1)`
//         return
//     }
    
//     element.classList.add('active-js')
//     element.style.transform = `scale(${scale})`

   
// }

window.addEventListener('DOMContentLoaded', (event) => {
    //fix for image size
    const nmbimgtags = document.querySelectorAll('img').length
    
    if (nmbimgtags > 1) {
        let image_tags = document.querySelectorAll('img')
        for (let i = 0; i < nmbimgtags; i++) {
            image_tags[i].classList.add("float-image-fix");
        }
    }


    //check if page title should be a right or wrong answer 
    //by asserting the page title, sets bg color thereafter in the starting html-tag
    let title = document.title
    console.log(title)
    if(title.includes("feil")){
        const ele = document.documentElement
        ele.style.backgroundColor = 'black'
        return
    }
    if(title.includes("riktig") || title.includes("rett")){
        const ele = document.documentElement
        ele.style.backgroundColor = 'yellow'
        return
    }
    if(title.includes("brown")){
        const ele = document.documentElement
        ele.style.backgroundColor = 'brown'
        return
    }
    if(title.includes("pause")){
        const ele = document.documentElement
        ele.style.backgroundColor = 'deepskyblue'
        return
    }
    if(title.includes("red")){
        const ele = document.documentElement
        ele.style.backgroundColor = 'red'
        return
    }
    if(title.includes("blue")){
        const ele = document.documentElement
        ele.style.backgroundColor = 'blue'
        return
    }
    if(title.includes("denim")){
        const ele = document.documentElement
        ele.style.backgroundColor = 'rgb(15, 74, 140)'
        return
    }
    if(title.includes("tema")){
        const ele = document.documentElement
        ele.style.backgroundColor = 'blue'
        
        const p = document.querySelectorAll('p');
        p[1].style.fontSize = '50px'
        p[1].style.textAlign = 'center'
        p[2].style.fontSize = '20px'
        p[3].style.fontSize = '35px'
        p[3].style.textAlign = 'center'
        console.log(p)
        return
    }
    //manual fix for "er du sikker???" pages
    if(title.includes("sikker")){
        const p = document.querySelectorAll('strong');
        p.forEach(element => {
            element.style.fontSize = '30px'
        });
        const ele = document.documentElement
        ele.style.backgroundColor = 'red'
        return
    }
})

const imageZoomOverlay = (element) => {

    const img = document.createElement("img");
    img.src = element.src
    img.classList.add('img-overlay')           

    const iframeWidth = document.documentElement.clientWidth
    const iframeHeight = document.documentElement.clientHeight
    if( (iframeHeight / element.height) >= (iframeWidth / element.width)){
        var scale = (iframeHeight / element.height)**1/2 * 0.8
    }
    else {
        var scale = (iframeWidth / element.width)**1/2 * 0.8
    }

    img.style.cssText = `transform: translate(-50%, -50%) scale(${scale}, ${scale}); `

    document.documentElement.appendChild(img)

    removeZoomItem()

}
const removeZoomItem = () => {
    document.querySelector('.img-overlay').addEventListener('click', (element) =>{
        element.target.classList.add('zoomout')
        setTimeout(() => {
            element.target.remove()
        }, 200);
        
    })
}
