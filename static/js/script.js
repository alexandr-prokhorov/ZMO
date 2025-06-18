document.addEventListener('DOMContentLoaded', function () {
    const container = document.getElementById('plans-container');
    const pagination = document.querySelector('.pagination');
    const loadingIndicator = document.getElementById('loading-indicator');

    // Обработчик кликов по пагинации
    pagination.addEventListener('click', function (e) {
        e.preventDefault();
        const btn = e.target.closest('.paginate-btn');
        if (!btn) return;

        const page = btn.dataset.page;
        loadPlans(page);
    });

    // Обработчик кнопок назад/вперед
    window.addEventListener('popstate', function () {
        const urlParams = new URLSearchParams(window.location.search);
        const page = urlParams.get('plans_page') || 1;
        loadPlans(page);
    });

    function loadPlans(page) {
        // Обновляем URL без перезагрузки
        history.pushState({}, '', `?plans_page=${page}`);

        // Показываем индикатор загрузки
        if (loadingIndicator) loadingIndicator.style.display = 'block';

        const url = new URL(window.location.href);
        url.searchParams.set('plans_page', page);

        fetch(url, {
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
            .then(response => {
                if (!response.ok) throw new Error('Network error');
                return response.json();
            })
            .then(data => {
                if (!data.html || data.html.trim() === '') {
                    container.innerHTML = '<div class="col-12 alert alert-info">Планы отсутствуют</div>';
                } else {
                    container.innerHTML = data.html;
                    updatePagination(data);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                container.innerHTML = '<div class="col-12 alert alert-danger">Ошибка загрузки планов</div>';
            })
            .finally(() => {
                if (loadingIndicator) loadingIndicator.style.display = 'none';
            });
    }

    function updatePagination(data) {
        // Обновляем активное состояние
        document.querySelectorAll('.page-item').forEach(item => {
            item.classList.remove('active');
        });

        const activeBtn = document.querySelector(`.paginate-btn[data-page="${data.current_page}"]`);
        if (activeBtn) {
            activeBtn.parentElement.classList.add('active');
        }

        // Обновляем доступность кнопок
        document.querySelectorAll('.paginate-btn').forEach(btn => {
            const btnPage = parseInt(btn.dataset.page);
            btn.parentElement.style.display = '';

            if (btnPage === data.current_page - 1 && !data.has_previous) {
                btn.parentElement.style.display = 'none';
            }
            if (btnPage === data.current_page + 1 && !data.has_next) {
                btn.parentElement.style.display = 'none';
            }
        });
    }
});



    document.querySelectorAll('.bg-black').forEach(card => {
    card.classList.add('spec-card');
});

     document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    window.scrollTo({
                        top: target.offsetTop - 60,
                        behavior: 'smooth'
                    });
                }
            });
        });