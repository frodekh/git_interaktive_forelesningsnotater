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
        document.cookie = `history${historyCookies.length}=${history} ? ${datetime()};`
        return
    }
    if(historyCookies.length > 3){
        counter > 3 ? counter = 0 : counter++
        console.log("counter: "+counter)
        document.cookie = `history${counter+1}=${history} ? ${datetime()};`
        return
    }

    document.cookie =  `history${historyCookies.length + 1}=${history}?${datetime()};`
}

function getHistory(){
    const historyCookies = document.cookie.split(';')
    let html = ''
    for(let i = 0; i < historyCookies.length; i++){
        let split = historyCookies[i].split( '=' );
        let timestamp = historyCookies[i].split( '?' );
        let link = split[1].split('?')
        let name = split[1].split('/')
        let file = name[6].split('?')
        console.log(timestamp, split, name, link)

        //console.log(name)
        html += `<li class="list-group-item"><a href="${link[0]}">${name[4]} ${name[5]} (${file[0]})<br/><span class="small-font"> ${timestamp[1]} <span></a></li>`
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
    let s = today.getSeconds()

    if(s < 10){
        s = '0'+s
    }

    return dd + '/' + mm + '/' + yyyy + " kl: "+h+":"+m+":"+s;
}
