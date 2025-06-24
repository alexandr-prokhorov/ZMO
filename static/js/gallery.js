document.addEventListener('DOMContentLoaded', function() {
    const gallery = document.querySelector('.gallery-container');
    const images = JSON.parse(gallery.getAttribute('data-images'));
    const descriptions = JSON.parse(gallery.getAttribute('data-descriptions'));

    const currentImage = document.getElementById('current-image');
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');
    const imageDescription = document.getElementById('image-description');

    let currentIndex = 0;

    function updateImage() {
        currentImage.style.opacity = 0;
        setTimeout(() => {
            currentImage.src = images[currentIndex];
            currentImage.alt = descriptions[currentIndex];
            document.getElementById('current-index').textContent = currentIndex + 1;
            imageDescription.textContent = descriptions[currentIndex];
            currentImage.style.opacity = 1;
        }, 200);
    }

    function nextImage() {
        currentIndex = (currentIndex + 1) % images.length;
        updateImage();
    }

    function prevImage() {
        currentIndex = (currentIndex - 1 + images.length) % images.length;
        updateImage();
    }

    // Обработчики событий
    nextBtn.addEventListener('click', nextImage);
    prevBtn.addEventListener('click', prevImage);

    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight') nextImage();
        if (e.key === 'ArrowLeft') prevImage();
    });

    currentImage.addEventListener('click', nextImage);
    document.getElementById('total-images').textContent = images.length;
    updateImage();
});