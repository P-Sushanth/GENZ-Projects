import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the SVG
svg_match = re.search(r'(<svg[^>]*>.*?</svg>)', content, re.DOTALL)
if not svg_match:
    print("Could not find SVG in index.html")
    svg = "<!-- SVG Logo goes here -->"
else:
    svg = svg_match.group(1)
    # Give the SVG a simpler class instead of keeping original width
    if 'class="logo-svg"' not in svg:
        svg = svg.replace('<svg ', '<svg class="logo-svg" ')

new_head = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="GENZ Projects is a premier architecture firm specializing in interiors, residential, and landscape design projects." />
    <title>GENZ Projects - Architecture Firm</title>
    
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;700&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="style.css">
</head>
<body class="u-theme-dark">

    <div class="nav-wrapper">
        <div class="nav-inner">
            <div class="nav-inner_wrapper">
                <a href="#works" class="nav-link-wrapper">Works</a>
                <a href="#about" class="nav-link-wrapper">About</a>
            </div>
            
            <a href="#" class="logo-wrapper w-inline-block">
"""

new_tail = """
                <img src="images/homepage/text.webp" alt="GENZ Projects Logo Text" loading="lazy" style="height:40px; margin-top:0.5rem;" />
            </a>

            <div class="nav-inner_wrapper">
                <a href="#impact" class="nav-link-wrapper">Impact</a>
                <a href="#contact" class="nav-link-wrapper">Contact</a>
            </div>

            <!-- Mobile nav trigger -->
            <div class="mobile-nav-toggle" onclick="document.querySelector('.mobile-overlay').classList.toggle('active')">
                <p>MENU</p>
            </div>
        </div>
    </div>

    <!-- Mobile overlay menu -->
    <div class="mobile-overlay">
        <div class="close-menu" onclick="document.querySelector('.mobile-overlay').classList.toggle('active')">&times;</div>
        <a href="#works" class="nav-link-wrapper" onclick="document.querySelector('.mobile-overlay').classList.remove('active')">Works</a>
        <a href="#about" class="nav-link-wrapper" onclick="document.querySelector('.mobile-overlay').classList.remove('active')">About</a>
        <a href="#impact" class="nav-link-wrapper" onclick="document.querySelector('.mobile-overlay').classList.remove('active')">Impact</a>
        <a href="#contact" class="nav-link-wrapper" onclick="document.querySelector('.mobile-overlay').classList.remove('active')">Contact</a>
    </div>

    <div class="page_wrap">
        <div class="page_main section u-container" style="padding-top: 5vh; min-height: 50vh; display: flex; align-items: center;">
            <h1 class="p-large" data-hero-blur style="max-width: 1000px; font-weight: 500; font-size: 2rem;">
                GENZ Projects is a cutting-edge architecture firm focused on delivering elegant interior and landscape designs. From stunning homes to smart commercial spaces, we combine creativity and functionality to shape inspiring environments.
            </h1>
        </div>

        <div class="section" id="works">
            <div class="section_title u-container flex-between">
                <div>
                    <h2 class="display">our</h2>
                    <h2 class="display" style="color: var(--primary);">works</h2>
                </div>
            </div>
            
            <div class="u-container" style="margin-top: 5vh;">
                <div class="projects-home-wrapper">
                    <!-- Project Items -->
                    <div class="project-home-item gs-reveal" onclick="location.href='residence.html'">
                        <img src="images/homepage/house1.webp" alt="Residence" class="project-img shadow">
                        <div class="project-inner-wrapper">
                            <div class="tags"><span class="tag">Architecture</span><span class="tag">Residential</span></div>
                            <h3 class="p-main">Residence</h3>
                        </div>
                    </div>
                    
                    <div class="project-home-item gs-reveal" onclick="location.href='restaurant.html'">
                        <img src="images/homepage/restaurant.webp" alt="Restaurant" class="project-img shadow">
                        <div class="project-inner-wrapper">
                            <div class="tags"><span class="tag">Interior</span><span class="tag">Commercial</span></div>
                            <h3 class="p-main">Restaurant</h3>
                        </div>
                    </div>

                    <div class="project-home-item gs-reveal" onclick="location.href='aesthetics.html'">
                        <img src="images/homepage/aesthetics.webp" alt="Aesthetic Office" class="project-img shadow">
                        <div class="project-inner-wrapper">
                            <div class="tags"><span class="tag">Design</span><span class="tag">Commercial</span></div>
                            <h3 class="p-main">Aesthetics Office</h3>
                        </div>
                    </div>

                    <div class="project-home-item gs-reveal" onclick="location.href='cosmetics.html'">
                        <img src="images/homepage/cosmetics.webp" alt="Cosmetics" class="project-img shadow">
                        <div class="project-inner-wrapper">
                            <div class="tags"><span class="tag">Interior</span><span class="tag">Retail</span></div>
                            <h3 class="p-main">Cosmetics Studio</h3>
                        </div>
                    </div>

                    <div class="project-home-item gs-reveal" onclick="location.href='addresshouse.html'">
                        <img src="images/homepage/addresshouse.webp" alt="Address House" class="project-img shadow">
                        <div class="project-inner-wrapper">
                            <div class="tags"><span class="tag">Architecture</span><span class="tag">Residential</span></div>
                            <h3 class="p-main">Address-House</h3>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="section" id="about">
            <div class="u-container">
                <div class="u-grid">
                    <div class="col-5">
                        <h2 class="h2">Expertise</h2>
                        <h3 class="h1" style="margin-top: 1rem;">A sensitive practice focused on collaboration</h3>
                    </div>
                    <div class="col-7" style="display:flex; flex-direction:column; gap: 3rem;">
                        <p class="p-main gs-reveal">
                            GENZ Projects is a cutting-edge architecture firm focused on delivering elegant interior and landscape designs. 
                            From stunning homes to smart commercial spaces, we combine creativity and functionality to shape inspiring environments.
                            <br><br>
                            With a commitment to innovation and excellence, we bring every vision to life.
                        </p>
                    </div>
                </div>
            </div>
        </div>

        <div class="section" id="impact">
            <div class="u-container">
                <div class="impact-stats gs-reveal">
                    <div class="impact-item">
                        <p>Over</p>
                        <div id="family-count">0</div>
                        <p>families transformed</p>
                    </div>
                    <div class="impact-item">
                        <p>More than</p>
                        <div id="commercial-count">0</div>
                        <p>commercial projects</p>
                    </div>
                    <div class="impact-item">
                        <p>Over</p>
                        <div id="landscape-count">0</div>
                        <p>landscapes brought to life</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="section spacer" id="contact" style="margin-bottom: 5vh;">
            <div class="u-container">
                <div class="flex-between center" style="margin-bottom: 2rem;">
                    <p class="h2">Let's work together</p>
                    <a href="https://wa.me/918978163888" target="_blank" rel="noopener noreferrer" class="btn_main_wrap">Contact Us</a>
                </div>
                <div class="flex-between gs-reveal">
                    <h4 class="display">start a</h4>
                    <h4 class="display" style="color: var(--primary);">project?</h4>
                </div>
                <div class="footer-bottom">
                    <div class="footer-contacts">
                        <p class="p-main">Phone: +91 8309641647</p>
                        <p class="p-main">Phone: +91 9000966644</p>
                    </div>
                    <p class="p-main" style="color: rgba(255,255,255,0.5);">© GENZ Projects 2026</p>
                </div>
            </div>
        </div>

    </div>

    <!-- Scripts -->
    <script src="https://cdn.jsdelivr.net/gh/studio-freight/lenis@1.0.23/bundled/lenis.min.js"></script> 
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.2/dist/gsap.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.2/dist/ScrollTrigger.min.js"></script>

    <script>
        // Init Smooth Scroll Lenis
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

        // Hero Init Array
        const heroEl = document.querySelector('[data-hero-blur]');
        if (heroEl) {
            gsap.to(heroEl, {
                opacity: 1, filter: "blur(0px)", duration: 1.5, ease: "power2.out", delay: 0.2
            });
        }

        // Split Projects Wrapper dynamically into 2 columns for a masonry-like scroll
        document.addEventListener('DOMContentLoaded', () => {
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

            // General Element Reveals
            const reveals = gsap.utils.toArray('.gs-reveal');
            reveals.forEach((element) => {
                gsap.fromTo(element, 
                    { opacity: 0, y: 30 },
                    { 
                        opacity: 1, 
                        y: 0, 
                        duration: 1, 
                        ease: 'power2.out',
                        scrollTrigger: { 
                            trigger: element, 
                            start: "top 85%", 
                            toggleActions: "play none none reverse" 
                        }
                    }
                );
            });

            // Interactive Box Shadow
            document.addEventListener('mousemove', function(e) {
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
                    
                    element.style.boxShadow = `${shadowX}px ${shadowY}px ${blurAmount}px rgba(255, 215, 0, 0.15)`;
                });
            });
        });

        // Stats Counting logic
        function animateCountUp(id, target, duration) {
            const element = document.getElementById(id);
            if (!element) return;
            let obj = { val: 0 };
            gsap.to(obj, { 
                val: target, 
                duration: duration, 
                roundProps: "val", 
                onUpdate: function() { element.textContent = obj.val; }, 
                scrollTrigger: { 
                    trigger: "#impact", 
                    start: "top 80%", 
                    once: true 
                } 
            });
        }
        animateCountUp("family-count", 30, 2);
        animateCountUp("commercial-count", 50, 2.5);
        animateCountUp("landscape-count", 15, 3);
    </script>

</body>
</html>
"""

# Let's combine them
final_html = new_head + svg + new_tail

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Updated index.html successfully.")
