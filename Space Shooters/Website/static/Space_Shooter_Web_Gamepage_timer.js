//const StartMinuten =1;
let tijdLimiet = 60;

const timer = document.getElementById("timer")// declareer timer met de waarde uit de HTML file met de aangegeven ID

setInterval(updatetimer,1000);

function updatetimer() {
    //const minuten = Math.floor(time /60);
    let seconden = tijdLimiet;//seconden gelijk aan tijdlimiet


    timer.innerHTML = seconden;//verander de HTML waarde met de  met de gegeven waarde: seconden
    tijdLimiet--; //seconden -1
    if (seconden<=0){timer.innerHTML = "GAME OVER"}// als seconden onder of gelijk is aan 0 weergeef GAME OVER


}