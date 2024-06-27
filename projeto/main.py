from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

import gui as interface

# Configurar o serviço e opções do Chrome
servico = Service(ChromeDriverManager().install())
options = Options()
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
)

# Inicializar o navegador
navegador = webdriver.Chrome(service=servico, options=options)

# Definir os dados do formulário
url = interface.valorSite
nome = "tester redbit"
email = "gutodidonato@gmail.com"
telefone = "(11) 3951-8656"
cidade = "SP"
text_area = "Teste"
teste = f"Teste do site {url}, verificar!"

# Abrir a página de contato
navegador.get("http://" + url + "/contato")

try:
    # Localizar e mudar para o iframe
    iframe = WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.ID, 'IframeForm')))
    navegador.switch_to.frame(iframe)
    
    # Preencher o formulário
    campo_nome = WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.ID, 'nome')))
    campo_nome.send_keys(nome)
    
    campo_email = WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.ID, 'email')))
    campo_email.send_keys(email)
    
    campo_assunto = WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.ID, 'assunto')))
    campo_assunto.click()
    campo_valores_assunto = WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="assunto"]/option[5]')))
    campo_valores_assunto.click()
    
    campo_estado = WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.ID, 'estado')))
    campo_estado.click()
    campo_estado_valores = WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="estado"]/option[26]')))
    campo_estado_valores.click()
    
    campo_telefone = WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.ID, 'telefone')))
    campo_telefone.send_keys(telefone)
    
    campo_cidade = WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.ID, 'cidade')))
    campo_cidade.send_keys(cidade)
    
    campo_mensagem = WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.ID, 'mensagem')))
    campo_mensagem.send_keys(teste)
    
    try:
        campo_conhecimento = WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.ID, 'conhecimento')))
        campo_conhecimento.send_keys(text_area)
    except:
        print("Não tem campo conheceu!")
        pass
    
    try:
        campo_politica = WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.ID, 'politica')))
        campo_politica.click()
    except:
        print("Não tem campo politica!")
        pass
    
    enviar = WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'gtm-formulario-contato')))
    #enviar.click()
    time.sleep(30)
    
except Exception as e:
    print(f"Erro: {e}")

