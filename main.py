
import sys
from PySide6.QtWidgets import QApplication,QMessageBox,QMainWindow,QLineEdit,QLabel,QVBoxLayout,QPushButton,QWidget,QFrame,QFileDialog,QMessageBox

import os
from index import Prestamos
from funcionalidad import Funcionamiento,OPcionesPrestamo,Prestamo,ConsultaPrestamo
from caja import Caja,TablaAmortizacion,ProcesarPagos,EstadoCuotas
from movimientos import Movimientos,Cobros,Cancelaciones,Deudas,Comentarios
from ingresos import VerIngresos
from banco import Banco,Operar
from flotante import Flotante
from clientes import VerClientesDatos,VerClientesPropios
#from operando import OperandoClientes
from bd_prestamos import Comunicacion
from backend import EditarExcel,Impresion,OperacionesMath,MostrarDatos
from otros import UserRegistration,UserPermision,Backups,Settings,UserUpdate
import re, ast

from PySide6.QtWidgets import QMainWindow, QWidget,QVBoxLayout,QFrame,QHBoxLayout,QLabel,QGridLayout,QPushButton,QApplication
from PySide6.QtCore import Qt
import estilos


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.prestar = Prestamos()

        self.funcionar = Funcionamiento()
        #self.op = OperandoClientes()

        self.base_datos = Comunicacion()

       
        self.permisos = []
        self.editar_acceso =  []

        self.operador =None

        try:
            datos_empresa = self.base_datos.mostrar_last_elemento('nombre_empresa,contacto,direccion','empresa','id_empresa')
            for nombre, contacto, direccion in datos_empresa:
                self.nombre_empresa = nombre
                self.contacto_empresa = contacto
                self.direccion_empresa = direccion
        except Exception:
            pass



        
        self.prestar.btn_banco.clicked.connect(self.banca_show_build)
        self.prestar.btn_prestamos.clicked.connect(self.prestamo_show_build)
        self.prestar.btn_clientes.clicked.connect(self.clientes_show_build)
        self.prestar.btn_caja.clicked.connect(self.caja_show_build)
        self.prestar.btn_ingresos.clicked.connect(self.ingresos_show_build)
        self.prestar.btn_movimientos.clicked.connect(self.movimientos_show_build)

        self.prestar.btn_Usuarios.clicked.connect(self.otros_wid)
        self.prestar.btn_Permisos.clicked.connect(self.user_permisos)
        self.prestar.btn_BackUp.clicked.connect(self.back_ups)
        self.prestar.btn_Ajustes.clicked.connect(self.ajustes)

        self.base_datos.crear_columna('clientes','cuenta_bancaria')

        

        #self.funcionar.mostrar_todos.clicked.connect(self.op.mostrar_clientes)

    def imprimir_recaudacion(self):
        file_path=os.path.join('recaudacion.xlsx')
        self.excell = EditarExcel(file_path)


#####################################################################################                  BANCO           ####################
    def banca_show_build(self):
        '''widget principal de banco'''
        permitido ='Banco'
        pase = self.pase_validar(permitido)
        if pase  == 'Permitido':

            self.flota_banck = Flotante(800,600,'Banco')
            self.flota_banck_wid = Banco()
            self.flota_banck.fr_container.setLayout(self.flota_banck_wid.lay_contenedor_banco)
            self.flota_banck_wid.inyection.clicked.connect(self.manejo_capital)

            self.mostrar_int_cap()
            
            self.flota_banck.exec()
        else:
            QMessageBox.information(self.prestar,'ERROR PERMISOS','No tiene permiso para acceder')

    def manejo_capital(self):
        self.capital_banco = Flotante(200,50,'')
        self.ventana_capital = Operar()


        self.capital_banco.fr_container.setLayout(self.ventana_capital.main_root)
        self.ventana_capital.btn_guardar.clicked.connect(self.guardar_banco)
        

        self.capital_banco.exec()
            


    def guardar_banco(self):
        fecha =self.ventana_capital.fecha_banco.text()
        detalle = self.ventana_capital.detalles.currentText()
        deposito = self.ventana_capital.deposito_banco.text()
        retiros = self.ventana_capital.retiros_banco.text()

        retiro_nulo = 0
        capital_nulo = 0

        if detalle =='Capital Inicial':
            self.base_datos.insertar('tabla_banco','fecha,detalle,deposito,retiro,operador',(fecha,detalle,deposito,retiro_nulo,self.operador))
        elif detalle =='Más Capital':
            self.base_datos.insertar('tabla_banco','fecha,detalle,deposito,retiro,operador',(fecha,detalle,deposito,retiro_nulo,self.operador))
        else:
            self.base_datos.insertar('tabla_banco','fecha,detalle,deposito,retiro,operador',(fecha,detalle,capital_nulo,retiros,self.operador))
        self.ventana_capital.detalles.clear()
        self.ventana_capital.deposito_banco.clear()
        self.ventana_capital.retiros_banco.clear()
        self.capital_banco.close()
        self.flota_banck_wid.show_tabla_bank()



        #self.flota_banck.banca_show()





#######################################################################################                PRESTAMOS            ##################
    def prestamo_show_build(self):
        '''esta es la pequeña ventana que se abre para ver las opciones que tienes
        ver el historial de los prestamos o hacer un prestamo'''
        self.agregar_ver = Flotante(200,30,'')
        self.prestamo = OPcionesPrestamo()
        self.prestamo.btn_nuevo.clicked.connect(self.prestamo_win)
        self.prestamo.btn_consultar.clicked.connect(self.consulta_prest)

        self.agregar_ver.titulo.hide()



        self.agregar_ver.fr_container.setLayout(self.prestamo.layout_main)
        self.agregar_ver.exec()

    def prestamo_win(self):
        '''Ventana de los prestamos, donde se realiza y procesa los prestamos para los clientes'''
        permitido ='Prestamo'
        pase = self.pase_validar(permitido)
        if pase  == 'Permitido':
            (self.operador)

            self.agregar_ver.close()
            self.presta_wid = Flotante(900,700,'PRESTAMOS')
            self.prestando=Prestamo()

            self.presta_wid.fr_container.setLayout(self.prestando.lay_general)
            self.fondos_dis()

            self.prestando.prestamo_monto.editingFinished.connect(self.sumar_fondos)
            
            self.prestando.btn_save_info.clicked.connect(self.guardar_info)
            self.prestando.btn_back.clicked.connect(self.prestando.limpiar_cajas)


            self.presta_wid.exec()
        else:
            QMessageBox.information(self.agregar_ver,'ERROR PERMISOS','No tiene permiso para acceder')

    def fondos_dis(self):

        total_deposito_f = self.base_datos.suma_element_misma_columna('deposito','tabla_banco')
        quitado_f = self.base_datos.suma_element_misma_columna('prestamo','prestamos')
        try:
            if total_deposito_f == None:
                total_deposito=0
                quitado=0
                restar = OperacionesMath(total_deposito,quitado)
                resultado = restar.resta()
                self.prestando.fondos_dispo_entry.setText(f'{"{:,}".format(int(resultado))}')
                self.prestando.prestamos_otor_entry.setText(f'{"{:,}".format(int(quitado))}')
            else:
                total_deposito = int(total_deposito_f)
                quitado = int(quitado_f)
                restar = OperacionesMath(total_deposito,quitado)
                resultado = restar.resta()
                self.prestando.fondos_dispo_entry.setText(f'{"{:,}".format(int(resultado))}')
                self.prestando.prestamos_otor_entry.setText(f'{"{:,}".format(int(quitado_f))}')
        except Exception as e:
            print(f'Error : {e}')
            total_deposito_f = self.base_datos.suma_element_misma_columna('deposito','tabla_banco')
            self.prestando.fondos_dispo_entry.setText(f'{"{:,}".format(int(total_deposito_f))}')

    def calculo_saldo(self):
        quitado_cal = self.base_datos.suma_element_misma_columna('prestamo','prestamos')
        try:
            if quitado_cal == None:
                quitado = 0
                monto_prestar = 0
                sumar = OperacionesMath(int(quitado),int(monto_prestar))
                resultado = sumar.suma()
                self.prestando.prestamos_otor_entry.setText(f'{"{:,}".format(int(resultado))}')
            else:
                quitado = quitado_cal
                monto_prestar = int(self.prestando.prestamo_monto.text())
                sumar = OperacionesMath(int(quitado),int(monto_prestar))
                resultado = sumar.suma()
                self.prestando.prestamos_otor_entry.setText(f'{"{:,}".format(int(resultado))}')
        except Exception:
            monto_prestar = int(self.prestando.prestamo_monto.text())
            self.prestando.prestamos_otor_entry.setText(f'{"{:,}".format(int(monto_prestar))}')


    def nuevo_disp(self):
        total_deposito = self.base_datos.suma_element_misma_columna('deposito','tabla_banco')
        if total_deposito ==None:
            total_deposito=0
            nuevo_otor=0
            restar = OperacionesMath(total_deposito,int(nuevo_otor))
            result = restar.resta()
            self.prestando.fondos_dispo_entry.setText(f'{"{:,}".format(int(result))}')
        else:
            total_deposito = int(total_deposito)
            otorgados = self.prestando.prestamos_otor_entry.text()
            nuevo_otor =otorgados.replace(',','')

            restar = OperacionesMath(total_deposito,int(nuevo_otor))
            result = restar.resta()
            self.prestando.fondos_dispo_entry.setText(f'{"{:,}".format(int(result))}')

    def sumar_fondos(self):
        try:
            if (self.prestando.prestamo_monto.text())=='':
                self.fondos_dis()
            else:
                self.calculo_saldo()
                self.nuevo_disp()
                self.disponiblidad()
        except ValueError:
            pass
            #self.nuevo_disp()
        

    def disponiblidad(self):
        otorgados = self.prestando.prestamos_otor_entry.text()
        monto_prestar = self.prestando.fondos_dispo_entry.text()
        nuevo_otor =otorgados.replace(',','')
        nuevo_disp =monto_prestar.replace(',','')
        nuevo_disp=int(nuevo_disp)
        nuevo_otor=int(nuevo_otor)
        disponible = int(self.prestando.fondos_dispo_entry.text())
        print(disponible)
        try:
            if  disponible == 0:
                QMessageBox.warning(self.presta_wid,'ATENCION','Se quedaría sin "Fondos')
            elif disponible < 0:
                QMessageBox.warning(self.presta_wid,'ATENCION','No dispone de suficiente dinero para esta operacion')
        except Exception:
            pass

        



    


    def consulta_prest(self):
        self.agregar_ver.close()
        self.cons_prestamos = Flotante(1000,600,'CONSULTAR HISTORIAL')
        self.consulta = ConsultaPrestamo()
        self.cons_prestamos.fr_container.setLayout(self.consulta.general_lay)

        self.consulta.categoria.currentTextChanged.connect(self.buscando)
        self.consulta.busq_buscar.textChanged.connect(self.buscando)

        self.consulta.imprimir_hist.clicked.connect(self.imprimir_consultas_pr)

        self.consulta.show_prestamos()

        self.cons_prestamos.exec()

    def buscando(self):
        self.consulta.show_query()

    def guardar_info(self):
        nombre = self.prestando.nombre.currentText()
        tipo_pago = self.prestando.tipo_pago.currentText()
        monto= self.prestando.capital_total_entry.text()
        saldo = self.prestando.saldo_total_entry.text()
        phone = self.prestando.telefono.text()

        sobrado = Cobros()
        sobrado.guardar_cobradores(nombre,tipo_pago,monto,saldo,phone)
        self.prestando.prestar_dinero()
        self.imprimir_prestamo()
        self.prestando.limpiar_cajas()

    def imprimir_consultas_pr(self):
        file_path=os.path.join('prestamo_consulta.xlsx')
        self.excell = EditarExcel(file_path)

        
        categoria= self.consulta.categoria.currentText()
        buscar= self.consulta.busq_buscar.text()
        
            
            

        self.excell.add_imagen('imagen_recuperada.png','B2')
        self.excell.actualizar_celda('D3',self.nombre_empresa)
        self.excell.actualizar_celda('D4',self.contacto_empresa)
        self.excell.actualizar_celda('F4',self.direccion_empresa)

        self.excell.actualizar_celda('H8',categoria)
        self.excell.actualizar_celda('I8',buscar)

        start_fila=11
        start_column=2
        self.excell.limpiar_filas('B11','M31')
        columnas = 'referencia,nombre_prestador,dip_pasaporte,telefono,prestamo,tasa_interes,periodos,fecha_inicio,cuota_mensual,intereses_totales,saldo_total,fecha_hoy'
        query= self.base_datos.filtro_condicion(columnas,'prestamos',categoria,buscar)
        self.excell.add_tupla_column(query,start_row=start_fila,start_col=start_column)

        self.excell.save()
        self.impresion = Impresion('prestamo_consulta')
        self.impresion.imprimir()



    def imprimir_prestamo(self):
        
        file_path=os.path.join('prestamo.xlsx')
        #pdf_path=os.path.join('prestamo.pdf')
        
        self.excell = EditarExcel(file_path)

        nombre = self.prestando.nombre.currentText()
        direccion = self.prestando.direccion.text()
        telefono = self.prestando.telefono.text()
        operacion = self.prestando.orden_opera.text()
        identificacion = self.prestando.dip_pasaporte.text()
        tipo_pago = self.prestando.tipo_pago.currentText()
        prestamo_monto = self.prestando.prestamo_monto.text()
        tasa_interes = self.prestando.tasa_interes.text()
        periodos = self.prestando.periodos.text()
        cuota_mensual = self.prestando.cuota_mensual.text()
        int_totales = self.prestando.intereses_totales.text()
        total_pagar = self.prestando.total_pagar.text()
        fecha_inicio = self.prestando.fecha_inicio.text()
        fecha_hoy = self.prestando.fecha.text()
        capital_t = self.prestando.capital_total_entry.text()
        interes_t = self.prestando.interes_total_entry.text()
        saldo_t = self.prestando.saldo_total_entry.text()

        query = self.base_datos.mostrar_datos('periodo,fecha,cuota_fija,capital,interes,saldo','tabla_amortizar')
        start_fila=19
        start_column=2
        self.excell.add_imagen('imagen_recuperada.png','B3')
        self.excell.limpiar_filas('B19','G39')
        self.excell.add_tupla_column(query,start_row=start_fila,start_col=start_column)

        self.excell.actualizar_celda('D3',self.nombre_empresa)
        self.excell.actualizar_celda('D4',self.contacto_empresa)
        self.excell.actualizar_celda('F4',self.direccion_empresa)

        self.excell.actualizar_celda('C7',nombre)
        self.excell.actualizar_celda('C8',direccion)
        self.excell.actualizar_celda('F7',telefono)
        self.excell.actualizar_celda('F8',identificacion)
        self.excell.actualizar_celda('C12',prestamo_monto)
        self.excell.actualizar_celda('C13',f'{tasa_interes} %')
        self.excell.actualizar_celda('C14',periodos)
        self.excell.actualizar_celda('E12',operacion)
        self.excell.actualizar_celda('E13',fecha_hoy)
        self.excell.actualizar_celda('E14',fecha_inicio)
        self.excell.actualizar_celda('E15',tipo_pago)
        self.excell.actualizar_celda('G12',total_pagar)
        self.excell.actualizar_celda('G13',cuota_mensual)
        self.excell.actualizar_celda('G14',int_totales)

        self.excell.actualizar_celda('C41',capital_t)
        self.excell.actualizar_celda('E41',interes_t)
        self.excell.actualizar_celda('G41',saldo_t)
        self.excell.actualizar_celda('B46',self.operador)



        self.excell.save()
        self.impresion = Impresion('prestamo')
        self.impresion.imprimir()
        #self.impresion.guardar_pdf(file_path,pdf_path)










######################################################################################                CLIENTES            ###################
    def clientes_show_build(self):
        '''tener a todos los clientes, seleccionar a los clientes y poder trabajar con ellos'''
        permitido ='Clientes'
        pase = self.pase_validar(permitido)
        if pase  == 'Permitido':
            self.clientes_wid = Flotante(800,400,'CLIENTES')
            self.cliente = VerClientesDatos()
            
            self.cliente.buscar_clientes.clicked.connect(self.view_clientes)
            self.cliente.actualizar_cliente.clicked.connect(self.act_clientes)
            self.cliente.borrar_cliente.clicked.connect(self.borrar_cliente)

            self.clientes_wid.fr_container.setLayout(self.cliente.general_clientes)

            self.clientes_wid.exec()
        else:
            QMessageBox.information(self.prestar,'ERROR PERMISOS','No tiene permiso para acceder')

    def view_clientes(self):
        self.ver_cliente = Flotante(600,400,'Lista de Clientes')
        self.clientes_propios = VerClientesPropios()

        self.ver_cliente.fr_container.setLayout(self.clientes_propios.general_clientes)
        self.clientes_propios.tabla_clientes_view.doubleClicked.connect(self.poner_datos_clientes)


        self.ver_cliente.exec()
    
    def poner_datos_clientes(self):
        datos = self.clientes_propios.select_item()
        for id_client,nombre,identidad,correo,telefono,direccion,observacion,nom_ref,telefo_ref,relacion,trabajo,banco,cuenta in datos:
            self.cliente.nombre_cliente.setText(nombre)
            self.cliente.doc_identidad.setText(identidad)
            self.cliente.id_cliente.setText(f'{id_client}')
            self.cliente.correo_cliente.setText(correo)
            self.cliente.telefono_cliente.setText(f'{telefono}')
            self.cliente.direccion_cliente.setText(direccion)
            self.cliente.observaciones.setPlainText(observacion)
            self.cliente.nombre_ref.setText(nom_ref)
            self.cliente.telefono_ref.setText(f'{telefo_ref}')
            self.cliente.relacion_ref.setText(relacion)
            self.cliente.trabajo_ed.setText(trabajo)
            self.cliente.banco_ed.setText(banco)
            self.cliente.cuenta_banca.setText(cuenta)
        
        self.ver_cliente.close()

    def act_clientes(self):
        nombre = self.cliente.nombre_cliente.text()
        identidad= self.cliente.doc_identidad.text()
        id_cliente = self.cliente.id_cliente.text()
        correo = self.cliente.correo_cliente.text()
        telefono = self.cliente.telefono_cliente.text()
        direccion = self.cliente.direccion_cliente.text()
        Observaciones = self.cliente.observaciones.toPlainText()
        ref_cliente = self.cliente.nombre_ref.text()
        ref_telefono = self.cliente.telefono_ref.text()
        relacion_ref = self.cliente.relacion_ref.text()
        trabajo = self.cliente.trabajo_ed.text()
        banco = self.cliente.banco_ed.text()
        datos = f'nombre_cliente="{nombre}",identidad="{identidad}",correo="{correo}",telefono="{telefono}",direccion="{direccion}",observacion="{Observaciones}",nombre_referencia="{ref_cliente}",telefono_referencia=""{ref_telefono},relacion="{relacion_ref}",trabajo="{trabajo}",banco="{banco}"'
        self.base_datos.update_multiple('clientes',datos,'id_cliente',id_cliente)
        self.cliente.limpiar_campos_client()

    def borrar_cliente(self):
        id_cliente = self.cliente.id_cliente.text()
        self.base_datos.borrar_fila('clientes','id_cliente',id_cliente)
        self.cliente.limpiar_campos_client()





    


#########################################################################################          CAJA          ################
    def caja_show_build(self):
        '''esta es la construccion de la caja de entrada y salidas de dinero'''
        permitido ='Caja'
        pase = self.pase_validar(permitido)
        if pase  == 'Permitido':
        
            self.caja_wid = Flotante(900,600,'CAJA')
            self.caja = Caja()

            self.caja_wid.fr_container.setLayout(self.caja.general_caja)
            self.caja.procesar_btn.clicked.connect(self.ejc_procesar_pagos)
            self.caja.btn_tabla_amort.clicked.connect(self.tabla_amortizacion)
            self.caja.btn_estado_cuotas.clicked.connect(self.estado_cuotas)


            self.caja_wid.exec()
        else:
            QMessageBox.information(self.prestar,'ERROR PERMISOS','No tiene permiso para acceder')

    def ejc_procesar_pagos(self):
        try:
            if self.caja.num_orden.text() =='':
                QMessageBox.warning(self.caja_wid,'ERROR','Porfavor una la transaccion')
            else:
                if self.caja.estado_caja.text()=='CANCELADO':
                    QMessageBox.warning(self.caja_wid,'ERROR','Operacion "CANCELADA"')
                else:
                    self.procesar_pagos()
        except Exception:
            QMessageBox.warning(self.prestar,'ERROR','Porfavor seleccione la transaccion')


    def procesar_pagos(self):
        self.procesando = Flotante(100,150,'')
        self.procesando.titulo.hide()

        self.procesar = ProcesarPagos()
        self.procesando.fr_container.setLayout(self.procesar.procesar_lay)
        self.procesar.interes_proces.setText('0')
        self.procesar.capit_proces.setText('0')


        self.procesar.capit_proces.textChanged.connect(self.control_error)
        self.procesar.interes_proces.textChanged.connect(self.control_error)
        self.procesar.confirmar.clicked.connect(self.procesando_pago)
        self.procesando.exec()
        
    def control_error(self):
        self.procesar.interes_proces.text()
        try:
            interes = int(self.procesar.interes_proces.text())
            capital = int(self.procesar.capit_proces.text())
            resultado = self.procesar.small_oper(interes,capital)
            self.procesar.saldo_edit.setText(f'{resultado}')
        except Exception:
            interes = 0
            capital = 0
            resultado = self.procesar.small_oper(interes,capital)
            self.procesar.saldo_edit.setText(f'{resultado}')



    def tabla_amortizacion(self):
        self.tabla_amor_view = Flotante(600,400,'TABLA AMORTIZACION')
        self.tabal_amr= TablaAmortizacion()
        self.tabla_amor_view.fr_container.setLayout(self.tabal_amr.general_lay)

        self.ejecutar_ref()

        self.tabla_amor_view.exec()


    def ejecutar_ref(self):
        referen = self.caja.num_orden.text()
        self.tabal_amr.mostrar_tabla_amort(referen)
    
    def mostrar_int_cap(self):
        self.flota_banck_wid.ver_capital()
        self.flota_banck_wid.ver_interes()
        self.flota_banck_wid.ver_recargos()

        

    

    def procesando_pago(self):
        
        fecha = self.caja.fecha_hoy.text()
        cliente = self.caja.nombre_caja_cliente.text()
        cuota = self.procesar.detalle.currentText()
        cappital = self.procesar.capit_proces.text()
        interes = self.procesar.interes_proces.text()
        recargos = self.procesar.recargos_proces.text()
        pagado = self.procesar.saldo_edit.text()
        ref = self.caja.num_orden.text()
        operador = self.operador
        deuda_total = self.caja.monto_total_caja.text()
        deuda_total = deuda_total.replace(',','')

        total_pagado = self.caja.pagado()
        print(total_pagado)
        total_pagado = total_pagado + int(pagado)
        pagado_total = total_pagado
        deuda_total=int(deuda_total)
        pagado_total = int(pagado_total)
        restar = OperacionesMath(deuda_total,pagado_total)
        pendiente = restar.resta()
        print(f'pendiente: {pendiente}')
        values = (fecha,cliente,cuota,cappital,interes,recargos,ref,pagado,operador,deuda_total,pagado_total,pendiente)
        self.base_datos.insertar('procesando_pago','fecha,cliente_name,detalle,capital,interes,recargo,ref,pagado,operador,deuda_total,total_pago,pendiente',values)
        if pendiente <=0:
            self.base_datos.update('prestamos','estado','CANCELADO','referencia',ref)
            self.base_datos.update('prestamos','fecha_cancelacion',fecha,'referencia',ref)
            self.caja.estado_caja.clear()
            self.caja.estado_caja.setText(f'CANCELADO')
        
        self.caja.show_operate_clients()
        self.procesando.close()

    
        #self.mostrar_int_cap()

    def estado_cuotas(self):
        self.cuota_flot = Flotante(700,400,'ESTADO de CUOTAS')
        self.cuota_wid= EstadoCuotas()
        self.cuota_flot.fr_container.setLayout(self.cuota_wid.cuota_greal)
        ref=self.caja.num_orden.text()

        self.cuota_wid.btn_printer.clicked.connect(self.imprimir_estados)

        self.cuota_wid.show_estado(ref)
        self.cuota_wid.datos_persona(ref)

        self.cuota_flot.exec()


    def imprimir_estados(self):
        ref=self.caja.num_orden.text()
        file_path=os.path.join('estado_cuotas.xlsx')
        self.excell = EditarExcel(file_path)


        columnas = 'ref,fecha,detalle,capital,interes,recargo,pagado,pendiente'
        query = self.base_datos.filtro_condicion(columnas,'procesando_pago','ref',ref)
        start_fila=21
        start_column=1
        self.excell.limpiar_filas('A21','H36')
        self.excell.add_tupla_column(query,start_row=start_fila,start_col=start_column)

        columnas = 'nombre_prestador,direccion,telefono,dip_pasaporte,prestamo,tasa_interes,periodos,referencia,fecha_hoy,fecha_inicio,saldo_total,cuota_mensual,intereses_totales,estado'
        datos = self.base_datos.filtro_condicion(columnas,'prestamos','referencia',ref)
        for nombre,direccion,telefono,dip,monto,tasa,periodo,referencia,fecha,fecha_inicio,saldo,cuotas,interes_total,estado in datos:
            
            self.excell.add_imagen('imagen_recuperada.png','B2')

            self.excell.actualizar_celda('D3',self.nombre_empresa)
            self.excell.actualizar_celda('D4',self.contacto_empresa)
            self.excell.actualizar_celda('F4',self.direccion_empresa)

            self.excell.actualizar_celda('C8',nombre)
            self.excell.actualizar_celda('C9',direccion)
            self.excell.actualizar_celda('F8',telefono)
            self.excell.actualizar_celda('F9',dip)
            self.excell.actualizar_celda('C13',monto)
            self.excell.actualizar_celda('C14',tasa)
            self.excell.actualizar_celda('C15',periodo)
            self.excell.actualizar_celda('E13',referencia)
            self.excell.actualizar_celda('E14',fecha)
            self.excell.actualizar_celda('E15',fecha_inicio)
            self.excell.actualizar_celda('G13',saldo)
            self.excell.actualizar_celda('G14',cuotas)
            self.excell.actualizar_celda('G15',interes_total)
            self.excell.actualizar_celda('E16',estado)
            #self.excell.actualizar_celda('G38',saldo_t)

        deuda_pendiente = self.base_datos.mostrar_un_elemento('pendiente','procesando_pago','ref',ref,'id_pago_cliente')
        for cantidad in deuda_pendiente:
            self.excell.actualizar_celda('G38',cantidad[0])
        self.excell.save()
        self.impresion = Impresion('estado_cuotas')
        self.impresion.imprimir()



        


    

        



#####################################################################################          INGRESOS          ####################
    def ingresos_show_build(self):
        '''aqui se controlan los ingresos de la empresa'''
        permitido ='Ingresos'
        pase = self.pase_validar(permitido)
        if pase  == 'Permitido':
       
            self.ingre = Flotante(800,600,'INGRESOS')

            self.caja_ingr = VerIngresos()

            self.ingre.fr_container.setLayout(self.caja_ingr.general_ingresos)
            
            self.caja_ingr.fecha_busqueda.dateTimeChanged.connect(self.busqueda_fecha)
            self.caja_ingr.printer.clicked.connect(self.imprimir_ingresos)

            self.ingre.exec()
        else:
            QMessageBox.information(self.prestar,'ERROR PERMISOS','No tiene permiso para acceder')

    def busqueda(self):
        self.caja_ingr.filtro_meses()

    def busqueda_fecha(self):
        self.caja_ingr.filtro_fecha()


    def imprimir_ingresos(self):
        file_path=os.path.join('ingresos.xlsx')
        self.excell = EditarExcel(file_path)

        fecha_mes = self.caja_ingr.datos_fecha()
        fecha_hoy = self.caja_ingr.fecha_busqueda.text()

        mes = self.caja_ingr.buscar_mes_ingr.currentText()
        año = self.caja_ingr.buscar_año_ingr.currentText()
        print(f'año {año}')

        columnas = 'fecha,ref,cliente_name,detalle,capital,interes,recargo'
        self.excell.limpiar_filas('F6','G6')

        if año  == '':
            query = self.base_datos.filtro_condicion(columnas,'procesando_pago','fecha',fecha_hoy)
            self.excell.actualizar_celda('D3',self.nombre_empresa)
            self.excell.actualizar_celda('D4',self.contacto_empresa)
            self.excell.actualizar_celda('F4',self.direccion_empresa)
            self.excell.actualizar_celda('F6',fecha_hoy)
            self.excell.actualizar_celda('D32',self.operador)
           
        else:
            
            query= self.base_datos.filtro_condicion(columnas,'procesando_pago','fecha',fecha_mes)
            self.excell.actualizar_celda('F6',mes)
            self.excell.actualizar_celda('G6',año)
            self.excell.actualizar_celda('D3',self.nombre_empresa)
            self.excell.actualizar_celda('D4',self.contacto_empresa)
            self.excell.actualizar_celda('F4',self.direccion_empresa)
            self.excell.actualizar_celda('D32',self.operador)

        print(query)
        self.excell.add_imagen('imagen_recuperada.png','B3')
        start_fila=9
        start_column=2
        self.excell.limpiar_filas('B9','G32')
        self.excell.add_tupla_column(query,start_row=start_fila,start_col=start_column)
        self.excell.save()

       
        self.impresion = Impresion('ingresos')
        self.impresion.imprimir()



######################################################################################          MOVIMIENTOS         ###################
    def movimientos_show_build(self):

        '''conrtol de las operaciones'''
        permitido ='Movimientos'
        pase = self.pase_validar(permitido)
        if pase  == 'Permitido':
       
            self.movimiento_wid = Flotante(800,600,'MOVIMIENTOS')
            self.movimientos = Movimientos()

            self.movimiento_wid.fr_container.setLayout(self.movimientos.general_move)
            self.cobros_gestion()
            self.movimientos.btn_cobros.clicked.connect(self.cobros_gestion)
            self.movimientos.inf_cancelados.clicked.connect(self.cobros_cancelados)
            self.movimientos.endeudados.clicked.connect(self.deudas)



            self.movimiento_wid.exec()
        else:
            QMessageBox.information(self.prestar,'ERROR PERMISOS','No tiene permiso para acceder')

    def cobros_gestion(self):
        self.cobro_win = Cobros()
        self.movimientos.layout_main.setCurrentIndex(0) 

        self.cobro_win.buscando_cobros.textChanged.connect(self.cobro_win.show_cobros)
        self.cobro_win.tabla_cobros.doubleClicked.connect(self.selec_cobro)
        self.cobro_win.printr.clicked.connect(self.imprimir_cobros)
        self.cobro_win.show_cobros_all()

        self.movimientos.cobros.setLayout(self.cobro_win.main_layout)


    def observaciones(self):
        '''comentar brevemente las dificultades al tratar de cobrar el dinero'''

        self.cuadro = Flotante(250,350,'Observaciones')
        self.comment = Comentarios()

        self.cuadro.fr_container.setLayout(self.comment.lay_gral)

        self.comment.btn_update.clicked.connect(self.update_comment)
        self.fijar_texto()
        self.cuadro.exec()

    
    def selec_cobro(self):
        datos = self.cobro_win.select_item()
        self.id_coment = datos
        self.observaciones()

    def fijar_texto(self):
        datos = self.id_coment
        self.datos=self.base_datos.filtro_condicion('observaciones','cobros','id_cobros',datos)
        for texto in self.datos:
            self.comment.texto.setPlainText(f'{texto[0]}')


    def update_comment(self):
        id_cobro = self.id_coment
        self.comment.actualizar_comment(id_cobro)

        self.cuadro.close()

    def cobros_cancelados(self):
        self.cancel_win = Cancelaciones()
        self.movimientos.layout_main.setCurrentIndex(1) 

        self.movimientos.cancel.setLayout(self.cancel_win.main_layout)

        self.cancel_win.show_cancelaciones()

        self.cancel_win.buscando_cancel.textChanged.connect(self.cancel_win.sow_cancel_filter)
        self.cancel_win.printer.clicked.connect(self.imprimir_cancelados)



    def deudas(self):
        self.deudas_win = Deudas()
        self.movimientos.layout_main.setCurrentIndex(2) 

        self.movimientos.deudas.setLayout(self.deudas_win.main_layout)
        self.deudas_win.show_deudas()        
        self.deudas_win.buscando_deudas.textChanged.connect(self.deudas_win.sow_deudas_filter)
        self.deudas_win.printr.clicked.connect(self.imprimir_deudas)




    def imprimir_deudas(self):
        file_path=os.path.join('otras_operaciones.xlsx')
        self.excell = EditarExcel(file_path)

        buscar= self.deudas_win.buscando_deudas.text()
        columnas = 'id_prestamos,nombre_prestador,prestamo,fecha_inicio,tasa_interes,saldo_total'

        if len(buscar)==0:
            query = self.base_datos.filtro_condicion(columnas,'prestamos','estado','ADEUDADO')
        else:
            query= self.base_datos.filtro_condicion_date(columnas,'prestamos','estado','ADEUDADO','nombre_prestador',buscar,'','')
        self.excell.add_imagen('imagen_recuperada.png','B3')
        self.excell.actualizar_celda('D6','DEUDAS ACTIVAS')
        self.excell.actualizar_celda('D3',self.nombre_empresa)
        self.excell.actualizar_celda('D4',self.contacto_empresa)
        self.excell.actualizar_celda('F4',self.direccion_empresa)
        self.excell.actualizar_celda('E43',self.operador)


        start_fila=9
        start_column=2
        self.excell.limpiar_filas('B9','G40')
        self.excell.add_tupla_column(query,start_row=start_fila,start_col=start_column)
        self.excell.save()
        self.impresion = Impresion('otras_operaciones')
        self.impresion.imprimir()


    def imprimir_cobros(self):
        file_path=os.path.join('cobros.xlsx')
        self.excell = EditarExcel(file_path)


        buscar= self.cobro_win.buscando_cobros.text()
        columnas = 'id_cobros,nombre,modo_pago,monto,saldo,telefono,observaciones'
        
        if len(buscar)==0:
            query = self.base_datos.mostrar_datos(columnas,'cobros')
        else:
            query= self.base_datos.filtro_condicion(columnas,'cobros','nombre',buscar)
            

        self.excell.add_imagen('imagen_recuperada.png','B2')
        self.excell.actualizar_celda('D3',self.nombre_empresa)
        self.excell.actualizar_celda('D4',self.contacto_empresa)
        self.excell.actualizar_celda('F4',self.direccion_empresa)


        self.excell.actualizar_celda('E29',self.operador)

        start_fila=8
        start_column=2
        self.excell.limpiar_filas('B8','H26')
        self.excell.add_tupla_column(query,start_row=start_fila,start_col=start_column)

        self.excell.save()
        self.impresion = Impresion('cobros')
        self.impresion.imprimir()


    def imprimir_cancelados(self):
        file_path=os.path.join('otras_operaciones.xlsx')
        self.excell = EditarExcel(file_path)

        buscar = self.cancel_win.buscando_cancel.text()
        columnas = 'id_prestamos,nombre_prestador,prestamo,fecha_inicio,tasa_interes,saldo_total'

        if len(buscar)==0:
            query = self.base_datos.filtro_condicion(columnas,'prestamos','estado','CANCELADO')
        else:
            query= self.base_datos.filtro_condicion_date(columnas,'prestamos','estado','CANCELADO','nombre_prestador',buscar,'','')
        self.excell.add_imagen('imagen_recuperada.png','B3')
        self.excell.actualizar_celda('D6','DEUDAS CANCELADAS')
        self.excell.actualizar_celda('D3',self.nombre_empresa)
        self.excell.actualizar_celda('D4',self.contacto_empresa)
        self.excell.actualizar_celda('F4',self.direccion_empresa)
        self.excell.actualizar_celda('E43',self.operador)


        start_fila=9
        start_column=2
        self.excell.limpiar_filas('B9','F40')
        
        self.excell.add_tupla_column(query,start_row=start_fila,start_col=start_column)
        self.excell.save()
        self.impresion = Impresion('otras_operaciones')
        self.impresion.imprimir()

    ############################################################################################################    otros

    def otros_wid(self):

        self.user_window = Flotante(250,300,'REGISTRO DE USUARIOS')
        self.users_reg = UserRegistration()

        self.user_window.fr_container.setLayout(self.users_reg.general_layout)
        self.user_window.titulo.hide()

        self.users_reg.btn_save_user.clicked.connect(self.guardando_users)
    
        self.user_window.exec()

    def guardando_users(self):
        nombre = self.users_reg.nombre_compl_entry.text()
        user_name = self.users_reg.nom_user_entry.text()
        password = self.users_reg.contraseña_entry.text()
        telefono = self.users_reg.telefono_entry.text()
        try:
            if len(nombre) >0 and len(user_name) >0 and len(password)>0 and len(telefono)>0: 
                self.users_reg.guardar_usuario()
                self.users_reg.limpiar_cajas()
                QMessageBox.information(self.user_window,'Informacion','Guardado con Exito!!!')
            else:
                QMessageBox.information(self.user_window,'Informacion','Porfavor rellene los campos Obligatorios')
        except :
            QMessageBox.warning(self.user_window,'ERROR','Existe un error que no puedo identificar con la base de datos')
        
    def user_permisos(self):
        permitido ='Permisos'
        pase = self.pase_validar(permitido)
        if pase  == 'Permitido':
        
            self.permision_window = Flotante(400,200,'')
            self.users_permit = UserPermision()

            self.permision_window.fr_container.setLayout(self.users_permit.general_layout)
            self.permision_window.titulo.hide()
            self.users_permit.prestamo_chk.stateChanged.connect(lambda: self.actualizar_lista(self.users_permit.prestamo_chk))
            self.users_permit.clientes_chk.stateChanged.connect(lambda: self.actualizar_lista(self.users_permit.clientes_chk))
            self.users_permit.caja_chk.stateChanged.connect(lambda: self.actualizar_lista(self.users_permit.caja_chk))
            self.users_permit.ingresos_chk.stateChanged.connect(lambda: self.actualizar_lista(self.users_permit.ingresos_chk))
            self.users_permit.banco_chk.stateChanged.connect(lambda: self.actualizar_lista(self.users_permit.banco_chk))
            self.users_permit.movimiento_chk.stateChanged.connect(lambda: self.actualizar_lista(self.users_permit.movimiento_chk))
            self.users_permit.config_chk.stateChanged.connect(lambda: self.actualizar_lista(self.users_permit.config_chk))
            self.users_permit.backup_chk.stateChanged.connect(lambda: self.actualizar_lista(self.users_permit.backup_chk))
            self.users_permit.permisos_chk.stateChanged.connect(lambda: self.actualizar_lista(self.users_permit.permisos_chk))
            self.users_permit.btn_aceptar.clicked.connect(self.aceptar_permisos)

            datos  = MostrarDatos(' nombre','users')
            datos.addDataCombo(self.users_permit.filtro_busqueda)

            self.users_permit.filtro_busqueda.textActivated.connect(self.filtro_user)
            self.users_permit.btn_aceptar.clicked.connect(self.aceptar_permisos)
            self.users_permit.btn_ver_user.clicked.connect(self.ver_user)
            



            self.permision_window.exec()
        else:
            QMessageBox.information(self.prestar,'ERROR PERMISOS','No tiene permiso para acceder')


    def ver_user(self):
        self.user_view = Flotante(250,300,'')
        self.users_view_win = UserUpdate()
        self.user_view.fr_container.setLayout(self.users_view_win.general_layout)

        self.users_view_win.btn_update_user.clicked.connect(self.act_persona)
        id_users =self.users_permit.line_id.text()
        campos = 'nombre,correo,user_name,passwd,telefono,pasport,domicilio'
        registro = self.base_datos.mostrar_condicion(campos,'users','id_users',id_users)

        for nombre,correo,user_name,pasword,telefono,pasport,domicilio in registro:
                    
            self.users_view_win.nombre_compl_entry.setText(f'{nombre}')
            self.users_view_win.correo_entry.setText(f'{correo}')
            self.users_view_win.nom_user_entry.setText(f'{user_name}')
            self.users_view_win.contraseña_entry.setText(f'{pasword}')
            self.users_view_win.telefono_entry.setText(f'{telefono}')
            self.users_view_win.dip_pasaporte_entry.setText(f'{pasport}')
            self.users_view_win.domiclio_entry.setText(f'{domicilio}')




        self.user_view.exec()



    def act_persona(self):
        id_users =self.users_permit.line_id.text()
        self.users_view_win.acualizar_usuario(id_users)


    def actualizar_lista(self,checkbox):
        if checkbox.isChecked():
            if checkbox.text() not in self.editar_acceso:
             self.editar_acceso.append(checkbox.text())
        else:
            if checkbox.text() in self.editar_acceso:
                while checkbox.text() in self.editar_acceso:
                    self.editar_acceso.remove(checkbox.text())


        
            

    def filtro_user (self):
        self.editar_acceso.clear()
        linea_texto = self.users_permit.filtro_busqueda.currentText()
        buscar = self.base_datos.mostrar_condicion('id_users,permisos','users','nombre',f'"{linea_texto}"')
        for numero,permiso in buscar:
            self.users_permit.line_id.setText(f'{numero}')
            self.lista_permisos = ast.literal_eval(permiso)
            if 'Prestamo' in self.lista_permisos:
                self.users_permit.prestamo_chk.setChecked(True)
                self.editar_acceso.append(self.users_permit.prestamo_chk.text())
            if 'Clientes' in self.lista_permisos:
                self.users_permit.clientes_chk.setChecked(True)
                self.editar_acceso.append(self.users_permit.clientes_chk.text())
            if 'Caja' in self.lista_permisos:
                self.users_permit.caja_chk.setChecked(True)
                self.editar_acceso.append(self.users_permit.caja_chk.text())
            if 'Banco' in self.lista_permisos:
                self.users_permit.banco_chk.setChecked(True)
                self.editar_acceso.append(self.users_permit.banco_chk.text())
            if 'Ingresos' in self.lista_permisos:
                self.users_permit.ingresos_chk.setChecked(True)
                self.editar_acceso.append(self.users_permit.ingresos_chk.text())
            if 'Movimientos' in self.lista_permisos:
                self.users_permit.movimiento_chk.setChecked(True)
                self.editar_acceso.append(self.users_permit.movimiento_chk.text())
            if 'Configuracion' in self.lista_permisos:
                self.users_permit.config_chk.setChecked(True)
                self.editar_acceso.append(self.users_permit.config_chk.text())
            if 'Permisos' in self.lista_permisos:
                self.users_permit.backup_chk.setChecked(True)
                self.editar_acceso.append(self.users_permit.permisos_chk.text())
            if 'Backup' in self.lista_permisos:
                self.users_permit.permisos_chk.setChecked(True)
                self.editar_acceso.append(self.users_permit.backup_chk.text())


        
    def aceptar_permisos(self):
        print(self.editar_acceso)
        acceso = list(self.editar_acceso)
        user_id = self.users_permit.line_id.text()
        self.base_datos.update('users','permisos',f'{acceso}','id_users',user_id)

        self.permision_window.close()

    def pase_validar(self,permiso):
        if f'{permiso}' in self.permisos:
            return 'Permitido'
        else:
            return 'No permitido'
        

    def back_ups(self):
        permitido ='Backup'
        pase = self.pase_validar(permitido)
        if pase  == 'Permitido':
        
            self.backups = Flotante(200,200,'')
            self.win_backups = Backups()

            self.backups.fr_container.setLayout(self.win_backups.general_layout)
            
            self.backups.exec()

    def ajustes(self):
        permitido ='Configuracion'
        pase = self.pase_validar(permitido)
        if pase  == 'Permitido':
        
            self.config_ajustes = Flotante(400,200,'')
            self.ajustes_wd = Settings()

            self.config_ajustes.fr_container.setLayout(self.ajustes_wd.general_layout)
            self.ajustes_wd.btn_select.clicked.connect(self.seleccionar_imagen)


            self.ajustes_wd.btn_save_datos.clicked.connect(self.crea_guarda)
            self.config_ajustes.exec()


    def crea_guarda(self):
        try:
            self.ajustes_wd.crea_tabla_guardar()
            QMessageBox.information(self.prestar,'EXITO',f' La empresa se ha guardado con exito')
            self.ajustes_wd.limpiar()
        except Exception:
            QMessageBox.warning(self.prestar,'ERROR',f' Error al guardar')


    def seleccionar_imagen(self):
        ruta_imagen, _ = QFileDialog.getOpenFileName(self.prestar, "Seleccionar Imagen","", "Imagenes (*.png *.jpg *.jpeg *.bmp)")
        if ruta_imagen:
            carpeta_base = os.path.dirname(ruta_imagen)
            nombre_imagen = ruta_imagen.split("/")[-1]
            self.ajustes_wd.guardar_imagen_db(carpeta_base, ruta_imagen)
            QMessageBox.information(self.prestar,'EXITO',f' La imagen {nombre_imagen}, se ha cargado')
            self.ajustes_wd.imagen_logo()
        else:
            QMessageBox.warning(self,'ERROR', 'No se seleccionó ninguna Imagen')




















from PySide6.QtGui import QIcon
import estilos
import sqlite3

class Login(MainWindow):
    
    def __init__(self):
        super().__init__()
        css_content = estilos.obtener_estilos()
        self.setStyleSheet(css_content)

        self.setWindowFlag(Qt.FramelessWindowHint)
        permiso =['Permisos']
        try:
            self.base_datos.crear_una_tabla()
            self.base_datos.insertar('users','nombre,user_name,passwd,telefono,permisos',('Admin','admin','admin','222000000',f'{permiso}'))
        except Exception:
            pass

        self.setFixedSize(250,250)
        self.center()
        self.setWindowTitle('CONTROL GENERAL DE CONTABILIDAD')
        self.setWindowIcon(QIcon(os.path.join('img/logo_eg.ico')))
        self.central_widget = QWidget(objectName='wid_login')
        self.root = QVBoxLayout()
        self.top_widget_fr = QFrame(objectName='top_log')
        self.buttom_widget_fr = QFrame(objectName='buttom_log')
        
        self.top_widget = QVBoxLayout()
        self.buttom_widget = QVBoxLayout()

        self.top_widget_fr.setLayout(self.top_widget)
        self.buttom_widget_fr.setLayout(self.buttom_widget)

        #self.root.setContentsMargins(0,0,0,0)
        self.central_widget.setLayout(self.root)
        self.setCentralWidget(self.central_widget)
        self.label_user = QLabel('Usuario')
        self.label_pass = QLabel('Contraseña')

        self.edit_user = QLineEdit(objectName='user')
        self.edit_pass = QLineEdit(objectName='pass')
        self.label_info = QLabel(objectName='alarma')
        self.edit_pass.setEchoMode(QLineEdit.Password)
        self.btn_iniciar= QPushButton('Iniciar Sesion',objectName='login')



        self.buttom_widget.addWidget(self.label_user)
        self.buttom_widget.addWidget(self.edit_user)
        self.buttom_widget.addWidget(self.label_pass)
        self.buttom_widget.addWidget(self.edit_pass)
        self.buttom_widget.addWidget(self.label_info)
        self.buttom_widget.addWidget(self.btn_iniciar)

        self.root.addWidget(self.top_widget_fr,20)
        self.root.addWidget(self.buttom_widget_fr,80)



        self.btn_iniciar.clicked.connect(self.iniciar_sesion)

        self.edit_user.returnPressed.connect(lambda:self.edit_pass.setFocus())
        self.edit_pass.returnPressed.connect(self.iniciar_sesion)

    def center(self):
        screen_geometry = QApplication.primaryScreen().geometry()

        x = (screen_geometry.width() - self.width()) //2
        y =(screen_geometry.height() - self.height()) //2

        self.move(x, y)




    def abrir_main(self):
        '''datos = self.base_datos.mostrar_condicion('permisos','users','id_users','1')
        dato_integro = datos[0]
        filtrado = dato_integro[0]
        lista = filtrado
        self.lista = ast.literal_eval(lista)
        for dato in self.lista:
            self.editar_acceso.append(dato)'''
        self.window_obj = MainWindow()
        self.window_obj.prestar.show()
        
       
        #window.ventana_elegida()



    def iniciar_sesion(self):

        nombre_bd = 'prestamos_bd.db'
        ruta_bd = os.path.join(nombre_bd)
        self.config = sqlite3.connect(ruta_bd)
        
        
        with self.config:
            cursor = self.config.cursor()
            bd = "select * FROM users where user_name=?  AND passwd = ?"
            cursor.execute(bd,(self.edit_user.text(),self.edit_pass.text()))
            registro = cursor.fetchone()
            if registro:
                self.abrir_main() 
                self.hide()    
                lista = registro[8]
                self.window_obj.operador = registro[1]
                self.lista = ast.literal_eval(lista)
                for dato in self.lista:
                    self.window_obj.permisos.append(dato)
            else:
                self.label_info.setText('usuario o contraseña incorrectos')
                self.edit_pass.clear()
                self.edit_user.setFocus()
        #print(self.window_obj.permisos)

        
if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec())  
