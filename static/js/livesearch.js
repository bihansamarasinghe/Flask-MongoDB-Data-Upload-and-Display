    const searchInput = document.getElementById('search-input');
    const rows = document.querySelectorAll('table tr');

    searchInput.addEventListener('input', function(event) {
    const searchQuery = event.target.value.toLowerCase();

        rows.forEach(function(row, index) {
            if (index === 0) return; // Skip header row

            const cells = row.querySelectorAll('td');
            let containsQuery = false;

    cells.forEach(function(cell) {
        const cellText = cell.textContent.toLowerCase();

        if (cellText.includes(searchQuery)) {
            containsQuery = true;
        }
    });

    if (containsQuery) {
        row.style.display = '';
    } else {
        row.style.display = 'none';
    }
    });
});