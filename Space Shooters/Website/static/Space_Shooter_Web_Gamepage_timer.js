//const StartMinuten =1;
let tijdLimiet = 10;

const timer = document.getElementById("timer")// declareer timer met de waarde uit de HTML file met de aangegeven ID

interval=setInterval(updatetimer,1000);//met setinterval roep ik de functie meerdere malen op net een delay van 1000 ms

interval;
function updatetimer() {
    //const minuten = Math.floor(time /60);
    let seconden = tijdLimiet;//seconden gelijk aan tijdlimiet


    timer.innerHTML = seconden;//verander de HTML waarde met de  met de gegeven waarde: seconden
    tijdLimiet--; //seconden -1
    if (seconden<=0){window.open("http://localhost:63342/space-invaders/Space%20Shooters/Website/templates/Space_Shooter_Web_NL_Scoreboard.html?_ijt=b8fr063qpcq50ub1rpg7vkhlo2","_self")
        clearInterval(interval)//hiermee stopik de interval(stop loop)
    }// als seconden onder of gelijk is aan 0 weergeef GAME OVER


}