from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# import PhantomJS

os.system('cls')
print("""
Feito por Arthur dos Santos - CSC TI
""")

# Configurações do Selenium
# Inicializar o navegador 

# Exemplo de uso da função run_selenium
login = open('C:\login\login.txt', 'r').read()
senha = open('C:\login\senha.txt', 'r').read()

# elemento base de consulta: 'data-name' em:
# nome_empresa
# nome_loja

nome_loja = 'l527' #input('Nome da loja, exemplo: l001:\n')
num_bluebird = 'G865' #input('Nome do Bluebird:\n')

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


# padrão para pesquisa l002 e G504

#abrir navegador
driver = webdriver.Firefox()

# executar via terminal
# driver = webdriver.PhantomJS()

# Abrir o site desejado
driver.get('https://awconsole.lojasrenner.com.br/AirWatch/Login?ReturnUrl=%2FAirWatch%2F#/Device/List')

# Fazer login
print('fazendo login...')
input_login = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="UserName"]')))
input_login.send_keys(login)
input_login.send_keys(Keys.RETURN)

input_senha = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Password"]')))
input_senha.send_keys(senha)
input_senha.send_keys(Keys.RETURN)

# pesquisando loja
print('Pesquisando loja...')
label_location = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/header[1]/div[2]/div/div/a')))
time.sleep(3)
label_location.click()

# digita no search
label_location_search = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/header[1]/div[2]/div/div/div/div[1]/div[1]/input')))
label_location_search.send_keys(nome_loja)

# clica no resultado do search
result_search = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'js-og-picker__item'))).click()

# pesquisando bluebird
print('pesquisando bluebird...')
time.sleep(3)

# clica no Search List e pesquisa o bluebird
label_search = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, 'SearchText')))
label_search.send_keys(num_bluebird)
label_search.send_keys(Keys.RETURN)
time.sleep(3)

def program(): # valida se o dispositivo existe antes de executar

    # clica no "more"
    drop_more = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div/section[1]/nav/section/ul/li[4]/a')))
    drop_more.click()

    # clica no Products
    time.sleep(2)
    print(f'Acessando Products do BlueBird {num_bluebird}... ')
    drop_more_products = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="device-details-products"]')))
    drop_more_products.click()

    time.sleep(2)

    print("\n--------REPROCESSANDO--------")

    def reprocess_force():
    # mapear o FORCE REPROCESS
        time.sleep(2)

        # force_reprocess = driver.find_element(By.XPATH, '/html/body/main/div/div/div[3]/section/section/div/div/section[1]/div[2]/a[2]')
        force_reprocess = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div/div[3]/section/section/div/div/section[1]/div[2]/a[2]')))
        time.sleep(2)
        force_reprocess.click()
        time.sleep(2)
        alert()

    

        
    for N in range(8): # vai clicar em até 8 products
        
        if N > 0:
            print(f'Product {N}')
            print('procurando o product_selected')
            # time.sleep(4)
            # reprocessa o product_select
            product_select =  WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, f'/html/body/main/div/div/div[3]/section/section/div/div/section[3]/section[1]/table/tbody/tr[{N}]/td[1]')))
            print('achei o product_select')
            # time.sleep(5)
            # product_select.click()

            for x in product_select:
                x.click()
                print(f'cliquei no {x}')
                print('cliquei no product_select')

            print('vou reprocessar')
            reprocess_force()
            alert()
            time.sleep(2)
        

        
        
# depois de reprocessar todos products clicar em More Actions > Sync Device
    # map_more_actions = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="MoreActionsPopup"]')))
    # map_more_actions.click()
    # time.sleep(2)
    # print(f'Sincronizando Device {num_bluebird}')
    # map_more_actions_sync_devide = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div/hgroup/div[2]/div/section[2]/div[3]/ul/li[2]')))
    # map_more_actions_sync_devide.click()
    # alert()
    # time.sleep(2)
    # alert()


    print('Loop Encerrado!')

# tenta clicar no bluebird pesquisado
try: # valida se o dispositivo existe antes de executar
    
    btn_status_up = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="airwatchdevicelistsearch"]/section[3]/section[1]/table/tbody/tr/td[2]')))
    # time.sleep(3)
    btn_status_up.click()
    program()    
    
except:
    print('dispositivo não encontrato!')
    print('fechando em 30 segundos')
