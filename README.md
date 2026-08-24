# projetoMDM

Automação em Python (Selenium) para gerenciamento em massa de dispositivos **BlueBird** no console **AirWatch/Workspace ONE UEM**, complementada por um pequeno protótipo web (HTML/CSS/JS) para simular login, listagem e consulta de dispositivos por loja.

> Projeto desenvolvido por **Arthur dos Santos** ([@as.infotech](https://instagram.com/as.infotech) — WhatsApp (51) 99512-4530), originalmente como exercício do curso *Python: Automação III - Selenium* (One Bit Code).

## Índice

- [Sobre o projeto](#sobre-o-projeto)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Como funciona a automação (`main.py`)](#como-funciona-a-automação-mainpy)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Protótipo web (HTML/CSS/JS)](#protótipo-web-htmlcssjs)
- [Geração de páginas de dispositivos](#geração-de-páginas-de-dispositivos)
- [Avisos importantes](#avisos-importantes)
- [Licença](#licença)

## Sobre o projeto

O `projetoMDM` reúne duas frentes:

1. **Automação (`main.py`)**: um robô Selenium que faz login no console AirWatch de uma rede de lojas, localiza dispositivos **BlueBird** (leitores/coletores) a partir de uma planilha, e para cada um deles:
   - inicia o serviço AWCM (AirWatch Cloud Messaging);
   - percorre a aba *Products* do dispositivo e força o **reprocessamento** de cada produto atribuído;
   - dispara a **sincronização** do dispositivo.
2. **Protótipo web**: um mini-sistema estático (login → home → busca de dispositivos por loja) usado para simular/visualizar a consulta de dispositivos, sem back-end real (dados mockados em JavaScript).

## Estrutura do repositório

```
projetoMDM-master/
├── main.py                     # Script de automação Selenium (AirWatch/BlueBirds)
├── dist/
│   └── bluebirds.xlsx          # Planilha com a lista de códigos dos BlueBirds a processar
├── index.html                  # Tela de login do protótipo web
├── home.html                   # Tela inicial após login, com busca e atalhos por modelo
├── consulta_devices.html       # Tela de resultado da busca (dados mockados)
├── script.js                   # Lógica de login, busca e navegação do protótipo
├── style.css                   # Estilos do protótipo web
└── devices/
    ├── cria_paginas.py         # Gera páginas HTML de exemplo para cada modelo/loja
    ├── iphone13.html
    ├── Samsung_Galaxy_S21.html
    ├── Google_Pixel_6.html
    ├── OnePlus_9.html
    └── Xiaomi_Mi_11.html
```

## Como funciona a automação (`main.py`)

1. Lê a lista de códigos de dispositivos BlueBird do arquivo `bluebirds.xlsx`.
2. Verifica uma **data limite** interna (`29/12/2023`) — o script só executa se a data atual for anterior a esse limite; depois disso, exibe uma mensagem de "licença expirada" e encerra.
3. Solicita no terminal:
   - **login** do console AirWatch;
   - **senha** (digitada de forma oculta, via `getpass`);
   - **nome da loja** (ex.: `l002`).
4. Abre o Chrome via Selenium e acessa o console AirWatch (`awconsole.lojasrenner.com.br`).
5. Faz login e filtra a loja informada.
6. Para até 15 BlueBirds da planilha:
   - pesquisa o dispositivo pelo código;
   - clica em **Start AWCM**;
   - abre a aba **Products** e força **Reprocess** em até 8 produtos;
   - executa **Sync Device**;
   - trata alertas de confirmação automaticamente;
   - volta para a listagem e segue para o próximo dispositivo.
7. Erros individuais por dispositivo são capturados (`try/except`) para não interromper o loop inteiro.

## Pré-requisitos

- Python 3.8+
- Google Chrome instalado (compatível com o `webdriver.Chrome()` do Selenium)
- Acesso válido (login/senha) ao console AirWatch/Workspace ONE UEM da rede de lojas
- Arquivo `bluebirds.xlsx` com os códigos dos dispositivos a processar

## Instalação

```bash
git clone <url-do-repositorio>
cd projetoMDM-master

python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

pip install selenium pandas openpyxl
```

> O script usa `webdriver.Chrome()` sem caminho explícito para o driver — garanta que o **ChromeDriver** esteja no `PATH` ou use uma versão recente do Selenium (4.6+), que já gerencia o driver automaticamente.

## Uso

1. Coloque o arquivo `bluebirds.xlsx` (com um código de dispositivo por linha, sem cabeçalho) no mesmo diretório do `main.py`, ou ajuste o caminho em:
   ```python
   bluebirds_df = pd.read_excel("bluebirds.xlsx")
   ```
   (no repositório atual, o arquivo está em `dist/bluebirds.xlsx`).
2. Execute:
   ```bash
   python main.py
   ```
3. Informe login, senha e o nome da loja quando solicitado.
4. Acompanhe o navegador Chrome executando as ações automaticamente.

## Protótipo web (HTML/CSS/JS)

Um mini-fluxo estático, sem back-end, para simular a experiência de consulta de dispositivos:

- `index.html` — formulário de login (credenciais fixas no código: usuário `user`, senha `password`, apenas para demonstração).
- `home.html` — tela pós-login, com campo de busca e links diretos para páginas de modelos (`devices/*.html`).
- `consulta_devices.html` — exibe resultados de busca a partir de **dados mockados** em JavaScript (não consulta nenhuma API real).
- `devices/*.html` — páginas individuais por modelo de dispositivo, com checklist de itens e botão "Enviar".

Para visualizar, basta abrir `index.html` em um navegador (não requer servidor).

## Geração de páginas de dispositivos

O script `devices/cria_paginas.py` gera páginas HTML de exemplo para 5 modelos de celular em 7 lojas fictícias (`loja_001` a `loja_007`), criando os arquivos dentro da pasta `devices/`. Para rodar:

```bash
cd projetoMDM-master
python devices/cria_paginas.py
```

## Avisos importantes

- **Credenciais e URLs sensíveis**: o script contém a URL de um console AirWatch de uma empresa específica e caminhos locais (`script.js`) hardcoded (ex.: `file:///C:/Users/arthur/...`). Ajuste esses valores antes de reutilizar o projeto em outro contexto.
- **Seletores XPath frágeis**: a automação depende fortemente de XPaths absolutos da interface do AirWatch, que podem quebrar caso o layout do console seja atualizado.
- **Data de expiração**: o `main.py` só roda antes de `29/12/2023`; para reutilizar o script, atualize a variável `data_limite`.
- **Protótipo web sem segurança real**: login, dados de dispositivos e lojas são todos mockados/fixos no front-end — não há autenticação ou persistência real.
- Uso pretendido apenas em ambiente autorizado, respeitando as políticas de segurança da organização dona do console MDM.

## Licença

Não há licença explícita neste repositório. Adicione um arquivo `LICENSE` caso deseje formalizar os termos de uso e distribuição.
