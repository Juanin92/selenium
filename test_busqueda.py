from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
import time

options = Options()
options.add_argument("--headless")  # para que corra sin GUI en GitHub Actions
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
# 👇 Asegúrate de **no** agregar `--user-data-dir`
# options.add_argument("--user-data-dir=/path/que/choca") ← esto NO lo uses

driver = webdriver.Edge(options=options)

driver.get("https://duckduckgo.com/")

# Buscar campo de texto
buscador = driver.find_element(By.NAME, "q")
buscador.send_keys("inmuebles en Melipilla")
buscador.send_keys(Keys.RETURN)

# Esperar resultados
time.sleep(2)

# Verificar que exista algún resultado
# resultados = driver.find_elements(By.CSS_SELECTOR, "div.result")
resultados = driver.find_elements(By.CSS_SELECTOR,'[data-testid="result"]')
assert len(resultados) > 0, "No se encontraron resultados."

print("Prueba funcional completada con éxito")

driver.quit()
