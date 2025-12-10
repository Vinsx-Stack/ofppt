(function(){
  const PASSWORD = 'anas123'; // client-side demo password
  const form = document.getElementById('loginForm');
  const passEl = document.getElementById('password');
  const msg = document.getElementById('loginMsg');

  function showMessage(text, isError){
    msg.textContent = text;
    msg.style.color = isError ? '#721c24' : '#155724';
    msg.style.background = isError ? '#f8d7da' : '#d4edda';
    msg.style.padding = '0.5rem';
    msg.style.borderRadius = '4px';
  }

  form.addEventListener('submit', function(e){
    e.preventDefault();
    const v = (passEl.value || '').trim();
    if(v === PASSWORD){
      // mark session as authed and redirect to panel
      try{ sessionStorage.setItem('luxyAdminAuth','true'); } catch(e){}
      window.location.href = 'admin.html';
    } else {
      showMessage('Incorrect password', true);
      passEl.value = '';
      passEl.focus();
    }
  });
})();
