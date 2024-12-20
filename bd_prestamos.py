import sqlite3
import os
import sys
#import psycopg2

class Comunicacion():
    def __init__(self):
        '''def __init__(self,user_name,password,hostbd,portdb,db_name):
            super(Comunicacion).__init__()
            try:
                self.conexion = psycopg2.connect(
                    user = {user_name},
                    password = {password},
                    host = {hostbd},
                    port= {portdb},
                    database = {db_name}
                )
            except (Exception, psycopg2.Error) as error:
                print(f'conexion rota {error}') '''

        #BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        nombre_bd = 'prestamos_bd.db'
        #ruta_bd = os.path.join(BASE_DIR,nombre_bd)
        ruta_bd = os.path.join(nombre_bd)
        
        self.config = sqlite3.connect(ruta_bd)

    def mostrar_datos_peajes(self):
        '''muestra la lista de peajes que han operado'''
        with self.config:
            cursor = self.config.cursor()
            bd = f'SELECT peaje from recaudar GROUP by peaje '
            cursor.execute(bd)
            registro = cursor.fetchall()
            return registro
        
    def mostrar_valor_actual(self,columnas,caja_bd):
        '''muestra la lista de peajes que han operado'''
        with self.config:
            cursor = self.config.cursor()
            bd = f'SELECT {columnas} from {caja_bd} order by id_caja desc limit 1 '
            cursor.execute(bd)
            registro = cursor.fetchall()
            return registro
    
    def mostrar_datos_tabla(self,columna,tabla):
        cursor = self.config.cursor()
        bd = f'SELECT {columna} FROM {tabla}'
        cursor.execute(bd)
        registro = cursor.fetchall()
        return registro
    
    def mostrar_datos(self,columna=None,tabla=None):
        cursor = self.config.cursor()
        bd = f'SELECT {columna} FROM {tabla}'
        cursor.execute(bd)
        registro = cursor.fetchall()
        return registro
        
    def suma_element_misma_columna(self,columna,tabla):
        ''' Sumar todos los elementos de una sola columna tal que se demanda asi
            sumar COLUMNA de  NOMBRE_TABLA .
        '''
        #with sqlite3.connect('pettite_chics.db') as config:
        with self.config:
            cursor = self.config.cursor()
            self.bd =f'''SELECT SUM({columna}) FROM {tabla} '''
            cursor.execute(self.bd)
            self.resultado = cursor.fetchone()[0]
            return self.resultado
        
    def suma_resumen_peaje(self,fecha):
        ''' Suma el total de las columnas ordenados por peaje .
        '''
        with self.config:
            cursor = self.config.cursor()
            self.bd =f''' SELECT id_recaudar,peaje,sum(turno1), sum(turno2), sum(turno3), sum(total) FROM recaudar WHERE tipo ='Peaje' and fecha like "%{fecha}%" GROUP by peaje ORDER BY fecha ASC'''
            print(self.bd)

            cursor.execute(self.bd)
            self.resultado = cursor.fetchall()
            return self.resultado
        
    def resumen_peaje(self,columnas,tabla,columna,fecha,peajes):
        ''' Suma el total de las columnas ordenados por peaje y despues crea una nueva columna de los totales.
        '''
        with self.config:
            cursor = self.config.cursor()
            lista_peajes = []
            for peaje in peajes:
                nueva_lista = f'sum({peaje})'
                lista_peajes.append(nueva_lista)
                lista=','.join(lista_peajes)
                lista_peaje = lista.replace(',','+')
            self.bd =f''' SELECT {columnas}, sum({lista_peaje}) OVER(PARTITION BY fecha) as total_turnos FROM {tabla} WHERE {columna} like "%{fecha}%" GROUP by fecha ORDER BY fecha ASC'''
            print(self.bd)
            cursor.execute(self.bd)
            self.resultado = cursor.fetchall()
            return self.resultado
        
    def mostrar_un_elemento(self,columna,tabla,campo,celda,campo_orden):
        '''mostrar el ultimo elemento ordenado por una variable ej: fecha'''
        with self.config:
            cursor = self.config.cursor()
            self.bd =f'''select {columna} from {tabla} where {campo}='{celda}' ORDER by {campo_orden} DESC limit 1'''
            cursor.execute(self.bd)
            self.resultado = cursor.fetchall()
            return self.resultado

        
    def mostrar_last_elemento(self,columna,tabla,campo_orden):
        '''mostrar el ultimo elemento ordenado por una variable ej: fecha'''
        with self.config:
            cursor = self.config.cursor()
            self.bd =f'''select {columna} from {tabla} ORDER by {campo_orden} DESC limit 1'''
            cursor.execute(self.bd)
            self.resultado = cursor.fetchall()
            return self.resultado

        
    def suma_resumen_barrera(self,fecha):
        ''' Suma el total de las columnas ordenados por peaje .
        '''
        with self.config:
            cursor = self.config.cursor()
            self.bd =f''' SELECT id_recaudar,peaje,sum(turno1), sum(turno2), sum(turno3), sum(total) FROM recaudar WHERE tipo ='Barrera' and fecha like "%{fecha}%" GROUP by peaje order by fecha ASC'''#WHERE fecha 
            cursor.execute(self.bd)
            self.resultado = cursor.fetchall()
            return self.resultado

            #
        
    def suma_elementos_columna_filtro(self,columna,tabla,campo,celda):
        ''' Sumar todos los elementos de una sola columna tal que se demanda asi
            sumar COLUMNA de la NOMBRE_TABLA donde Valor_campo_tabla_bd =valor variable GUI.
        '''
        #with sqlite3.connect('pettite_chics.db') as config:
        with self.config:
            cursor = self.config.cursor()
            self.bd =f'''SELECT SUM({columna}) FROM {tabla} where {campo} like "%{celda}%" '''
            cursor.execute(self.bd)
            self.resultado = cursor.fetchone()[0]
            return self.resultado
    
    def suma_elementos_columna(self,columnaA,columnaB,columnaC,tabla,dato,valor):
        #with sqlite3.connect('pettite_chics.db') as config:
        with self.config:
            self.cursor = self.config.cursor()
            self.bd =f'''SELECT {columnaA}+{columnaB}-{columnaC} FROM {tabla} WHERE {dato} = "{valor}" '''
            self.cursor.execute(self.bd)
            self.resultado = self.cursor.fetchone()[0]
            return self.resultado


    def insertar(self,tabla,campos,values):
        #with sqlite3.connect('pettite_chics.db') as config:
        with self.config:
            cursor = self.config.cursor()
            self.bd =f'''INSERT INTO {tabla} ({campos})  VALUES {values}'''
            self.bd
            cursor.execute(self.bd)
            self.config.commit()

    def insertar_fecha(self,tabla,campos,values):
        #with sqlite3.connect('pettite_chics.db') as config:
        with self.config:
            cursor = self.config.cursor()
            self.bd =f'''INSERT OR IGNORE INTO {tabla} ({campos})  VALUES ({values})'''
            self.bd
            cursor.execute(self.bd)
            self.config.commit()

    def actualizar_tickets(self,tabla,columna_upd1, datos1,datos2):
        #with sqlite3.connect('pettite_chics.db') as config:
        with self.config:
            cursor = self.config.cursor()
            self.bd =f'''UPDATE {tabla} SET  {columna_upd1} = 50* {datos1}*{datos2}'''
            cursor.execute(self.bd)
            self.config.commit()

    def actualizar_tickets_invent(self,tabla,columna_upd1, datos1,datos2,columna,valor_celda):
        '''tabla, columna_a _actualizar 50* dato1 * dato2 donde id[columna] = valor_celda Id QLineEdit'''
        #with sqlite3.connect('pettite_chics.db') as config:
        with self.config:
            cursor = self.config.cursor()
            self.bd =f'''UPDATE {tabla} SET  {columna_upd1} = 50* {datos1}*{datos2} WHERE {columna}={valor_celda}'''
            cursor.execute(self.bd)
            self.config.commit()

    def actualizar_monet(self,tabla,columna_upd1, datos1,datos2):
        #with sqlite3.connect('pettite_chics.db') as config:
        with self.config:
            cursor = self.config.cursor()
            self.bd =f'''UPDATE {tabla} SET  {columna_upd1} = {datos1}*{datos2} '''
            cursor.execute(self.bd)
            self.config.commit()
           
    def update(self,tabla,dato, valor,columna,valor_celda):
        '''actualiza la TABLA y pon el DATO = VALOR, donde NOMBRE_COLUMNA = VALOR_CELDA'''
        #with sqlite3.connect('pettite_chics.db') as config:
        with self.config:
            cursor = self.config.cursor()
            self.bd =f'''UPDATE {tabla} SET  {dato} = "{valor}" WHERE {columna}="{valor_celda}"'''
            cursor.execute(self.bd)
            self.config.commit()

    def update_multiple(self,tabla,dato_multiples, columna,valor_celda):
        '''actualiza la TABLA y pon el DATO = VALOR, donde NOMBRE_COLUMNA = VALOR_CELDA'''
        #with sqlite3.connect('pettite_chics.db') as config:
        with self.config:
            cursor = self.config.cursor()
            self.bd =f'''UPDATE {tabla} SET  {dato_multiples} WHERE {columna}={valor_celda}'''
            cursor.execute(self.bd)
            self.config.commit()

    def update_operacion(self,tabla,dato, valor1,signo,valor2,columna,valor_celda):
        '''actualiza la TABLA y pon el DATO = VALOR, donde NOMBRE_COLUMNA = VALOR_CELDA'''
        #with sqlite3.connect('pettite_chics.db') as config:
        with self.config:
            cursor = self.config.cursor()
            self.bd =f'''UPDATE {tabla} SET  {dato} = ({valor1} {signo} {valor2}) WHERE {columna}="{valor_celda}"'''
            cursor.execute(self.bd)
            self.config.commit()

    def update_filtro(self,tabla,dato, valor,dato2, valor2,dato3,valor3,columna,valor_celda, columna2,valor_celda2):
        '''actualiza la TABLA y pon el DATO = VALOR, donde NOMBRE_COLUMNA = VALOR_CELDA'''
        #with sqlite3.connect('pettite_chics.db') as config:
        with self.config:
            cursor = self.config.cursor()
            self.bd =f'''UPDATE {tabla} SET  {dato} = "{valor}", {dato2} = "{valor2}", {dato3} = "{valor3}" WHERE {columna}="{valor_celda}" and {columna2} ="{valor_celda2}"'''
            cursor.execute(self.bd)
            self.config.commit()

    def update_control(self,tabla,dato, valor1,valor2,columna,valor_celda, columna2,valor_celda2):
        '''actualiza la TABLA y pon el DATO = VALOR, donde NOMBRE_COLUMNA = VALOR_CELDA'''
        #with sqlite3.connect('pettite_chics.db') as config:
        with self.config:
            cursor = self.config.cursor()
            self.bd =f'''UPDATE {tabla} SET  {dato} = ({valor1} - {valor2}) WHERE {columna}="{valor_celda}" and {columna2} ="{valor_celda2}"'''
            cursor.execute(self.bd)
            self.config.commit()

    def contar_item(self,tabla):
        #with sqlite3.connect('pettite_chics.db') as config:
        with self.config:
            cursor = self.config.cursor()
            query= f'SELECT COUNT () as total FROM {tabla} '
            cursor.execute(query)
            registro = cursor.fetchall()
            return registro
        
    def borrar_datos_comp(self,tabla):
       #with sqlite3.connect('pettite_chics.db') as config:
        ''' Recibe el nombre de la tabla y borra todos los datos que tiene dentro'''
        with self.config:
            self.cursor = self.config.cursor()
            self.bd =f'''DELETE from {tabla} '''
            self.cursor.execute(self.bd)
            self.config.commit()

    def borrar_fila(self,tabla,referencia,valor):
       #with sqlite3.connect('pettite_chics.db') as config:
        ''' Recibe el nombre de la tabla y borra todos los datos que tiene dentro'''
        with self.config:
            self.cursor = self.config.cursor()
            self.bd =f'''DELETE from {tabla} WHERE {referencia} ={valor} '''
            self.cursor.execute(self.bd)
            self.config.commit()
           

    def filtro_condicion(self,columnas,tabla,columna,celda):
        #with sqlite3.connect('pettite_chics.db') as config:
        with self.config:
            cursor = self.config.cursor()
            bd = f"SELECT {columnas} FROM {tabla} WHERE {columna} LIKE '%{celda}%'"
            cursor.execute(bd)
            print(bd)
            registro = cursor.fetchall()
            return registro
        
    def filtro_select(self,columnas,tabla,columna,celda):
        #with sqlite3.connect('pettite_chics.db') as config:
        with self.config:
            cursor = self.config.cursor()
            bd = f"SELECT {columnas} FROM {tabla} WHERE {columna} = {celda}"
            cursor.execute(bd)
            registro = cursor.fetchall()
            return registro
        
    def mostrar_condicion(self,columnas,tabla,columna,celda):
        ''' Motrar datos a partir de una condicion igualatoria'''
        #with sqlite3.connect('pettite_chics.db') as config:
        with self.config:
            cursor = self.config.cursor()
            bd = f"SELECT {columnas} FROM {tabla} WHERE {columna} = {celda}"
            cursor.execute(bd)
            registro = cursor.fetchall()
            return registro
        
    def filtro_condicion_date(self,columnas,tabla,columna,celda,columna2,celda2,columna3,celda3):
        '''select columnas from tabla where columna = celda and columna2 a0 celda2'''
        #with sqlite3.connect('pettite_chics.db') as config:
        with self.config:
            cursor = self.config.cursor()
            bd = f"SELECT {columnas} FROM {tabla} WHERE {columna} " 
            if columna:
                bd += f"LIKE '%{celda}%'" 
            else:
                bd += "1 = 1"
            if columna2 :
                bd  += f" and {columna2} like '%{celda2}%'"  
            else:
                bd += "1 = 1"      
            if columna3 :
                bd  += f" and {columna3} like '%{celda3}%'"           
            cursor.execute(bd)
            registro = cursor.fetchall()
            return registro
        
    def crear_columna(self,nombre_tabla,column_name):
        try:
            with self.config:
                cursor = self.config.cursor()
                self.bd = (f'''PRAGMA table_info ({nombre_tabla})''')
                columns=cursor.fetchall()
                column_exist=any(column[1]==column_name for column in columns)
                if not column_exist:
                    self.bd = (f'''ALTER TABLE {nombre_tabla} ADD COLUMN {column_name} TEXT''')
                    cursor.execute(self.bd)
                    self.config.commit()
        except Exception :
            pass
        
    def crear_una_tabla(self):
        try:
            with self.config:
                cursor = self.config.cursor()
                self.bd = (f'''  
                    CREATE TABLE IF NOT EXISTS "users" (
                    "id_users"	INTEGER NOT NULL,
                    "nombre"	TEXT NOT NULL,
                    "correo"	TEXT,
                    "user_name"	TEXT NOT NULL UNIQUE,
                    "passwd"	TEXT NOT NULL,
                    "telefono"	TEXT NOT NULL,
                    "pasport"	TEXT,
                    "domicilio"	TEXT,
                    "permisos"	TEXT,
                    PRIMARY KEY("id_users" AUTOINCREMENT)); ''')
                cursor.execute(self.bd)
                self.config.commit()
        except Exception as e:
            print(e)

                           
    def crear_tablas(self):
        try:
            with self.config:
                cursor = self.config.cursor()
                self.bd = (f'''  
                    CREATE TABLE IF NOT EXISTS "entradas" (
                        "entrada_id"	INTEGER NOT NULL,
                        "fecha"	TEXT NOT NULL,
                        "codigo_valores"	TEXT,
                        "descripcion_valores"	TEXT,
                        "entrada_valores"	TEXT,
                        "total_tickets"	INTEGER,
                        "total_monetario"	INTEGER,
                        PRIMARY KEY("entrada_id")
                    );
                    CREATE TABLE IF NOT EXISTS "facturas" (
                        "id_facturas"	INTEGER NOT NULL,
                        "fecha"	TEXT,
                        "no_facturas"	INTEGER,
                        "proveedor"	TEXT,
                        "direccion_prov"	TEXT,
                        "telefono_prov"	TEXT,
                        "cliente"	TEXT,
                        "direccion_client"	TEXT,
                        "telefono_client"	TEXT,
                        "detalle"	TEXT,
                        "total"	INTEGER,
                        PRIMARY KEY("id_facturas" AUTOINCREMENT)
                    );
                    CREATE TABLE IF NOT EXISTS  "inventario" (
                        "codigo_valores"	TEXT NOT NULL,
                        "descripcion"	TEXT,
                        "valores_iniciales"	INTEGER,
                        "stock_minimo"	INTEGER,
                        "entrada_valores"	INTEGER,
                        "salida_valores"	INTEGER,
                        "stock_actual"	INTEGER,
                        "stock_tickets"	INTEGER,
                        "total_monetario"	INTEGER
                    );
                    CREATE TABLE IF NOT EXISTS  "justificante_entrega" (
                        "justifi_id"	INTEGER NOT NULL,
                        "fecha"	TEXT,
                        "no_entrega"	INTEGER,
                        "recaudador_name"	TEXT,
                        "telefono"	INTEGER,
                        "peaje"	TEXT,
                        "detalles"	TEXT,
                        "valores_entregados"	INTEGER,
                        "total_monetario"	INTEGER,
                        PRIMARY KEY("justifi_id" AUTOINCREMENT)
                    );
                    CREATE TABLE IF NOT EXISTS  "justificante_valores" (
                        "id_justificante"	INTEGER NOT NULL,
                        "valores"	TEXT,
                        "descripcion"	TEXT,
                        "valores_entregados"	INTEGER,
                        "total_tickets"	INTEGER,
                        "total_monetario"	INTEGER,
                        PRIMARY KEY("id_justificante" AUTOINCREMENT)
                    );
                    CREATE TABLE IF NOT EXISTS  "peajes_barreras" (
                        "id_peajes" INTEGER NOT NULL,
                        "peaje"	TEXT NOT NULL,
                        "responsable"	TEXT,
                        "contacto"	TEXT,
                        PRIMARY KEY("id_peajes" AUTOINCREMENT)
                    );
                    CREATE TABLE IF NOT EXISTS  "recaudador" (
                        "id_recaudador" INTEGER NOT NULL,
                        "nombre"	TEXT,
                        "telefono"	TEXT,
                        "dip_pasaporte"	TEXT,
                        "domicilio"	TEXT,
                        PRIMARY KEY("id_recaudador" AUTOINCREMENT)
                    );
                    CREATE TABLE IF NOT EXISTS  "salidas" (
                        "id_salidas"	INTEGER NOT NULL,
                        "fecha"	TEXT,
                        "codigo_valores"	TEXT,
                        "descripcion_valores"	INTEGER,
                        "peajes_barreras"	TEXT,
                        "recaudador"	TEXT,
                        "salida_valores"	INTEGER,
                        "total_tickets"	INTEGER,
                        "total_monetario"	INTEGER,
                        "fecha_retorno" TEXT,
                        "retorno_valores" INTEGER,
                        "total_monetario_retorno" INTEGER,
                        "remanente_valores" INTEGER,
                        "total_remanente_tickets" INTEGER,
                        "remanente_monetario" INTEGER,
                        PRIMARY KEY("id_salidas" AUTOINCREMENT)
                    );
                    CREATE TABLE IF NOT EXISTS  "ventas_hoy" (
                        "id_ventas"	INTEGER NOT NULL,
                        "cantidad"	TEXT,
                        "concepto"	TEXT,
                        "precio_unidad"	INTEGER,
                        "total"	INTEGER,
                        PRIMARY KEY("id_ventas" AUTOINCREMENT)
                    );                  
                ''')
                cursor.executescript(self.bd)
                self.config.commit()
        except Exception as e:
            print(f'error de base de datos {e}')



class Conexion():
    def __init__(self):
        nombre_bd = 'users.db'
        ruta_bd = os.path.join(nombre_bd)
        self.config = sqlite3.connect(ruta_bd)
    
    def insertar(self,tabla,campos,values):
        with self.config:
            cursor = self.config.cursor()
            self.bd =f'''INSERT INTO {tabla} ({campos})  VALUES {values}'''
            self.bd
            cursor.execute(self.bd)
            self.config.commit()

    def mostrar_datos_tabla(self,columna,tabla):
        cursor = self.config.cursor()
        bd = f'SELECT {columna} FROM {tabla}'
        cursor.execute(bd)
        registro = cursor.fetchall()
        return registro