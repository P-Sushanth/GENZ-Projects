// Smooth Scroll Lenis
const lenis = new Lenis({
    lerp: 0.1,
    wheelMultiplier: 0.7,
    smoothTouch: false
});

function raf(time) {
    lenis.raf(time);
    requestAnimationFrame(raf);
}
requestAnimationFrame(raf);

// GSAP ScrollTrigger
gsap.registerPlugin(ScrollTrigger);

// Hero Reveal
const heroEl = document.querySelector('[data-hero-blur]');
if (heroEl) {
    gsap.to(heroEl, {
        opacity: 1,
        filter: "blur(0px)",
        duration: 1.5,
        ease: "power2.out",
        delay: 0.2
    });
}

// Element Reveals
const reveals = gsap.utils.toArray('.gs-reveal, .gallery-item');
reveals.forEach((element) => {
    gsap.fromTo(element,
        { opacity: 0, y: 30, filter: "blur(10px)" },
        {
            opacity: 1,
            y: 0,
            filter: "blur(0px)",
            duration: 1,
            ease: 'power2.out',
            scrollTrigger: {
                trigger: element,
                start: "top 90%",
                toggleActions: "play none none reverse"
            }
        }
    );
});

// Interactive Shadow
document.addEventListener('mousemove', function (e) {
    const shadowElements = document.querySelectorAll('.shadow');
    const { clientX: mouseX, clientY: mouseY } = e;

    shadowElements.forEach(element => {
        const rect = element.getBoundingClientRect();
        const centerX = rect.left + rect.width / 2;
        const centerY = rect.top + rect.height / 2;

        const deltaX = mouseX - centerX;
        const deltaY = mouseY - centerY;

        const shadowX = deltaX / 25;
        const shadowY = deltaY / 25;
        const blurAmount = Math.max(20, (Math.abs(deltaX) + Math.abs(deltaY)) / 12);

        element.style.boxShadow = `${shadowX}px ${shadowY}px ${blurAmount}px rgba(255, 215, 0, 0.07)`;
    });
});

// Sticky Nav Shrink
window.addEventListener('scroll', () => {
    const nav = document.querySelector('.nav-wrapper');
    if (window.scrollY > 50) {
        nav.classList.add('scrolled');
    } else {
        nav.classList.remove('scrolled');
    }
});

// Lightbox Functionality
const initLightbox = () => {
    const lightbox = document.createElement('div');
    lightbox.className = 'lightbox-modal';
    lightbox.innerHTML = `
    <span class="lightbox-close">&times;</span>
    <img class="lightbox-content" src="" alt="Full view">
  `;
    document.body.appendChild(lightbox);

    const lightboxImg = lightbox.querySelector('.lightbox-content');

    // Select all images in galleries and project headers
    const images = document.querySelectorAll('.gallery-item img, .project_header img');

    images.forEach(img => {
        img.style.cursor = 'zoom-in';
        img.addEventListener('click', (e) => {
            e.stopPropagation();
            lightboxImg.src = img.src;
            lightbox.classList.add('active');
            document.body.style.overflow = 'hidden';
        });
    });

    lightbox.addEventListener('click', () => {
        lightbox.classList.remove('active');
        document.body.style.overflow = '';
    });
};

// Homepage Specific Logic
const initHomepage = () => {
    // Masonry Column Split
    const wrapper = document.querySelector('.projects-home-wrapper');
    if (wrapper) {
        const items = Array.from(wrapper.querySelectorAll('.project-home-item'));
        if (items.length >= 2 && window.innerWidth > 1024) {
            const leftColumn = document.createElement('div');
            const rightColumn = document.createElement('div');
            leftColumn.classList.add('column-left');
            rightColumn.classList.add('column-right');

            items.forEach((item, index) => {
                if (index % 2 === 0) leftColumn.appendChild(item);
                else rightColumn.appendChild(item);
            });
            wrapper.innerHTML = '';
            wrapper.appendChild(leftColumn);
            wrapper.appendChild(rightColumn);
        }
    }

    // Animated Counters
    const counters = document.querySelectorAll('.impact-number');
    counters.forEach(counter => {
        const target = +counter.getAttribute('data-count');
        let obj = { val: 0 };
        gsap.to(obj, {
            val: target,
            duration: 2.5,
            ease: "power2.out",
            scrollTrigger: {
                trigger: counter,
                start: "top 90%",
                once: true
            },
            onUpdate: function () {
                counter.innerText = Math.floor(obj.val) + '+';
            }
        });
    });
};

document.addEventListener('DOMContentLoaded', () => {
    initLightbox();
    initHomepage();
});
