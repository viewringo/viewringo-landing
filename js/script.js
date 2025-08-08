document.addEventListener('DOMContentLoaded', function() {
    // Language switcher logic
    var languageDropdownItems = document.querySelectorAll('.dropdown-item[data-lang]');

    languageDropdownItems.forEach(function(item) {
        item.addEventListener('click', function(event) {
            event.preventDefault();
            var selectedLang = this.getAttribute('data-lang');
            var newUrl;
            if (selectedLang === 'en') {
                newUrl = 'index.html';
            } else {
                newUrl = 'index_' + selectedLang + '.html';
            }
            window.location.href = newUrl;
        });
    });

    // Image slider logic for hero section
    const slider = document.querySelector('.sliding-background-container');
    const images = document.querySelectorAll('.sliding-background-image');
    const imageCount = images.length; // Total number of images including the duplicate
    const uniqueImageCount = imageCount - 1; // Number of unique images
    let currentIndex = 0; // Current index of the image being displayed (0 to uniqueImageCount - 1)
    const biToolLabel = document.getElementById('current-bi-tool-label');

    // Helper function to update the label based on a given index
    function updateLabelForIndex(index) {
        const toolName = images[index].getAttribute('data-tool-name');
        if (biToolLabel) {
            biToolLabel.textContent = toolName;
        }
    }

    function updateSlider() {
        // Calculate the next index to show
        let nextIndex = currentIndex + 1;

        // If we are about to show the duplicated first image (at uniqueImageCount index)
        if (nextIndex === imageCount) {
            // Smoothly slide to the duplicated first image
            slider.style.transition = 'transform 1s ease-in-out';
            slider.style.transform = `translateX(-${(uniqueImageCount) * (100 / imageCount)}%)`;
            updateLabelForIndex(uniqueImageCount); // Update label for the duplicate PowerBI

            // After the transition to the duplicate, instantly snap back to the real first image
            setTimeout(() => {
                slider.style.transition = 'none'; // Disable transition for instant snap
                currentIndex = 0; // Reset index to the first image
                slider.style.transform = `translateX(-${currentIndex * (100 / imageCount)}%)`; // Snap back to the first image (0%)
                updateLabelForIndex(currentIndex); // Update label for the real first image
            }, 1000); // This timeout should match the CSS transition duration
        } else {
            // Normal slide to the next image
            slider.style.transition = 'transform 1s ease-in-out';
            slider.style.transform = `translateX(-${nextIndex * (100 / imageCount)}%)`;
            currentIndex = nextIndex; // Update current index
            updateLabelForIndex(currentIndex); // Update label for normal slide
        }
    }

    // Initial update of the label and slider position
    updateLabelForIndex(currentIndex);
    slider.style.transform = `translateX(-${currentIndex * (100 / imageCount)}%)`;

    // Start the slider
    setInterval(updateSlider, 3000); // Change image every 3 seconds

    // EmailJS integration for contact form
    (function() {
        // IMPORTANT: Replace 'YOUR_PUBLIC_KEY' with your actual Public Key from your EmailJS account.
        emailjs.init('o9OuOowb-wue0AEy-');
    })();

    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(event) {
            event.preventDefault();

            const submitButton = this.querySelector('button[type="submit"]');
            const originalButtonHTML = submitButton.innerHTML;
            
            // Disable button and show spinner
            submitButton.disabled = true;
            submitButton.innerHTML = `<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Sending...`;

            // IMPORTANT: Replace 'YOUR_SERVICE_ID' and 'YOUR_TEMPLATE_ID' with your actual IDs from EmailJS.
            // The form input 'name' attributes (name, email, message) must match the variables in your EmailJS template.
            const serviceID = 'service_gmqugw6';
            const templateID = 'template_7y2k35p';

            emailjs.sendForm(serviceID, templateID, this)
                .then(() => {
                    alert('Your message has been sent successfully!');
                    contactForm.reset(); // Clear the form
                }, (err) => {
                    alert('Failed to send the message. Please try again later. Error: ' + JSON.stringify(err));
                })
                .finally(() => {
                    // Re-enable button and restore original text
                    submitButton.disabled = false;
                    submitButton.innerHTML = originalButtonHTML;
                });
        });
    }
});