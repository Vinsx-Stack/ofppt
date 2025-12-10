/* products.js — renders items saved via admin.html into pages
   Usage: include <script src="products.js"></script> on pages and set <body data-category="man|woman|home"> */

(function() {
  const ITEMS_KEY = 'luxyItems';

  function getItems() {
    try {
      return JSON.parse(localStorage.getItem(ITEMS_KEY) || '[]');
    } catch (e) {
      return [];
    }
  }

  function formatPrice(p) {
    if (typeof p === 'number') return '$' + p.toFixed(2);
    const parsed = parseFloat(String(p).replace(/[^0-9.]/g, ''));
    return isNaN(parsed) ? '$0.00' : '$' + parsed.toFixed(2);
  }

  function createCard(item) {
    const col = document.createElement('div');
    col.className = 'col-lg-3 col-md-6 mb-4';

    const card = document.createElement('div');
    card.className = 'product-card';

    const img = document.createElement('img');
    img.className = 'product-img';
    img.src = item.image || '';
    img.alt = item.name || 'Product';

    const body = document.createElement('div');
    body.className = 'product-body';

    const h5 = document.createElement('h5');
    h5.className = 'product-title';
    h5.textContent = item.name || 'Product';

    const price = document.createElement('p');
    price.className = 'product-price';
    price.textContent = formatPrice(item.price);

    const desc = document.createElement('p');
    desc.className = 'product-description';
    desc.textContent = item.description || '';

    const a = document.createElement('a');
    a.href = 'javascript:void(0)';
    a.className = 'btn-add-cart';
    a.textContent = 'Add to Cart';

    body.appendChild(h5);
    body.appendChild(price);
    body.appendChild(desc);
    body.appendChild(a);

    card.appendChild(img);
    card.appendChild(body);

    col.appendChild(card);
    return col;
  }

  function renderCategory(category) {
    const container = document.getElementById('dynamic-products');
    if (!container) return;

    const items = getItems().filter(i => (i.category || '').toLowerCase() === (category || '').toLowerCase());
    if (!items.length) {
      // don't show anything if no admin items for this category
      return;
    }

    const row = document.createElement('div');
    row.className = 'row';

    items.forEach(item => {
      row.appendChild(createCard(item));
    });

    // Insert at top of container
    container.innerHTML = '';
    container.appendChild(row);
  }

  // Auto-run on load
  document.addEventListener('DOMContentLoaded', function() {
    const category = (document.body && document.body.dataset && document.body.dataset.category) || 'home';
    renderCategory(category);
  });

  // expose for console debugging
  window.luxyProducts = { getItems };
})();
