document.getElementById('search-button').addEventListener('click', function() {
    const searchQuery = document.getElementById('search').value;
    const priceMin = document.getElementById('price-min').value;
    const priceMax = document.getElementById('price-max').value;
    const category = document.getElementById('category').value;
    
    const queryParams = new URLSearchParams();
    if (searchQuery) queryParams.append('search', searchQuery);
    if (priceMin) queryParams.append('price_min', priceMin);
    if (priceMax) queryParams.append('price_max', priceMax);
    if (category) queryParams.append('category', category);
    
    const apiUrl = `http://localhost:8000/api/products/search/?${queryParams.toString()}`;
    
    fetch(apiUrl)
        .then(response => response.json())
        .then(products => {
            const resultsList = document.getElementById('search-results');
            resultsList.innerHTML = ''; // Clear previous results
            products.forEach(product => {
                const li = document.createElement('li');
                li.innerHTML = `
                    <strong>${product.name}</strong><br>
                    Price: $${product.price}<br>
                    Category: ${product.category}<br>
                    <img src="${product.image_url}" alt="${product.name}" width="100">
                `;
                resultsList.appendChild(li);
            });
        });
});