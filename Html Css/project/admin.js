(function(){
  const ITEMS_KEY = 'luxyItems';
  const form = document.getElementById('adminForm');
  const nameEl = document.getElementById('name');
  const priceEl = document.getElementById('price');
  const imageEl = document.getElementById('image');
  const descEl = document.getElementById('description');
  const catEl = document.getElementById('category');
  const msg = document.getElementById('msg');
  const adminList = document.getElementById('adminList');
  const clearBtn = document.getElementById('clearBtn');
  const submitBtn = form.querySelector('button[type="submit"]');
  let editingId = null;

  function getItems(){
    try{ return JSON.parse(localStorage.getItem(ITEMS_KEY) || '[]'); }
    catch(e){ return []; }
  }

  function saveItems(items){
    localStorage.setItem(ITEMS_KEY, JSON.stringify(items));
    renderList();
  }

  function renderList(){
    const items = getItems();
    adminList.innerHTML = '';
    if(!items.length){ adminList.textContent = 'No admin items yet.'; return; }
    items.forEach(it => {
      const div = document.createElement('div');
      div.className = 'product-row';
      const img = document.createElement('img'); img.src = it.image || 'https://via.placeholder.com/80';
      const info = document.createElement('div');
      info.innerHTML = `<strong>${escapeHtml(it.name)}</strong><br><small>${escapeHtml(it.category)} • ${escapeHtml(String(it.price))}</small><div>${escapeHtml(it.description || '')}</div>`;
      const btns = document.createElement('div');
      btns.style.marginLeft = 'auto';

      const edit = document.createElement('button');
      edit.className = 'btn btn-sm btn-outline-primary me-2';
      edit.textContent = 'Edit';
      edit.addEventListener('click', ()=>{
        editingId = it.id;
        nameEl.value = it.name || '';
        priceEl.value = it.price || '';
        imageEl.value = it.image || '';
        descEl.value = it.description || '';
        catEl.value = it.category || 'woman';
        submitBtn.textContent = 'Save changes';
        showMessage('Editing mode: make changes and click "Save changes"');
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });

      const del = document.createElement('button'); del.className='btn btn-sm btn-outline-danger'; del.textContent='Delete';
      del.addEventListener('click', ()=>{
        if(!confirm('Delete this item?')) return;
        const remain = getItems().filter(x=>x.id!==it.id);
        saveItems(remain);
        showMessage('Item deleted');
      });

      btns.appendChild(edit);
      btns.appendChild(del);
      div.appendChild(img); div.appendChild(info); div.appendChild(btns);
      adminList.appendChild(div);
    });
  }

  function escapeHtml(s){ return String(s).replace(/[&<>"']/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":"&#39;"}[c]; }); }

  form.addEventListener('submit', function(e){
    e.preventDefault();
    const name = nameEl.value.trim();
    const price = priceEl.value.trim();
    const image = imageEl.value.trim();
    const description = descEl.value.trim();
    const category = (catEl.value || '').toLowerCase();

    if(!name || !price){ showMessage('Please provide name and price', true); return; }

    if(editingId){
      // update existing
      const items = getItems().map(it => {
        if(it.id === editingId){
          return { ...it, name, price, image, description, category };
        }
        return it;
      });
      saveItems(items);
      editingId = null;
      submitBtn.textContent = 'Add product';
      form.reset();
      showMessage('Product updated');
      return;
    }

    const item = { id: 'a_' + Date.now(), name, price, image, description, category };
    const items = getItems();
    items.unshift(item);
    saveItems(items);
    form.reset();
    showMessage('Product added');
  });

  form.addEventListener('reset', ()=>{
    editingId = null;
    if(submitBtn) submitBtn.textContent = 'Add product';
  });

  clearBtn.addEventListener('click', function(){
    if(!confirm('Clear all admin products?')) return;
    localStorage.removeItem(ITEMS_KEY);
    renderList();
    showMessage('Cleared');
  });

  function showMessage(text, isError){
    msg.style.display = 'block';
    msg.textContent = text;
    msg.style.background = isError ? '#f8d7da' : '#d4edda';
    msg.style.color = isError ? '#721c24' : '#155724';
    setTimeout(()=>{ msg.style.display='none'; }, 3000);
  }

  // initial
  renderList();
})();
