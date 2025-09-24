// Basic Dakota AI Website Interactions
// Simple functionality without complex animations

document.addEventListener('DOMContentLoaded', function() {
    // Initialize basic components
    initMobileMenu();
    initThemeToggle();

    console.log('🚀 Dakota AI website loaded successfully!');
});

// Mobile menu functionality
function initMobileMenu() {
    const mobileToggle = document.querySelector('.mobile-menu-toggle');
    const nav = document.querySelector('nav ul');

    if (!mobileToggle || !nav) return;

    mobileToggle.addEventListener('click', function() {
        nav.classList.toggle('mobile-open');
        this.classList.toggle('active');
    });

    // Close mobile menu when clicking outside
    document.addEventListener('click', function(e) {
        if (!nav.contains(e.target) && !mobileToggle.contains(e.target)) {
            nav.classList.remove('mobile-open');
            mobileToggle.classList.remove('active');
        }
    });
}

// Basic theme toggle functionality
function initThemeToggle() {
    const themeToggle = document.getElementById('themeToggle');
    if (!themeToggle) return;

    const currentTheme = localStorage.getItem('theme') || 'light';
    setTheme(currentTheme);

    themeToggle.addEventListener('click', () => {
        const newTheme = document.body.hasAttribute('data-theme') ? 'light' : 'dark';
        setTheme(newTheme);
    });

    function setTheme(theme) {
        if (theme === 'dark') {
            document.body.setAttribute('data-theme', 'dark');
            document.body.style.backgroundColor = '#1a1a2e';
            document.body.style.color = '#f1f5f9';

            // Update theme toggle icon
            const svg = themeToggle.querySelector('svg');
            svg.innerHTML = `<path d="M12 3v2.25m6.364.386l-1.591 1.591M21 12h-2.25m-.386 6.364l-1.591-1.591M12 18.75V21m-4.773-4.227l-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0z"/>`;
            themeToggle.style.background = 'rgba(30, 41, 59, 0.9)';
        } else {
            document.body.removeAttribute('data-theme');
            document.body.style.backgroundColor = '';
            document.body.style.color = '';

            // Update theme toggle icon
            const svg = themeToggle.querySelector('svg');
            svg.innerHTML = `<path d="M12 2.25a.75.75 0 01.75.75v2.25a.75.75 0 01-1.5 0V3a.75.75 0 01.75-.75zM7.5 12a4.5 4.5 0 119 0 4.5 4.5 0 01-9 0zM18.894 6.166a.75.75 0 00-1.06-1.06l-1.591 1.59a.75.75 0 101.06 1.061l1.591-1.59zM21.75 12a.75.75 0 01-.75.75h-2.25a.75.75 0 010-1.5H21a.75.75 0 01.75.75zM17.834 18.894a.75.75 0 001.06-1.06l-1.59-1.591a.75.75 0 10-1.061 1.06l1.59 1.591zM12 18a.75.75 0 01.75.75V21a.75.75 0 01-1.5 0v-2.25A.75.75 0 0112 18zM7.758 17.303a.75.75 0 00-1.061-1.06l-1.591 1.59a.75.75 0 001.06 1.061l1.591-1.59zM6 12a.75.75 0 01-.75.75H3a.75.75 0 010-1.5h2.25A.75.75 0 016 12zM6.697 7.757a.75.75 0 001.06-1.06l-1.59-1.591a.75.75 0 00-1.061 1.06l1.59 1.591z"/>`;
            themeToggle.style.background = 'rgba(0,0,0,0.8)';
        }
        localStorage.setItem('theme', theme);
    }
}
