document.addEventListener('DOMContentLoaded', () => {
    console.log('Scripts loaded');

    // Xử lý tìm kiếm
    const searchForm = document.querySelector('.search-box form');
    if (searchForm) {
        searchForm.addEventListener('submit', (e) => {
            const query = document.querySelector('#searchInput').value.trim();
            if (!query) {
                e.preventDefault();
                alert('Vui lòng nhập từ khóa tìm kiếm!');
            }
        });
    } else {
        console.warn('Search form not found');
    }

    // Xử lý dropdown thể loại
    const dropdownToggle = document.querySelector('.dropdown-toggle');
    const dropdownMenu = document.querySelector('.dropdown-menu');
    let hideTimeout;

    if (dropdownToggle && dropdownMenu) {
        console.log('Dropdown elements found:', {
            toggle: dropdownToggle,
            menu: dropdownMenu
        });

        // Bật/tắt dropdown khi nhấp vào "Thể loại"
        dropdownToggle.addEventListener('click', (e) => {
            e.preventDefault();
            dropdownMenu.classList.toggle('active');
            console.log('Dropdown toggled:', {
                isActive: dropdownMenu.classList.contains('active'),
                display: window.getComputedStyle(dropdownMenu).display
            });

            // Xử lý ẩn tự động sau 5 giây
            if (dropdownMenu.classList.contains('active')) {
                clearTimeout(hideTimeout);
                hideTimeout = setTimeout(() => {
                    dropdownMenu.classList.remove('active');
                    console.log('Dropdown auto-hidden after 5 seconds');
                }, 5000);
            } else {
                clearTimeout(hideTimeout);
            }
        });

        // Ẩn dropdown khi nhấp ra ngoài
        document.addEventListener('click', (e) => {
            if (!dropdownToggle.contains(e.target) && !dropdownMenu.contains(e.target)) {
                dropdownMenu.classList.remove('active');
                clearTimeout(hideTimeout);
                console.log('Dropdown hidden (clicked outside)');
            }
        });

        // Ẩn dropdown khi nhấp vào một thể loại
        const genreLinks = dropdownMenu.querySelectorAll('a');
        console.log('Genre links found:', genreLinks.length);
        if (genreLinks.length > 0) {
            genreLinks.forEach((link, index) => {
                link.addEventListener('click', () => {
                    dropdownMenu.classList.remove('active');
                    clearTimeout(hideTimeout);
                    console.log(`Genre link ${index + 1} clicked, dropdown hidden`);
                });
            });
        } else {
            console.warn('No genre links found in dropdown menu');
        }

        // Giữ dropdown mở khi di chuột
        dropdownMenu.addEventListener('mouseenter', () => {
            clearTimeout(hideTimeout);
            console.log('Mouse entered dropdown, auto-hide paused');
        });

        dropdownMenu.addEventListener('mouseleave', () => {
            if (dropdownMenu.classList.contains('active')) {
                hideTimeout = setTimeout(() => {
                    dropdownMenu.classList.remove('active');
                    console.log('Dropdown auto-hidden after leaving');
                }, 5000);
            }
        });
    } else {
        console.error('Dropdown elements not found:', {
            toggle: !!dropdownToggle,
            menu: !!dropdownMenu
        });
    }
});