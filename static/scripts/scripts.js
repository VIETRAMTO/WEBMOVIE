document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelectorAll('.banner-slide');
    if (slides.length === 0) return; // Thoát nếu không có slide

    let currentSlide = 0;

    function showSlide(index) {
        slides.forEach((slide, i) => {
            slide.classList.toggle('active', i === index);
        });
    }

    function nextSlide() {
        currentSlide = (currentSlide + 1) % slides.length;
        showSlide(currentSlide);
    }

    showSlide(currentSlide); // Hiển thị slide đầu tiên
    setInterval(nextSlide, 3000); // Chuyển slide mỗi 3 giây
});