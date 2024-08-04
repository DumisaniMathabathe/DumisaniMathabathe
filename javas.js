function showPage(page) {
    var sections = document.querySelectorAll('.content section');
    sections.forEach(function(section) {
        section.classList.remove('active');
    });
    document.getElementById(page).classList.add('active');
}

// Show home page by default
document.addEventListener('DOMContentLoaded', function() {
    showPage('home');
});
