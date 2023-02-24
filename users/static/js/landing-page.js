// Add some animation using JavaScript
const landingPage = document.querySelector('.landing-page');
const image = landingPage.querySelector('img');
const heading = landingPage.querySelector('h1');

// Move the image up and fade it in when the page loads
image.style.opacity = 0;
image.style.transform = 'translateY(-50px)';
image.style.transition = 'opacity 1s ease-in-out, transform 1s ease-in-out';
setTimeout(() => {
    image.style.opacity = 1;
    image.style.transform = 'translateY(0)';
}, 500);

// Make the heading fade in and out
heading.style.opacity = 0;
heading.style.transition = 'opacity 1s ease-in-out';
setInterval(() => {
    if (heading.style.opacity === '0') {
        heading.style.opacity = 1;
    } else {
        heading.style.opacity = 0;
    }
}, 2000);
