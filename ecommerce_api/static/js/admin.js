const apiUrl = 'http://localhost:8000/api/products/'; // Update with your backend API URL

// Create Product
document.getElementById('create-product-form').addEventListener('submit', function (event) {
    event.preventDefault();
    
    const productData = {
        name: document.getElementById('name').value,
        description: document.getElementById('description').value,
        price: document.getElementById('price').value,
        category: document.getElementById('category').value,
        stock_quantity: document.getElementById('stock').value,
        image_url: document.getElementById('image').value
    };
    
    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('auth_token')}` // Assuming token-based authentication
        },
        body: JSON.stringify(productData)
    })
    .then(response => response.json())
    .then(data => {
        alert('Product created successfully');
        loadProducts(); // Reload product list
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

// Load Product List
function loadProducts() {
    fetch(apiUrl)
        .then(response => response.json())
        .then(products => {
            const productList = document.getElementById('product-list');
            productList.innerHTML = ''; // Clear the list before adding new items
            products.forEach(product => {
                const li = document.createElement('li');
                li.innerHTML = `
                    <strong>${product.name}</strong><br>
                    <span>Price: $${product.price}</span><br>
                    <span>Category: ${product.category}</span><br>
                    <span>Stock: ${product.stock_quantity}</span><br>
                    <span>Description: ${product.description}</span><br>
                    <img src="${product.image_url}" alt="${product.name}" width="100">
                    <button onclick="deleteProduct(${product.id})">Delete</button>
                    <button onclick="editProduct(${product.id})">Edit</button>
                `;
                productList.appendChild(li);
            });
        });
}

// Delete Product
function deleteProduct(productId) {
    fetch(`${apiUrl}${productId}/`, {
        method: 'DELETE',
        headers: {
            'Authorization': `Bearer ${localStorage.getItem('auth_token')}`
        }
    })
    .then(response => {
        if (response.ok) {
            alert('Product deleted');
            loadProducts(); // Reload product list
        } else {
            alert('Error deleting product');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Edit Product (Example implementation, you may need to extend this)
function editProduct(productId) {
    const productData = {
        name: prompt('Enter new name:'),
        price: prompt('Enter new price:')
    };
    
    fetch(`${apiUrl}${productId}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('auth_token')}`
        },
        body: JSON.stringify(productData)
    })
    .then(response => response.json())
    .then(data => {
        alert('Product updated');
        loadProducts(); // Reload product list
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Initial load of products
loadProducts();