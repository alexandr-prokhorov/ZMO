document.addEventListener('DOMContentLoaded', function() {
    const gallery = document.getElementById('plans-gallery');
    if (!gallery) return;

    const plans = JSON.parse(gallery.dataset.plans);
    if (plans.length <= 1) return;

    const currentPlanEl = document.getElementById('current-plan');
    const currentIndexEl = document.getElementById('current-plan-index');
    const prevBtn = document.getElementById('prev-plan');
    const nextBtn = document.getElementById('next-plan');

    let currentIndex = 0;

    function showPlan(index) {
        if (!currentPlanEl) return;
        currentPlanEl.src = plans[index].image;
        if (currentIndexEl) {
            currentIndexEl.textContent = index + 1;
        }
        currentIndex = index;
    }

    if (prevBtn) {
        prevBtn.addEventListener('click', function() {
            const newIndex = (currentIndex - 1 + plans.length) % plans.length;
            showPlan(newIndex);
        });
    }

    if (nextBtn) {
        nextBtn.addEventListener('click', function() {
            const newIndex = (currentIndex + 1) % plans.length;
            showPlan(newIndex);
        });
    }
});