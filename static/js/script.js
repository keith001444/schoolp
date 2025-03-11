// Toggle sidebar
document.getElementById('menu-toggle').addEventListener('click', function() {
    const sidebar = document.getElementById('sidebar');
    const content = document.getElementById('content');
    const menuName = document.getElementById('menu-name');
    const dashboardHeader = document.getElementById('dashboard-header');

    sidebar.classList.toggle('show'); // Toggle the 'show' class to slide the sidebar in/out
    content.classList.toggle('sidebar-visible'); // Adjust content when sidebar is visible

    // Hide the menu name when sidebar appears, show it when sidebar is hidden
    if (sidebar.classList.contains('show')) {
        menuName.style.display = 'none'; // Hide Menu name
        dashboardHeader.style.marginLeft = '-55px'; // Connect the sidebar and header
        dashboardHeader.style.width = '105.5%';
    } else {
        menuName.style.display = 'inline'; // Show Menu name
        dashboardHeader.style.marginLeft = '0'; // Reset header margin when sidebar is hidden
    }
});

// Hide sidebar with arrow button
document.getElementById('hide-sidebar').addEventListener('click', function() {
    const sidebar = document.getElementById('sidebar');
    const content = document.getElementById('content');
    const menuName = document.getElementById('menu-name');
    const dashboardHeader = document.getElementById('dashboard-header');

    sidebar.classList.remove('show'); // Hide sidebar
    content.classList.remove('sidebar-visible'); // Reset content margin
    menuName.style.display = 'inline'; // Show Menu name
    dashboardHeader.style.marginLeft = '0'; // Reset header margin when sidebar is hidden
});
