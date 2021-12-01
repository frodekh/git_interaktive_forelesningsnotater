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

    if(historyCookies < 1){
        document.cookie = `history${historyCookies.length}=${history} ? ${datetime()};`
        return
    }
    if(historyCookies.length > 3){
        counter > 3 ? counter = 0 : counter++
        // console.log("counter: "+counter)
        document.cookie = `history${counter+1}=${history} ? ${datetime()};`
        return
    }

    document.cookie =  `history${historyCookies.length + 1}=${history}?${datetime()};`
}

function getHistory(){
    const historyCookies = document.cookie.split(';')
    let html = ''
    for(let i = historyCookies.length -1; i > 0 ; i--){
        let split = historyCookies[i].split( '=' );

        let link = split[1].split('?')[0]
        link = link.replace("https://acruxdb.uio.no","")
        let timestamp = historyCookies[i].split( '?' );
        timestamp = timestamp[timestamp.length - 1]
        
        let name = link.split("forelesninger/").pop()
 
        html += `<a href='${link}'><li class='list-group-item'>${name}<br/><span class='small-font'> ${timestamp} <span></li></a>`
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
