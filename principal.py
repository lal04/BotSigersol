from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from clase import bot
import pandas as pd


driver=webdriver.Chrome(ChromeDriverManager().install())
robot = bot()

driver.get('https://sistemas.minam.gob.pe/SigersolNM/login.xhtml')
#maximizar pestaña
#driver.maximize_window()
#mitad de pantalla
robot.mitad_pantalla(driver)
#accedemos a la cuenta

driver.find_element(By.ID,'formLogin:j_username').send_keys('2048641679420')
driver.find_element(By.ID,'formLogin:j_password').send_keys('HWPWRNAXXV')
driver.find_element(By.XPATH,'//*[@id="formLogin:btnEntrar"]').click()

#abrimos el menu lateral

WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//div[@id=\'j_idt19\']/ul/li/a/i")))
driver.find_element(By.XPATH, "//div[@id=\'j_idt19\']/ul/li/a/i").click()

#click en la primera opcion
WebDriverWait(driver,50).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#form-307\\3AmbarPrincipal_0 span")))
driver.find_element(By.CSS_SELECTOR, "#form-307\\3AmbarPrincipal_0 span").click()

#escoge el periodo
datos_periodo=[]
datos_periodo.append(int(input("ingresa el numero de trimeste: ")))
datos_periodo.append(int(input("ingresa el año: ")))
print(robot.busca(driver,datos_periodo[0],datos_periodo[1]))
#espetamos a que se muestre un elemento seleccionado, para confirmanr que estamos en la pagina correcta
#en este caso el texto "Plantas Registradas por Empresa"
encontado=WebDriverWait(driver,50).until(EC.text_to_be_present_in_element((By.XPATH,'//*[@id="formRegistroSigersol"]/div[2]/div/div/h1'),'Plantas Registradas por Empresa'))
if encontado==True:
    print("entramos en la pagina correcta!!")
else:
    print("ocurrio un error, no estamos en la pagina correcta o fallo en internet")

#revisar si se encuentra activado el boton cliente
WebDriverWait(driver,50).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="formRegistroSigersol:tblRegistroDeclaracion:0:btnClientes"]')))
driver.find_element(By.XPATH,'//*[@id="formRegistroSigersol:tblRegistroDeclaracion:0:btnClientes"]').click()

#espetamos a que se muestre un elemento seleccionado, para confirmar que estamos en la pagina correcta
#en este caso el texto "Clientes Registrados por Plantas"
encontado=WebDriverWait(driver,50).until(EC.text_to_be_present_in_element((By.XPATH,'//*[@id="formRegistroSigersol"]/div[2]/div/div/h1'),'Clientes Registrados por Plantas'))
time.sleep(6)
print("termino correctamente!!")
