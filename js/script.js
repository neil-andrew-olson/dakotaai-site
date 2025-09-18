// Simple form submission placeholder
document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contact-form');

    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();

            // Get form data
            const formData = new FormData(this);
            const name = formData.get('name');
            const email = formData.get('email');
            const message = formData.get('message');

            // Placeholder for form submission - in a real app, this would send to a server
            alert(`Thank you for your message, ${name}! We'll get back to you at ${email} soon.`);

            // Reset form
            this.reset();
        });
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
