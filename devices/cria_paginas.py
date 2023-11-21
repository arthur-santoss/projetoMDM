# Função para criar uma página HTML para cada dispositivo
def criar_pagina_html(loja_numero, celular_info):
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="../style.css">
  <title>{celular_info['nome']}</title>
</head>
<body>
  <div class="container">
    <h2>{celular_info['nome']}</h2>
    <p>This is the page for {celular_info['nome']}. Add your content here.</p>

    <button onclick="mostrarAlerta()">Enviar</button>

    <h3>Itens:</h3>
    <ul>
      <li>
        <label><input type="checkbox" name="item1"> Item 1</label>
      </li>
      <li>
        <label><input type="checkbox" name="item2"> Item 2</label>
      </li>
      <li>
        <label><input type="checkbox" name="item3"> Item 3</label>
      </li>
      <li>
        <label><input type="checkbox" name="item4"> Item 4</label>
      </li>
    </ul>

    <a href="../home.html">Back to Home</a>
  </div>

  <script src="../script.js"></script>
</body>
</html>
"""
    nome_arquivo = f"devices/{celular_info['modelo'].replace(' ', '_')}.html"
    
    # Escrever o conteúdo no arquivo
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(html_content)

# Lista de modelos de dispositivos
modelos_dispositivos = [
    "iPhone 13",
    "Samsung Galaxy S21",
    "Google Pixel 6",
    "OnePlus 9",
    "Xiaomi Mi 11",
]

# Criar dados de exemplo para 7 lojas e 5 celulares em cada loja
lojas = {}

for i in range(1, 8):
    loja_numero = f"loja_{i:03d}"
    celulares_loja = {}

    for j, modelo_dispositivo in enumerate(modelos_dispositivos, start=1):
        modelo = f"{modelo_dispositivo.replace(' ', '_')}_{loja_numero}_{j:02d}"
        celulares_loja[modelo] = {
            "nome": f"{modelo_dispositivo} Loja {i} Celular {j}",
            "preco": 1000 + j * 100,
            "estoque": 10,
            "modelo": modelo,
        }

        # Criar a página HTML para cada dispositivo
        criar_pagina_html(loja_numero, celulares_loja[modelo])

    lojas[loja_numero] = celulares_loja
