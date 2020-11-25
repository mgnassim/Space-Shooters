//Hier worden de navigation slide opgevraagd in de website
const navSlide = () => {
    const menu = document.querySelector('.menu');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');

    //Hier wordt een functie toegevoegd
    menu.addEventListener('click', () => {
        nav.classList.toggle('nav-active');

        //Hier wordt een loop gemaakt zodat hij niet blijft hangen na 1 keer
        navLinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = '';
            } else {
                //Hier wordt een smooth delay gemaakt voor de slide
            link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.6}s`;
            }
         });
         menu.classList.toggle('toggle');
    });
}
//Hier wordt de functie opgevraagd zodat hij werkt
navSlide();

//Hier wordt op de pagina gekeken naar hoe de pagina eruit ziet, om te herkennen wanneer hij op de pagina is
const sections = document.querySelectorAll('section');
const border = document.querySelector('.border');
const gradients = ["linear-gradient(to right top, #f46b45, #eea849)",
"linear-gradient(to right top, #50ff61, #ffff)",
"linear-gradient(to right top, #f46b45, #50ff61)",
"linear-gradient(to right top, #ffff, #eea849)"];

//Hier wordt bepaalt bij hoeveel procent hij de pagina herkent
const options = {
    threshold: 0.7
};

let observer = new IntersectionObserver(navCheck, options);

//Hier wordt aangegeven waar op de pagina alles staat, hierdoor weet hij waar de kleuren zijn etc.
function navCheck(entries){
    entries.forEach(entry =>{
        const className = entry.target.className;
        const activeAnchor = document.querySelector(`[data-page=${className}]`);
        const gradientIndex = entry.target.getAttribute('data-index');
        const coords = activeAnchor.getBoundingClientRect();
        const directions = {
            height: coords.height,
            width: coords.width,
            top: coords.top,
            left: coords.left
        };
        //Hier wordt een loop gemaakt zodat hij steeds weer door gaat
        if (entry.isIntersecting) {
            border.style.setProperty('left', `${directions.left}px`);
            border.style.setProperty('top', `${directions.top}px`);
            border.style.setProperty('width', `${directions.width}px`);
            border.style.setProperty('height', `${directions.height}px`);
        }
    });
}
//Hier wordt de functie weer opgevraagd
sections.forEach(section =>{
    observer.observe(section);
});



