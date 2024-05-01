from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Opciones para ejecutar en modo headless (sin interfaz gráfica)
options = Options()

# Especificar la ruta completa del WebDriver si no está en PATH
service = Service(executable_path="Progr/msedgedriver.exe")

# Iniciar el servicio del WebDriver
service.start()

# Iniciar Edge con las opciones definidas y el servicio
driver = webdriver.Edge(service=service, options=options)

# Abrir la página web deseada
driver.get("https://chat.openai.com/")

# Esperar hasta que el textarea esté presente
textarea = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "prompt-textarea"))
)

# Ingresar texto en el textarea
textarea.send_keys("¿Cómo estás?")

# Esperar hasta que el botón esté presente y sea clickable
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="send-button"]'))
)

# Hacer clic en el botón
button.click()

# Cerrar el navegador
driver.quit()

# Detener el servicio del WebDriver
service.stop()
