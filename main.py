from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configurações do Selenium
def run_selenium(login, senha):
    # Inicializar o navegador (neste exemplo, usaremos o Firefox)
    driver = webdriver.Firefox()

    # Abrir o site desejado
    driver.get('http://127.0.0.1:5500/index.html')

    # Fazer login
    time.sleep(1)

    # Preencher o campo de login
    input_login = driver.find_element(By.XPATH, '//*[@id="username"]')
    input_login.send_keys(login)
    time.sleep(1)

    # Preencher o campo de senha
    input_senha = driver.find_element(By.XPATH, '//*[@id="password"]')
    input_senha.send_keys(senha)
    time.sleep(1)

    # Clicar no botão de login
    btn_login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/button')
    btn_login.click()
    time.sleep(1)

    # Verificar se há um alerta e aceitar
    try:
        alert = driver.switch_to.alert
        alert_text = alert.text
        print(f"Alerta detectado: {alert_text}")
        alert.accept()
    except:
        pass

    # Clicar em "iphone 13"
    time.sleep(1)
    device_1 = driver.find_element(By.XPATH, '/html/body/div/ul/a[1]/li')
    time.sleep(1)
    device_1.click()

    itens_click = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
    time.sleep(2)
    # Clicar em todos os checkboxes
    for indice, item in enumerate(itens_click, start=1):  # Começando do índice 1
        try:
            checkbox = driver.find_element(By.XPATH, f"//li[contains(text(), '{item}')]/label/input")
            checkbox.click()
            print(f"Clicou no checkbox para '{item}' no índice {indice}.")
            time.sleep(1)  # Adicionar um pequeno atraso opcional entre cliques
        except:
            print(f"Item {item} não encontrado.")

    # Fechar o navegador ao finalizar
    # driver.quit()

# Exemplo de uso da função run_selenium
login = "user"
senha = "password"
run_selenium(login, senha)
print('Encerrado!')
