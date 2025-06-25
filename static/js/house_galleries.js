document.addEventListener('DOMContentLoaded', function() {
    const imagesGallery = document.getElementById('images-gallery');
    if (!imagesGallery) return;

    const elements = {
        image: document.getElementById('current-image'),
        prevBtn: document.getElementById('prev-image'),
        nextBtn: document.getElementById('next-image'),
        currentIndex: document.getElementById('current-image-index'),
        totalImages: document.getElementById('total-images')
    };

    if (Object.values(elements).some(el => !el)) {
        console.error('Не найдены элементы галереи');
        return;
    }

    const imagesData = JSON.parse(imagesGallery.getAttribute('data-images') || '[]');
    const loadedImages = {}; // Кэш загруженных изображений

    if (imagesData.length <= 1) {
        elements.prevBtn.style.display = 'none';
        elements.nextBtn.style.display = 'none';
        return;
    }

    elements.totalImages.textContent = imagesData.length;
    let currentIndex = 0;

    // Предзагрузка всех изображений
    imagesData.forEach((item, index) => {
        loadedImages[index] = new Image();
        loadedImages[index].src = item.image;
    });

    function updateImage() {
        if (loadedImages[currentIndex].complete) {
            elements.image.src = loadedImages[currentIndex].src;
        } else {
            loadedImages[currentIndex].onload = function() {
                elements.image.src = this.src;
            };
        }
        elements.currentIndex.textContent = currentIndex + 1;
    }

    elements.prevBtn.addEventListener('click', () => {
        currentIndex = (currentIndex - 1 + imagesData.length) % imagesData.length;
        updateImage();
    });

    elements.nextBtn.addEventListener('click', () => {
        currentIndex = (currentIndex + 1) % imagesData.length;
        updateImage();
    });

    updateImage();
});