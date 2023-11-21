from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Configurações do Selenium
def run_selenium(login, senha):
    # Inicializar o navegador 
    
    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico)

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
    def alert():
        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            print(f"Alerta detectado: {alert_text}")
            alert.accept()
        except:
            pass
        
    alert()
    # Clicar em "iphone 13"
    time.sleep(1)
    device_1 = driver.find_element(By.XPATH, '/html/body/div/ul/a[1]/li')
    time.sleep(1)
    device_1.click()
    
    try:
        # Clicar em todos os checkboxes
        for i in range(1, 7):
            checkbox = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"/html/body/div/ul/li[{i}]/label/input"))
            )
            checkbox.click()
        
        alert()
    except:
        pass
    
    btn_enviar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'btnEnviar')))
    btn_enviar.click()
    
    
    # Fechar o navegador ao finalizar
    # driver.quit()

# Exemplo de uso da função run_selenium
login = "user"
senha = "password"
run_selenium(login, senha)
print('Encerrado!')
