// Remove any Cloudflare or analytics scripts if present
// This file contains only essential client-side interactions

(function() {
    // Block Cloudflare scripts from loading
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            mutation.addedNodes.forEach(function(node) {
                if (node.tagName === 'SCRIPT' &&
                    node.src &&
                    node.src.includes('cloudflareinsights.com')) {
                    node.parentNode.removeChild(node);
                    console.log('Cloudflare script blocked');
                }
            });
        });
    });

    // Start observing
    observer.observe(document.documentElement, {
        childList: true,
        subtree: true
    });

    // Also block existing Cloudflare scripts
    document.querySelectorAll('script[src*="cloudflareinsights.com"]').forEach(function(script) {
        script.parentNode.removeChild(script);
        console.log('Existing Cloudflare script removed');
    });
})();

document.addEventListener('DOMContentLoaded', function() {
    // Formspree handles form submission, no need for custom handling
    // But we can add success feedback if needed
    const contactForm = document.getElementById('contact-form');

    if (contactForm) {
        // Optional: Add custom success handling
        // Note: With Formspree, form will submit and redirect to success page
    }

    // Simple hover effects for service cards
    const serviceCards = document.querySelectorAll('.service-card');
    serviceCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
        });

        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });

    // Simple animation for hero visual (placeholder for AI-themed visual)
    const heroVisual = document.getElementById('hero-visual');
    if (heroVisual) {
        heroVisual.addEventListener('mouseenter', function() {
            this.style.background = 'rgba(255, 255, 255, 0.2)';
            this.innerHTML = '<svg width="50" height="50" viewBox="0 0 50 50"><circle cx="25" cy="25" r="15" fill="rgba(255,255,255,0.5)"><animateTransform attributeName="transform" attributeType="XML" type="scale" values="1;1.2;1" dur="1s" repeatCount="indefinite"/></circle></svg>';
        });

        heroVisual.addEventListener('mouseleave', function() {
            this.style.background = 'rgba(255, 255, 255, 0.1)';
            this.innerHTML = '';
        });
    }
});
