from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Caminho correto para o seu ChromeDriver
webdriver_service = Service(r'c:\Users\thiago.bravi\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe')

# Inicializa o navegador
driver = webdriver.Chrome(service=webdriver_service)

# Abre a página
driver.get('https://superset.data.quintoandar.com.br/sqllab?savedQueryId=2262')

# Espera até que um elemento específico esteja presente (ajuste conforme necessário)
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'element-id'))  # Substitua 'element-id' pelo ID de um elemento que você espera ver na página
    )
    print("Página carregada com sucesso.")
except TimeoutException:
    print("Tempo de espera expirado. A página pode não ter carregado completamente.")

# Feche o navegador após o teste
driver.quit()
