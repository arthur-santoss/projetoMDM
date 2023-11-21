function login() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
  
    // Adicione lógica de autenticação aqui
    // Este é apenas um exemplo básico
    if (username === 'user' && password === 'password') {
      alert('Login bem-sucedido!');
      window.location.href = 'home.html';
    } else {
      alert('Login falhou. Verifique seu nome de usuário e senha.');
    }
  }

  function searchDevices() {
    // Obter o valor do campo de pesquisa
    var searchTerm = document.getElementById("search").value.toLowerCase();
    
    // Redirecionar para a página de consulta com o termo de pesquisa como parâmetro
    window.location.href = `consulta_devices.html?search=${encodeURIComponent(searchTerm)}`;
  }

  function mostrarAlerta() {
    window.location.href = 'file:///C:/Users/arthur/Desktop/ONE%20BIT%20CODE/Python-Automacao_III-Selenium/projetoMDM/home.html';
    alert('Ação de enviar realizada!');
  }
  