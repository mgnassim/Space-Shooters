const navSlide = () => {
    const menu = document.querySelector('.menu');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');

    menu.addEventListener('click', () => {
        nav.classList.toggle('nav-active');

        navLinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = '';
            } else {
            link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 1}s`;
            }
         });
         menu.classList.toggle('toggle');
    });
}   

navSlide();

const sections = document.querySelectorAll('section');
const border = document.querySelector('.border');
const gradients = ["linear-gradient(to right top, #f46b45, #eea849)",
"linear-gradient(to right top, #50ff61, #ffff)",
"linear-gradient(to right top, #f46b45, #50ff61)",
"linear-gradient(to right top, #ffff, #eea849)"];

const options = {
    threshold: 0.7
};

let observer = new IntersectionObserver(navCheck, options);

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
        if (entry.isIntersecting) {
            border.style.setProperty('left', `${directions.left}px`);
            border.style.setProperty('top', `${directions.top}px`);
            border.style.setProperty('width', `${directions.width}px`);
            border.style.setProperty('height', `${directions.height}px`);
        }
    });
}

sections.forEach(section =>{
    observer.observe(section);
});



