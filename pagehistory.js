var counter = 0;
function iframeclick() {
    const iframe = document.getElementById("iframe")
    const history = iframe.contentWindow.location.href
    
    if(history.includes('dashboard.html')){
        //dont include dashboard.html in history
        console.log("history.html detected, exiting")
        return
    }
    const historyCookies = document.cookie.split(';')
    //console.log("historycookies: " + historyCookies)

    if(historyCookies < 1){
        document.cookie = `history${historyCookies.length}=${history};`
        return
    }
    if(historyCookies.length > 3){
        counter > 3 ? counter = 0 : counter++
        console.log("counter: "+counter)
        document.cookie = `history${counter+1}=${history};`
        return
    }

    document.cookie =  `history${historyCookies.length + 1}=${history};`
}

function getHistory(){
    const historyCookies = document.cookie.split(';')
    let html = ''
    for(let i = 0; i < historyCookies.length; i++){
        let split = historyCookies[i].split( '=' );
        let name = split[1].split('/')
        //console.log(name)
        html += `<li><a href="${split[1]}">${name[4]} ${name[5]} (${name[6]}) • ${datetime()}</a></li>`
    }
    //console.log(html)

    return html
}

const datetime = () => {
    var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    var yyyy = today.getFullYear();

    let h = today.getHours()
    let m = today.getMinutes()


    return dd + '/' + mm + '/' + yyyy + " kl: "+h+":"+m;
}
