document.addEventListener('DOMContentLoaded', function() {
    // Xử lý hover cho movie card
    const movieCards = document.querySelectorAll('.movie-card');

    movieCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px)';
            this.style.boxShadow = '0 15px 30px rgba(0,0,0,0.2)';
        });

        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(-5px)';
            this.style.boxShadow = '0 10px 20px rgba(0,0,0,0.2)';
        });

        // Click vào card để xem chi tiết
        card.addEventListener('click', function() {
            const movieId = this.dataset.id;
            window.location.href = `/movie/${movieId}`;
        });
    });

    // Xử lý tìm kiếm
    const searchBox = document.querySelector('.search-box input');
    const searchButton = document.querySelector('.search-box button');

    searchButton.addEventListener('click', performSearch);
    searchBox.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') performSearch();
    });

    function performSearch() {
        const query = searchBox.value.trim();
        if (query.length > 2) {
            // Gọi API tìm kiếm hoặc filter client-side
            console.log('Searching for:', query);
        }
    }
});