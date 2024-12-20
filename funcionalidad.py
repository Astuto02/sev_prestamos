from PySide6.QtWidgets import (QApplication,QMainWindow,QDialog, QVBoxLayout,QLabel,QFrame, QPushButton,
                               QGridLayout, QLineEdit,QHBoxLayout,QDateEdit,QComboBox,QTextEdit,QCompleter,QMessageBox)
from PySide6.QtCore import Qt
from datetime import datetime,timedelta

from backend import Tabla,MostrarDatos_in,SelecRow,OperacionesMath
from bd_prestamos import Comunicacion

#from operando import OperandoClientes

import math as m



from flotante import Flotante
import json

class Funcionamiento():
    def __init__(self):
        super().__init__()

        self.base_datos = Comunicacion()


    def amortizacion(self,monto_prestado,tasa_interes,num_cuotas):
        tasa_interes = float(tasa_interes)/100 # convertir a decimal
        cuota_fija = (monto_prestado * float(tasa_interes) * (1+ float(tasa_interes))** num_cuotas) / ((1+ float(tasa_interes))**num_cuotas -1)
        saldo_restante = monto_prestado
        tabla_amortizacion = []

        for item in range(1,num_cuotas + 1):
            interes = saldo_restante * float(tasa_interes)
            capital = cuota_fija - float(interes)
            saldo_restante =  saldo_restante - capital
            tabla_amortizacion.append({
                "Cuota":cuota_fija,
                "Capital":capital,
                "Interes":interes,
                "Saldo":saldo_restante
            })
        #json_str = json.dumps(tabla_amortizacion)
        
        return tabla_amortizacion

    
    def amortiza_guinea(self,monto_prestado,tasa_interes,num_cuotas):
        tasa_interes = float(tasa_interes)/100 # convertir a decimal
        interes_now = monto_prestado * tasa_interes
        intereses  = interes_now * num_cuotas
        cuota_fija = (intereses + monto_prestado)/num_cuotas
        saldo_restante = monto_prestado
        tabla_amortizacion = []

        for item in range(1,num_cuotas + 1):
            interes = interes_now
            capital = cuota_fija - float(interes)
            saldo_restante =  saldo_restante - capital
            tabla_amortizacion.append({
                "Cuota":m.ceil(cuota_fija),
                "Capital":m.ceil(capital),
                "Interes":m.ceil(interes),
                "Saldo":m.ceil(saldo_restante)
            })
        
        return tabla_amortizacion
    
    def amortiza_guinea_dato(self,monto_prestado,tasa_interes,num_cuotas):
        tasa_interes = float(tasa_interes)/100 # convertir a decimal
        interes_now = monto_prestado * tasa_interes
        intereses  = interes_now * num_cuotas
        cuota_fija = (intereses + monto_prestado)/num_cuotas
        saldo_restante = monto_prestado
        tabla_amortizacion = []

        for item in range(1,num_cuotas + 1):
            interes = interes_now
            capital = cuota_fija - float(interes)
            saldo_restante =  saldo_restante - capital
            tabla_amortizacion.append({
                "Cuota":m.ceil(cuota_fija),
                "Capital":m.ceil(capital),
                "Interes":m.ceil(interes),
                "Saldo":m.ceil(saldo_restante)
            })
        
        return tabla_amortizacion
    


class OPcionesPrestamo():
    def __init__(self):
        super(OPcionesPrestamo).__init__()

        self.show_opcion()
        self.btn_nuevo.clicked.connect(self.prestamo_in)
        #self.btn_consultar.clicked.connect(self.prestamo_consult)

        

        #self.agregar_ver.exec()

    def show_opcion(self):

        self.layout_main = QVBoxLayout()

        self.btn_nuevo = QPushButton('NUEVO PRESTAMO', objectName='nuevo_prestamo')
        self.btn_consultar = QPushButton('DETALLES PRESTAMOS', objectName='presta_consultar')

        self.layout_main.addWidget(self.btn_nuevo)
        self.layout_main.addWidget(self.btn_consultar)
        #self.agregar_ver.fr_container.setLayout(self.layout_main)


    def prestamo_in(self):
        self.prestamo = Prestamo()
        #self.prestamo.()
    def prestamo_consult(self):
        self.prestamo = ConsultaPrestamo()
        #self.prestamo.()


class Prestamo():
    def __init__(self):
        super(Prestamo).__init__()

        
        self.show_prestamo()
        self.func = Funcionamiento()

        self.base_datos = Comunicacion()

        self.buscar_prestar.textChanged.connect(self.consultar_list_clientes)
        self.nombre.textActivated.connect(self.mostrar_datos_cliente)
        self.update_btn.clicked.connect(self.amortizar_money)
        self.tiempo.textActivated.connect(self.gestion_tiempos)
        self.tiempo_tipo()
        self.orden_oper_ref()





    def show_prestamo(self):
        #self.agregar_ver.close()
        '''El prestamo y todas las operaciones relacionadas, interes generado, cuotas asi como otras cositas'''

        self.lay_general = QVBoxLayout()

        self.fr_top_date = QFrame()
        self.fr_top_date.setFixedHeight(80)
        self.fr_data_client = QFrame()
        self.fr_tabla_data = QFrame()

        self.top_layout = QHBoxLayout()
        self.top_layout.setContentsMargins(0,0,0,0)
        self.central_layout =  QHBoxLayout()
        self.central_layout.setContentsMargins(0,0,0,0)
        self.lay_tabla_datos = QVBoxLayout()


        self.fr_top_date.setLayout(self.top_layout)
        self.fr_data_client.setLayout(self.central_layout)
        self.fr_tabla_data.setLayout(self.lay_tabla_datos)


        self.lay_general.addWidget(self.fr_top_date,10)
        self.lay_general.addWidget(self.fr_data_client,30)
        self.lay_general.addWidget(self.fr_tabla_data,60)


        self.fr_fondos_info = QFrame()
        self.fr_fondos_date = QFrame()

        self.fondos_inf_lay = QGridLayout()
        self.fondos_date_lay = QVBoxLayout()

        self.fr_fondos_info.setLayout(self.fondos_inf_lay)
        self.fr_fondos_date.setLayout(self.fondos_date_lay)

        self.top_layout.addWidget(self.fr_fondos_info)
        self.top_layout.addStretch()
        self.top_layout.addWidget(self.fr_fondos_date)


        ################################################################
        self.fondos_dispo =QLabel('Fondos disponibles')
        self.fondos_dispo_entry =QLineEdit(objectName='especiales')
        self.fondos_dispo_entry.setReadOnly(True)
        self.prestamos_otorg =QLabel('Prestamos otorgados')
        self.prestamos_otor_entry =QLineEdit(objectName='especiales')
        self.prestamos_otor_entry.setReadOnly(True)

        buscar_prestar = QLabel('Buscar clientes ')
        self.buscar_prestar = QLineEdit()
        self.buscar_prestar.setFixedHeight(30)
        self.buscar_prestar.setPlaceholderText(' buscar Nombre de cliente')

        self.orden_opera = QLabel(objectName='refe_op')

        self.fondos_inf_lay.addWidget(self.fondos_dispo,0,0)
        self.fondos_inf_lay.addWidget(self.fondos_dispo_entry,0,1)
        self.fondos_inf_lay.addWidget(self.prestamos_otorg,1,0)
        self.fondos_inf_lay.addWidget(self.prestamos_otor_entry,1,1)
        self.fondos_inf_lay.addWidget(buscar_prestar,2,0)
        self.fondos_inf_lay.addWidget(self.buscar_prestar,2,1)
        self.fondos_inf_lay.addWidget(self.orden_opera,2,2)


        ###############################################################
        self.clientes_datos = QFrame()
        self.prestamo_info  = QFrame()
        self.infor_data  = QFrame()

        self.central_layout.addWidget(self.clientes_datos,25)
        self.central_layout.addWidget(self.prestamo_info,50)
        self.central_layout.addWidget(self.infor_data,25)


        self.lay_client_datos = QGridLayout()
        self.lay_prestamo = QGridLayout()
        self.lay_info_pres = QGridLayout()

        self.clientes_datos.setLayout(self.lay_client_datos)
        self.prestamo_info.setLayout(self.lay_prestamo)
        self.infor_data.setLayout(self.lay_info_pres)

        nombre = QLabel('Nombre ')
        dip_numero = QLabel('DIP o PASAPORTE ')
        direccion = QLabel('Direccion ')
        telefono = QLabel('Telefono ')

        self.nombre = QComboBox()
        self.nombre.setFixedHeight(20)
        self.dip_pasaporte = QLineEdit()
        self.direccion = QLineEdit()
        self.telefono = QLineEdit()

        self.lay_client_datos.addWidget(nombre,0,0)
        self.lay_client_datos.addWidget(dip_numero,1,0)
        self.lay_client_datos.addWidget(direccion,2,0)
        self.lay_client_datos.addWidget(telefono,3,0)
        self.lay_client_datos.addWidget(self.nombre,0,1)
        self.lay_client_datos.addWidget(self.dip_pasaporte,1,1)
        self.lay_client_datos.addWidget(self.direccion,2,1)
        self.lay_client_datos.addWidget(self.telefono,3,1)


        #prestamo
        fecha = QLabel('Fecha ')
        prestamo_monto = QLabel('Prestamo monto ')
        tasa_interes = QLabel('Tasa de interes ')
        periodos = QLabel('Periodos ')
        fecha_inicio = QLabel('Fecha de Inicio ')
        tiempo = QLabel('Tiempo ')
        tipo_pago = QLabel('Tipo de pago ')

        self.fecha = QDateEdit()
        self.fecha.setCalendarPopup(True)
        self.fecha.setDate(datetime.today())
        self.fecha.date().toString('dd/MM/yyyy') 

        self.prestamo_monto = QLineEdit()
        self.tasa_interes = QLineEdit()
        self.periodos = QLineEdit()
        self.update_btn = QPushButton(objectName='upd_tabla')

        self.fecha_inicio = QDateEdit()
        self.fecha_inicio.setCalendarPopup(True)
        self.fecha_inicio.setDate(datetime.today())
        self.fecha_inicio.date().toString('dd/MM/yyyy') 
        self.tiempo = QComboBox()
        self.tipo_pago = QComboBox()
        amortizable = QLabel('Amortizacion:')
        self.amortizable = QComboBox()

        amorti = ['Guineana','Frances']
        for item in amorti:
            self.amortizable.addItem(item)

        self.lay_prestamo.addWidget(fecha,0,0)
        self.lay_prestamo.addWidget(prestamo_monto,1,0)
        self.lay_prestamo.addWidget(tasa_interes,2,0)
        self.lay_prestamo.addWidget(periodos,3,0)
        self.lay_prestamo.addWidget(fecha_inicio,0,2)
        self.lay_prestamo.addWidget(tiempo,1,2)
        self.lay_prestamo.addWidget(tipo_pago,2,2)
        self.lay_prestamo.addWidget(self.fecha,0,1)
        self.lay_prestamo.addWidget(self.prestamo_monto,1,1)
        self.lay_prestamo.addWidget(self.tasa_interes,2,1)
        self.lay_prestamo.addWidget(self.periodos,3,1)
        self.lay_prestamo.addWidget(amortizable,4,0)
        self.lay_prestamo.addWidget(self.amortizable,4,1)
        self.lay_prestamo.addWidget(self.update_btn,3,3)
        self.lay_prestamo.addWidget(self.fecha_inicio,0,3)
        self.lay_prestamo.addWidget(self.tiempo,1,3)
        self.lay_prestamo.addWidget(self.tipo_pago,2,3)

        cuota_mensual = QLabel('Cuota mensual ')
        intereses_totales = QLabel('Intereses totales ')
        total_pagar = QLabel('Monto total a pagar ')

        self.cuota_mensual = QLineEdit(objectName='especiales')
        self.cuota_mensual.setReadOnly(True)
        self.intereses_totales = QLineEdit(objectName='especiales')
        self.intereses_totales.setReadOnly( True)
        self.total_pagar = QLineEdit(objectName='especiales')
        self.total_pagar.setReadOnly(True)

        self.lay_info_pres.addWidget(cuota_mensual,0,0)
        self.lay_info_pres.addWidget(intereses_totales,1,0)
        self.lay_info_pres.addWidget(total_pagar,2,0)
        self.lay_info_pres.addWidget(self.cuota_mensual,0,1)
        self.lay_info_pres.addWidget(self.intereses_totales,1,1)
        self.lay_info_pres.addWidget(self.total_pagar,2,1)

        self.fr_botones = QFrame()
        self.lay_info_pres.addWidget(self.fr_botones,3,0,1,3)

        self.lay_botones_info = QHBoxLayout()
        self.fr_botones.setLayout(self.lay_botones_info)

        self.btn_back = QPushButton(objectName='volver')
        self.btn_delete = QPushButton(objectName='delete')
        self.btn_save_info = QPushButton(objectName='save_prest')

        self.lay_botones_info.addWidget(self.btn_back)
        #self.lay_botones_info.addWidget(self.btn_delete)
        self.lay_botones_info.addWidget(self.btn_save_info)

        ################################################################# tabla de datos
        self.tabla_prestamos = Tabla(['Periodo','Fecha','Cuota fija','Capital','Interes','Saldo'])
        self.tabla_prestamos.setFixedWidth(610)
        self.fr_tabla_prestamos = QFrame()
        self.fr_totales = QFrame()
        self.lay_tabla_datos.addWidget(self.fr_tabla_prestamos)
        self.lay_tabla_datos.addWidget(self.fr_totales)

        self.lay_tabla_totales = QHBoxLayout()
        self.lay_frame_totales = QHBoxLayout()
        self.fr_tabla_prestamos.setLayout(self.lay_tabla_totales)
        self.fr_totales.setLayout(self.lay_frame_totales)

        self.lay_tabla_totales.addWidget(self.tabla_prestamos)
        
        self.capital_total = QLabel ('Capital')
        self.interes_total = QLabel ('Interes')
        self.saldo_total = QLabel ('Saldo')

        self.capital_total_entry = QLineEdit(objectName='especiales')
        self.capital_total_entry.setReadOnly( True)
        self.interes_total_entry = QLineEdit(objectName='especiales')
        self.interes_total_entry.setReadOnly( True)
        self.saldo_total_entry = QLineEdit(objectName='especiales')
        self.saldo_total_entry.setReadOnly( True)


        self.lay_frame_totales.addStretch()
        self.lay_frame_totales.addWidget(self.capital_total)
        self.lay_frame_totales.addWidget(self.capital_total_entry)
        self.lay_frame_totales.addWidget(self.interes_total)
        self.lay_frame_totales.addWidget(self.interes_total_entry)
        self.lay_frame_totales.addWidget(self.saldo_total)
        self.lay_frame_totales.addWidget(self.saldo_total_entry)
        self.lay_frame_totales.addStretch()

        

        

    def orden_oper_ref(self):
        from random import choice
        lista = ('A','B','C','D','E','AA','BB','CC','DD','EE','AB','AC','AD','AE','BA','BC','BD','BE','CA','CB','CD','CE','DA','DB','DE',\
                 'EA','EB','EC','ED','AAA','AAB','AAC','AAD','AAE','ABA','ABB','ABC','ABD','ABE','ACA','ACB','ACC','ACD','ACE','ADA','ADD',\
                 'ADC','ADE','AEA','AEC','AED','AEE')
        lista2 = ('A','B','C','D','E','AA','BB','CC','DD','EE','AB','AC','AD','AE','BA','BC','BD','BE','CA','CB','CD','CE','DA','DB','DE',\
                 'EA','EB','EC','ED','AAA','AAB','AAC','AAD','AAE','ABA','ABB','ABC','ABD','ABE','ACA','ACB','ACC','ACD','ACE','ADA','ADD',\
                 'ADC','ADE','AEA','AEC','AED','AEE','BAA','BBB','BBC','BBD','BBE','BAB','BAC','BAD','BAE','BCA','BCB','BCC','BCD','BCE',\
                    'BDA','BDB','BDC','BDD','BDC','BEA','BEB','BEC','BED','BEE')
        pr= choice(lista2)
        am = choice(lista)
        contar = self.base_datos.contar_item('prestamos')
        for j in contar:
            sumado = j[0] +1
            contado = f'0{sumado}{pr}-{am}'
            self.orden_opera.setText(f'{contado}')

    def tiempo_tipo(self):
        self.nivel = [
                {'tiempo':'dia',
                'periodos':['semanal','quincenal']},
                {'tiempo':'mes',
                'periodos': ['mensual','bimensual','trimestral','semestral']}
                ]
        for item in self.nivel:
            grado = item['tiempo']
            self.tiempo.addItem(grado)

    

    def tipo_pago_dia(self):
        self.tipo_pago.clear()
        for item in self.nivel:
            if item['tiempo']=='dia':
                grupos = item['periodos']
                for grupo in grupos:
                    self.tipo_pago.addItem(grupo)

    def tipo_pago_mes(self):
        self.tipo_pago.clear()
        for item in self.nivel:
            if item['tiempo']=='mes':
                grupos = item['periodos']
                for grupo in grupos:
                    self.tipo_pago.addItem(grupo)
    
    def gestion_tiempos(self):
        tiempo_elegido = self.tiempo.currentText()
        if tiempo_elegido =='dia':
            self.tipo_pago_dia()
        else:
            self.tipo_pago_mes()
    
    def gestion_periodos(self):
        self.periodos_fijos:int
        tipo=self.tipo_pago.currentText()

        if tipo =='semanal':
            self.periodos_fijos=7
        elif tipo =='quincenal':
            self.periodos_fijos=15
        if tipo =='mensual':
            self.periodos_fijos=30
        elif tipo =='bimensual':
            self.periodos_fijos=60
        elif tipo =='trimestral':
            self.periodos_fijos=90
        elif tipo =='semestral':
            self.periodos_fijos=180
        return self.periodos_fijos
    

    def prestamos_otor(self):
        quitado = self.base_datos.suma_element_misma_columna('prestamo','prestamos')
        prestamo_otor = self.prestamos_otor_entry.setText(quitado)
        disponible = int(self.fondos_dispo_entry.text())
        prestar_a = self.prestamo_monto.text()
    
    def amortizar_money(self):
        if self.amortizable.currentText()=='Guineana':
            self.calculo_amortiza()
        else:
            self.calculo_amortiza_const()

    




    def prestar_dinero(self):
        ref_opeacion = self.orden_opera.text()
        nombre = self.nombre.currentText()
        dip = self.dip_pasaporte.text()
        direccion = self.direccion.text()
        telefono = self.telefono.text()
        monto_prestado = self.prestamo_monto.text()
        tasa_interes = self.tasa_interes.text()
        periodos = self.periodos.text()
        fecha_inicio = self.fecha_inicio.text()
        tiempo = self.tiempo.currentText()
        tipo_pago = self.tipo_pago.currentText()
        cuota_mensual = self.cuota_mensual.text()
        intereses_totales = self.intereses_totales.text()
        total_pagar = self.total_pagar.text()
        saldo_total = self.saldo_total_entry.text()
        fecha_hoy = self.fecha.text()
        estado = 'ADEUDADO'
        self.trabajo = ''
        self.banco = ''
   

        tabla_in_bd = json.dumps(self.amortizar)

        self.base_datos.insertar('prestamos','referencia,nombre_prestador,dip_pasaporte,direccion,telefono,prestamo,tasa_interes,periodos,fecha_inicio,tiempo,tipo_pago,cuota_mensual,tabla_amortizacion,intereses_totales,monto_total_pagar,saldo_total,fecha_hoy,estado,trabajo,banco',
                                             (ref_opeacion,nombre,dip,direccion,telefono,monto_prestado,tasa_interes,periodos,fecha_inicio,tiempo,tipo_pago,cuota_mensual,f'{tabla_in_bd}',intereses_totales,total_pagar,saldo_total,fecha_hoy,estado,self.trabajo,self.banco))
        self.orden_oper_ref()

    def limpiar_cajas(self):
        self.nombre.clear()
        self.dip_pasaporte.clear()
        self.direccion.clear()
        self.telefono.clear()
        self.prestamo_monto.clear()
        self.tasa_interes.clear()
        self.periodos.clear()
        self.tiempo.clear()
        self.tipo_pago.clear()
        self.cuota_mensual.clear()
        self.intereses_totales.clear()
        self.total_pagar.clear()
        self.saldo_total_entry.clear()
        self.base_datos.borrar_datos_comp('tabla_amortizar')










    def consultar_list_clientes(self):
        self.nombre.clear()
        self.nombre.setPlaceholderText('Selecione un nombre')
        texto = self.buscar_prestar.text()
        mostrar =MostrarDatos_in(combo=self.nombre )
        mostrar.addDataCombo('nombre_cliente','clientes','nombre_cliente',texto)


    def mostrar_datos_cliente(self):
        filtro = self.nombre.currentText()
        filtrado = self.base_datos
        datos = filtrado.filtro_condicion('identidad,telefono,direccion,trabajo,banco','clientes','nombre_cliente',filtro)
        for identidad,telefono,direccion,trabajo,banco in datos:
            self.dip_pasaporte.setText(identidad)
            self.direccion.setText(direccion)
            self.telefono.setText(telefono)
            self.trabajo = f'{trabajo}'
            self.banco = f'{banco}'
    def calculo_amortiza(self):
        try:
            self.base_datos.borrar_datos_comp('tabla_amortizar')
            monto_prestado = int(self.prestamo_monto.text())
            tasa_interes = float(self.tasa_interes.text())
            periodos = int(self.periodos.text())
            self.amortizar = self.func.amortiza_guinea(monto_prestado,tasa_interes,periodos)
            fecha_inicio = self.fecha_inicio.text()
            fecha = datetime.strptime(f'{fecha_inicio}',"%d/%m/%Y")
            try:
                dias = self.gestion_periodos()
                for i, fila in enumerate(self.amortizar,start=1):
                    fecha = fecha+timedelta(days=dias)
                    real_fecha = fecha.strftime("%d/%m/%Y")
                    periodo = f'{i}'
                    Fecha = real_fecha
                    cuota_fija =  f'{fila["Cuota"]:.2f}'
                    capital = f'{fila["Capital"]:.2f}'
                    interes = f'{fila["Interes"]:.2f}'
                    saldo = f'{fila["Saldo"]:.2f}'
                    self.base_datos.insertar('tabla_amortizar','periodo,fecha,cuota_fija,capital,interes,saldo',(periodo,Fecha,cuota_fija,capital,interes,saldo))
                    self.cuota_mensual.setText(f'{cuota_fija}')
                self.mostrar_tabla_int()
            except Exception:
                self.base_datos.borrar_datos_comp('tabla_amortizar')
                self.mostrar_tabla_int()
        except Exception:
            QMessageBox.warning(self,'ATENCION','Rellene los campos vacios')

    def calculo_amortiza_const(self):
        try:
            self.base_datos.borrar_datos_comp('tabla_amortizar')
            monto_prestado = int(self.prestamo_monto.text())
            tasa_interes = float(self.tasa_interes.text())
            periodos = int(self.periodos.text())
            self.amortizar = self.func.amortizacion(monto_prestado,tasa_interes,periodos)
            fecha_inicio = self.fecha_inicio.text()
            fecha = datetime.strptime(f'{fecha_inicio}',"%d/%m/%Y")
            try:
                dias = self.gestion_periodos()
                for i, fila in enumerate(self.amortizar,start=1):
                    fecha = fecha+timedelta(days=dias)
                    real_fecha = fecha.strftime("%d/%m/%Y")
                    periodo = f'{i}'
                    Fecha = real_fecha
                    cuota_fija =  f'{fila["Cuota"]:.2f}'
                    capital = f'{fila["Capital"]:.2f}'
                    interes = f'{fila["Interes"]:.2f}'
                    saldo = f'{fila["Saldo"]:.2f}'
                    self.base_datos.insertar('tabla_amortizar','periodo,fecha,cuota_fija,capital,interes,saldo',(periodo,Fecha,cuota_fija,capital,interes,saldo))
                    self.cuota_mensual.setText(f'{cuota_fija}')
                self.mostrar_tabla_int()
            except Exception:
                self.base_datos.borrar_datos_comp('tabla_amortizar')
                self.mostrar_tabla_int()
        except Exception:
            QMessageBox.warning(self,'ATENCION','Rellene los campos vacios')


    def mostrar_tabla_int(self):
        tabla = self.tabla_prestamos
        mostrando = MostrarDatos_in(tabla)
        mostrando.addDataTable('periodo,fecha,cuota_fija,capital,interes,saldo','tabla_amortizar')
        interes = self.base_datos.suma_element_misma_columna('interes','tabla_amortizar')
        total_paga = self.base_datos.suma_element_misma_columna('capital','tabla_amortizar')
        #sald = self.base_datos.suma_element_misma_columna('saldo','tabla_amortizar')

        intereses ="{:,}".format(int(interes))
        total_pagar ="{:,}".format(int(total_paga))

        saldo_cal = int(interes) + int(total_paga)
        saldo ="{:,}".format(int(saldo_cal))

        self.intereses_totales.setText(f'{intereses}')
        self.total_pagar.setText(f'{total_pagar}')
        self.saldo_total_entry.setText(f'{saldo}')

        self.interes_total_entry.setText(f'{intereses}')
        self.capital_total_entry.setText(f'{total_pagar}')

        
class ConsultaPrestamo():
    def __init__(self):
        super(ConsultaPrestamo).__init__()
        self.show_prestamo_consulta()
        self.base_datos = Comunicacion()

        
    def show_prestamo_consulta(self):
        self.general_lay = QVBoxLayout()

        fr_top = QFrame()
        main_fr = QFrame()

        self.lay_top_fr = QHBoxLayout()
        self.main_tabla = QVBoxLayout()

        fr_top.setLayout(self.lay_top_fr)
        main_fr.setLayout(self.main_tabla)

        self.general_lay.addWidget(fr_top,5)
        self.general_lay.addWidget(main_fr,95)
        columnas_label = ['Codigo','Nombre','Identificacion','Telefono','Prestamo','Tasa Interes','Periodos','fecha_inicio',\
                    'Mensualidad','Intereses','Deuda Total','fecha_transaccion']

        self.tabla_consulta_hist = Tabla(columnas_label)
        self.main_tabla.addWidget(self.tabla_consulta_hist)

        self.categoria = QComboBox()
        buscar= QLabel('Buscar ')
        self.busq_buscar= QLineEdit()
        self.imprimir_hist= QPushButton(objectName='imprimir')

        categorias = ['referencia','nombre_prestador','trabajo','banco','dip_pasapote','telefono','prestamo','fecha_inicio','cuota_mensual']
        for categoria in categorias:
            self.categoria.addItem(categoria)

        self.lay_top_fr.addWidget(self.categoria)
        self.lay_top_fr.addWidget(buscar)
        self.lay_top_fr.addWidget(self.busq_buscar)
        self.lay_top_fr.addStretch()
        self.lay_top_fr.addWidget(self.imprimir_hist)



    def show_prestamos(self):
        tabla = self.tabla_consulta_hist 
        columnas = 'referencia,nombre_prestador,dip_pasaporte,telefono,prestamo,tasa_interes,periodos,fecha_inicio,cuota_mensual,intereses_totales,saldo_total,fecha_hoy'
        show_tabla = MostrarDatos_in(tabla)
        show_tabla.addDataTable(columnas,'prestamos')


    def show_query(self):
        category = self.categoria.currentText()
        busq_entry= self.busq_buscar.text()
        tabla = self.tabla_consulta_hist 
        columnas = 'referencia,nombre_prestador,dip_pasaporte,telefono,prestamo,tasa_interes,periodos,fecha_inicio,cuota_mensual,intereses_totales,saldo_total,fecha_hoy'
        show_tabla = MostrarDatos_in(tabla)
        show_tabla.addDataTableCondicion(columnas,'prestamos',category,busq_entry)






    
