from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException



class bot:
    def __init__(self):
        pass


    def busca(self, objeto, num_trimeste, num_año,):
        #este metodo recorre la tabla de periodos para encontrar coincidencias con los datos ingresados en primera insntancias(numero de trimeste y el año)
        #cuando los encuentra presiona el boton ingresar

        try:
            for i in range(1, 12):
                time.sleep(3)
                print("repeticion numero:", i)
                trimeste = int(objeto.find_element(By.XPATH, '//*[@id="formRegistroSigersol:tblRegistroInforme_data"]/tr['+str(i)+']/td[6]').text)
                año = int(objeto.find_element(
                    By.XPATH, '//*[@id="formRegistroSigersol:tblRegistroInforme_data"]/tr['+str(i)+']/td[5]').text)
                print(trimeste, año)
                if num_trimeste == trimeste and num_año == año:
                    objeto.find_element(
                        By.XPATH, '//*[@id="formRegistroSigersol:tblRegistroInforme:'+str(i-1)+':btnEditar"]').click()

                    time.sleep(5)
                    print("dimos click en ingresar!!")
                    break
        except NoSuchElementException:
            print("no se encontro el elemento: ")
            return False
            

    def mitad_pantalla(self, pantalla):
        #divide la pantalla del navegador a la mitad
        #ubica la ventana del navegador al lado izquierdo
        # dimersion de ventana
        pantalla.set_window_size(691, 744)
        size = pantalla.get_window_size()
        print("las dimensiones de la ventana son: ", size)
        # posicion de ventan
        pantalla.set_window_position(-7, 0)
        position = pantalla.get_window_position()
        print("las posicion de la ventana es: ", position)
    
    def crear_ficha (self, crea):
        #crear la ficha
        #llenar los primeros datos de la ficha
        pass
    
    def llenar_ficha(self,escribe):
        #llena la ficha con los datos de la base de datos
        pass

    def encuentra_ficha(self, identificador, direccion):
        #recorre la tabla de los clientes ingresados
        #busca la ficha ingresada
        #quita los espaacios en los valores que se van a comparar
        for i in range(1, 11):
            dire_en_tabla = identificador.find_element(
                By.XPATH, '//*[@id="formRegistroSigersol:tblRegistroDeclaracion_data"]/tr['+str(i)+']/td[5]').text
            dire_en_tabla = dire_en_tabla.replace(" ", "")
            direccion=direccion.replace(" ","")
            if direccion == dire_en_tabla:
                print("lo encontramos!!")
                self.llenar_ficha(identificador)
                
                pass

            print("fila numero: ", i)
    def buscador_simplificado(self, objeto, numero_trimestre, numero_año,):
        dataframe=pd.read_html(objeto.current_url)
        df=dataframe[0]
        for index, row in df.iterrows():
            print(index)
            if row[6]==numero_trimestre and row[5]==numero_año :
                print("lo encontramos...")
            elif index ==5:
                print("no lo encontramos: ...")

        
        pass