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
    alert('Ação de enviar realizada!');
    // Adicione aqui a lógica desejada após o alerta
  }
  