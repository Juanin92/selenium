from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tempfile
import time

options = Options()
options.add_argument("--headless")  # Ejecutar sin UI (opcional en CI)
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Crear un perfil temporal único para evitar conflicto
profile_dir = tempfile.mkdtemp(prefix="edge-profile-")
options.add_argument(f"--user-data-dir={profile_dir}")

service = Service('/usr/local/bin/msedgedriver')  # Ruta del driver en GitHub Actions runner

driver = webdriver.Edge(service=service, options=options)

driver.get("https://duckduckgo.com/")

# Buscar campo de texto
buscador = driver.find_element(By.NAME, "q")
buscador.send_keys("inmuebles en Melipilla")
buscador.send_keys(Keys.RETURN)

# Esperar resultados
time.sleep(2)

# Verificar que exista algún resultado
wait = WebDriverWait(driver, 10)  # espera hasta 10 segundos
resultados = wait.until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-testid="result"]'))
)
assert len(resultados) > 0, "No se encontraron resultados."

print("Prueba funcional completada con éxito")

driver.quit()
