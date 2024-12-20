
from PySide6.QtWidgets import QVBoxLayout,QFrame,QHBoxLayout,QLabel,QGridLayout,QPushButton,QLineEdit,QDateEdit,QComboBox

from backend import Tabla,MostrarDatos_in,SelecRow,OperacionesMath


from datetime import datetime,timedelta

from bd_prestamos import Comunicacion

class Caja():
    def __init__(self):
        super(Caja).__init__()
        
        self.base_datos = Comunicacion()

        self.show_caja()

        
        self.buscar_caja.textChanged.connect(self.show_operaciones_clientes)
        self.tabla_caja_top.doubleClicked.connect(self.show_data_client)

       

    def show_caja(self):

        self.general_caja = QVBoxLayout()

        self.fr_top_caja = QFrame()
        self.fr_central_caja = QFrame()
        self.fr_bottom_caja = QFrame()

        self.general_caja.addWidget(self.fr_top_caja,10)
        self.general_caja.addWidget(self.fr_central_caja,35)
        self.general_caja.addWidget(self.fr_bottom_caja,55)


        self.lay_fr_top_caja = QHBoxLayout()
        self.lay_fr_top_caja.setContentsMargins(0,0,0,0)
        self.lay_fr_central_caja = QHBoxLayout()
        self.lay_fr_central_caja.setContentsMargins(0,0,0,0)
        self.lay_fr_bottom_caja = QHBoxLayout()
        self.lay_fr_bottom_caja.setContentsMargins(0,0,0,0)

        self.fr_top_caja.setLayout(self.lay_fr_top_caja)
        self.fr_central_caja.setLayout(self.lay_fr_central_caja)
        self.fr_bottom_caja.setLayout(self.lay_fr_bottom_caja)
        ######################################################### buscar
        self.buscar_caja = QLineEdit()
        self.buscar_caja.setFixedWidth(200)
        self.num_orden = QLabel(objectName='orden')

        self.lay_fr_top_caja.addWidget(self.buscar_caja)
        self.lay_fr_top_caja.addWidget(self.num_orden)
        self.lay_fr_top_caja.addStretch()

        #################################### datos
        fr_izq_central = QFrame()
        fr_der_central = QFrame()


        self.lay_fr_central_caja.addWidget(fr_izq_central,50)   # layout
        self.lay_fr_central_caja.addWidget(fr_der_central,50)   # layout

        self.lay_izq = QVBoxLayout()
        self.lay_izq.setContentsMargins(0,0,0,0)
        fr_izq_central.setLayout(self.lay_izq)
        self.lay_derecha = QVBoxLayout()
        self.lay_derecha.setContentsMargins(0,0,0,0)
        fr_der_central.setLayout(self.lay_derecha)

        fr_izq_top = QFrame()
        fr_izq_bot = QFrame()

        self.lay_izq.addWidget(fr_izq_top,50)
        self.lay_izq.addWidget(fr_izq_bot,50)

        self.fr_izq_top_lay = QVBoxLayout()
        self.fr_izq_top_lay.setContentsMargins(0,0,0,0)
        self.fr_izq_bot_lay = QGridLayout()
        self.fr_izq_bot_lay.setContentsMargins(0,0,0,0)

        fr_izq_top.setLayout(self.fr_izq_top_lay)
        fr_izq_bot.setLayout(self.fr_izq_bot_lay)

        self.tabla_caja_top = Tabla(['Prestamo','Cliente','Monto','Estado'])
        self.fr_izq_top_lay.addWidget(self.tabla_caja_top)

        prestamo = QLabel('Prestamo monto')
        tasa_interes = QLabel('Tasa interes')
        periodo = QLabel('Periodo')
        tipo_pago = QLabel('Tipo de pago')
        fecha_otorg = QLabel('Fecha otorgado')
        fecha_inicio = QLabel('Fecha inicio')
        estado = QLabel('Estado')

        self.prestamo_caja =QLineEdit()
        self.tasa_interes_caja =QLineEdit()
        self.periodo_caja =QLineEdit()
        self.tipo_pago_caja =QLineEdit()
        self.fecha_otorg_caja =QLineEdit()
        self.fecha_inicio_caja =QLineEdit()
        self.estado_caja =QLineEdit()

        fr_botones_caja_left = QFrame()

        self.fr_izq_bot_lay.addWidget(prestamo,0,0)
        self.fr_izq_bot_lay.addWidget(tasa_interes,1,0)
        self.fr_izq_bot_lay.addWidget(periodo,2,0)
        self.fr_izq_bot_lay.addWidget(tipo_pago,3,0)
        self.fr_izq_bot_lay.addWidget(fecha_otorg,0,2)
        self.fr_izq_bot_lay.addWidget(fecha_inicio,1,2)
        self.fr_izq_bot_lay.addWidget(estado,2,2)
        self.fr_izq_bot_lay.addWidget(fr_botones_caja_left,2,3,1,2)

        self.fr_izq_bot_lay.addWidget(self.prestamo_caja,0,1)
        self.fr_izq_bot_lay.addWidget(self.tasa_interes_caja,1,1)
        self.fr_izq_bot_lay.addWidget(self.periodo_caja,2,1)
        self.fr_izq_bot_lay.addWidget(self.tipo_pago_caja,3,1)
        self.fr_izq_bot_lay.addWidget(self.fecha_otorg_caja,0,3)
        self.fr_izq_bot_lay.addWidget(self.fecha_inicio_caja,1,3)
        self.fr_izq_bot_lay.addWidget(self.estado_caja,2,3)
        #la parte de nombre y los datos del prestamo

        fr_top_derecha = QFrame()
        fr_bot_derecha = QFrame()
        self.lay_derecha.addWidget(fr_top_derecha)
        self.lay_derecha.addWidget(fr_bot_derecha)

        self.lay_top_derecha = QGridLayout()
        self.lay_top_derecha.setContentsMargins(0,0,0,0)
        self.lay_bot_derecha = QGridLayout()
        self.lay_bot_derecha.setContentsMargins(0,0,0,0)

        fr_top_derecha.setLayout(self.lay_top_derecha)
        fr_bot_derecha.setLayout(self.lay_bot_derecha)

        nombre = QLabel('Nombre')
        identidad = QLabel('Indentidad')
        telefono = QLabel('Telefono ')
        id_client = QLabel('Direccion')
        correo_client = QLabel('Banco ')

        self.nombre_caja_cliente = QLineEdit(objectName='especiales')
        self.identidad_caja_cliente = QLineEdit(objectName='especiales')
        self.telefono_caja_cliente = QLineEdit(objectName='especiales')
        self.id_client_caja_cliente = QLineEdit(objectName='especiales')
        self.correo_client_caja_cliente = QLineEdit(objectName='especiales')

        self.fecha_hoy = QDateEdit()
        self.fecha_hoy.setCalendarPopup(True)
        self.fecha_hoy.setDate(datetime.today())
        self.fecha_hoy.date().toString('dd/MM/yyyy') 

        self.lay_top_derecha.addWidget(nombre,0,0)
        self.lay_top_derecha.addWidget(identidad,1,0)
        self.lay_top_derecha.addWidget(telefono,2,0)
        self.lay_top_derecha.addWidget(id_client,1,2)
        #self.lay_top_derecha.addWidget(correo_client,2,2)

        self.lay_top_derecha.addWidget(self.nombre_caja_cliente,0,1)
        self.lay_top_derecha.addWidget(self.fecha_hoy,0,3)
        self.lay_top_derecha.addWidget(self.identidad_caja_cliente,1,1)
        self.lay_top_derecha.addWidget(self.telefono_caja_cliente,2,1)
        self.lay_top_derecha.addWidget(self.id_client_caja_cliente,1,3)
        #self.lay_top_derecha.addWidget(self.correo_client_caja_cliente,2,3)

        monto_total = QLabel('Monto total')
        monto_cuotas = QLabel('Monto cuotas')
        intereses_totales=QLabel('Intereses totales')

        self.monto_total_caja = QLineEdit(objectName='especiales')
        self.monto_cuotas_caja = QLineEdit(objectName='especiales')
        self.intereses_totales_caja = QLineEdit(objectName='especiales')

        self.btn_estado_cuotas = QPushButton(' Ver Estado Cuotas ',objectName='otros')
        self.btn_tabla_amort = QPushButton(' Ver Tabla AM ',objectName='otros')

        self.procesar_btn = QPushButton(' Procesar ',objectName='otros')

        self.lay_bot_derecha.addWidget(monto_total,0,0)
        self.lay_bot_derecha.addWidget(monto_cuotas,1,0)
        self.lay_bot_derecha.addWidget(intereses_totales,2,0)
        self.lay_bot_derecha.addWidget(self.monto_total_caja,0,1)
        self.lay_bot_derecha.addWidget(self.monto_cuotas_caja,1,1)
        self.lay_bot_derecha.addWidget(self.intereses_totales_caja,2,1)
        self.lay_bot_derecha.addWidget(self.btn_estado_cuotas,0,3)
        self.lay_bot_derecha.addWidget(self.btn_tabla_amort,1,3)
        self.lay_bot_derecha.addWidget(self.procesar_btn,2,3)

         ######################################     tabla detalles

        self.tabla_operacion_caja = Tabla(['Fecha','Detalles','Capital','Interes','Recargos','Total ','Referencia','Operador'])
        self.lay_fr_bottom_caja.addWidget(self.tabla_operacion_caja)

        

    def show_operaciones_clientes(self):
        tabla=self.tabla_caja_top
        buscar = self.buscar_caja.text()
        show_tabla = MostrarDatos_in(tabla)
        show_tabla.addDataTableCondicion('id_prestamos,nombre_prestador,prestamo,estado','prestamos','nombre_prestador',buscar)

    def show_data_client(self):
        tabla = self.tabla_caja_top
        selected = SelecRow(tabla)
        valor = selected.obten_valor(0)
        query=self.base_datos.filtro_select('prestamo,tasa_interes,periodos,tipo_pago,fecha_hoy,fecha_inicio,estado,saldo_total,cuota_mensual,intereses_totales,referencia,telefono,dip_pasaporte,nombre_prestador,direccion',\
                                               'prestamos','id_prestamos',valor)
        for monto,interes,periodo,tipo_pago,fecha,fecha_ini,estado,monto_total,cuotas,intereses,ref,phone,dip,nombre,adress in query:
            self.prestamo_caja.setText(f'{monto}')
            self.tasa_interes_caja.setText(f'{interes}%')
            self.periodo_caja.setText(f'{periodo}')
            self.tipo_pago_caja.setText(f'{tipo_pago}')
            self.fecha_otorg_caja.setText(f'{fecha}')
            self.fecha_inicio_caja.setText(f'{fecha_ini}')
            self.estado_caja.setText(f'{estado}')
            self.monto_total_caja.setText(f'{monto_total}')
            self.monto_cuotas_caja.setText(f'{cuotas}')
            self.intereses_totales_caja.setText(f'{intereses}')
            self.num_orden.setText(f'{ref}')
            self.nombre_caja_cliente.setText(f'{nombre}')
            self.identidad_caja_cliente.setText(f'{dip}')
            self.telefono_caja_cliente.setText(f'{phone}')
            self.id_client_caja_cliente.setText(f'{adress}')
            

        self.show_operate_clients()

    def show_operate_clients(self):
        tabla=self.tabla_operacion_caja
        ref = self.num_orden.text()
        show_tabla = MostrarDatos_in(tabla)
        show_tabla.addDataTableCondicion('fecha,detalle,capital,interes,recargo,total_pago,ref,operador','procesando_pago','ref',ref)

    
            

    def pagado(self):
        try:
            if len(self.num_orden.text())!=0:
                ref = self.num_orden.text()
                query = self.base_datos.suma_elementos_columna_filtro('pagado','procesando_pago','ref',ref)
                self.total_pagado = query
                if query == None:
                    self.total_pagado=0
            else:
                self.total_pagado = query
            return self.total_pagado
        except Exception:
            pass
      
        
    

    ############################################################### tabla de amortizacion

class TablaAmortizacion():
    def __init__(self):
        super(TablaAmortizacion).__init__()

        self.tabla_amortizacion()


    def tabla_amortizacion(self):
        

        self.general_lay =QVBoxLayout()
        

        fr_tabla_view =QFrame()
        fr_totales = QFrame()

        self.general_lay.addWidget(fr_tabla_view)
        self.general_lay.addWidget(fr_totales)

        view_tabla_lay = QVBoxLayout()
        lay_totales = QHBoxLayout()

        fr_tabla_view.setLayout(view_tabla_lay)
        fr_totales.setLayout(lay_totales)

        self.tabla_amorti = Tabla(['Periodo','Fecha','Cuota Fija','Capital','Interes','Saldo'])
        view_tabla_lay.addWidget(self.tabla_amorti)
        capital = QLabel('Capital')
        interes = QLabel('Interes')
        saldo = QLabel('Saldo')

        self.capital_amort = QLineEdit()
        self.interes_amort = QLineEdit()
        self.saldo_amort = QLineEdit()

        lay_totales.addStretch()
        lay_totales.addWidget(capital)
        lay_totales.addWidget(self.capital_amort)
        lay_totales.addWidget(interes)
        lay_totales.addWidget(self.interes_amort)
        lay_totales.addWidget(saldo)
        lay_totales.addWidget(self.saldo_amort)
        lay_totales.addStretch()
    
    def gestion_periodos(self,tipo_pago:str):
        self.periodos_fijos:int

        if tipo_pago =='semanal':
            self.periodos_fijos=7
        elif tipo_pago =='quincenal':
            self.periodos_fijos=15
        if tipo_pago =='mensual':
            self.periodos_fijos=30
        elif tipo_pago =='bimensual':
            self.periodos_fijos=60
        elif tipo_pago =='trimestral':
            self.periodos_fijos=90
        elif tipo_pago =='semestral':
            self.periodos_fijos=180
        return self.periodos_fijos

    def mostrar_tabla_amort(self,ref):
        referen = ref
        import json

        self.base_datos = Comunicacion()
        self.base_datos.borrar_datos_comp('tabla_amortizar')
        tabla = self.base_datos.filtro_condicion('tabla_amortizacion,tipo_pago,fecha_inicio','prestamos','referencia',ref)
        for amortizar,tipo_pago,fecha in tabla:
            fecha = datetime.strptime(f'{fecha}',"%d/%m/%Y")
            dias = self.gestion_periodos(f'{tipo_pago}')
        amoriza = str(amortizar)
        amortizar = json.loads(amortizar) 
        for i, fila in enumerate(amortizar,start=1):
            fecha = fecha+timedelta(days=dias)
            real_fecha = fecha.strftime("%d/%m/%Y")
            periodo = f'{i}'
            Fecha = real_fecha
            cuota_fija =  f'{fila['Cuota']}'
            capital = f'{fila['Capital']}'
            interes = f'{fila['Interes']}'
            saldo = f'{fila['Saldo']}'
            self.base_datos.insertar('tabla_amortizar','periodo,fecha,cuota_fija,capital,interes,saldo',(periodo,Fecha,cuota_fija,capital,interes,saldo))
            
            

        tabla = self.tabla_amorti 
        mostrando = MostrarDatos_in(tabla)
        mostrando.addDataTable('periodo,fecha,cuota_fija,capital,interes,saldo','tabla_amortizar')
        capital=self.base_datos.suma_element_misma_columna('capital','tabla_amortizar')
        interes = self.base_datos.suma_element_misma_columna('interes','tabla_amortizar')

        self.interes_amort.setText(f'{interes}')
        self.capital_amort.setText(f'{capital}')

        inter = int(self.interes_amort.text())
        capi = int(self.capital_amort.text())

        resultado = inter + capi

        self.saldo_amort.setText(f'{resultado}')
        


    ######################################################################### ventana emergente procesar los pagos
class ProcesarPagos():
    def __init__(self):
        super(ProcesarPagos).__init__()
        self.procesar_pagos()

    def procesar_pagos(self):
        

        self.procesar_lay = QGridLayout()
        
        fr_proceso = QFrame(objectName='procesar_fr')
        saldo = QLabel('Saldo')
        self.saldo_edit = QLineEdit()
        self.confirmar = QPushButton(' Confirmar ',objectName='otros')

        self.procesar_lay.addWidget(fr_proceso,0,0,4,2)
        self.procesar_lay.addWidget(saldo,5,0)
        self.procesar_lay.addWidget(self.saldo_edit,5,1)
        self.procesar_lay.addWidget(self.confirmar,6,1,1,2)

        lay_proceso = QGridLayout()
        fr_proceso.setLayout(lay_proceso)

        detalle = QLabel('Detalle')
        self.detalle = QComboBox()
        combos = ['Capital e Interes','Solo Capital','Solo Interes']
        for combo in combos:
            self.detalle.addItem(combo)

        capital_process = QLabel('Capital ')
        interes_proceso = QLabel('Interes ')
        recargos_proceso = QLabel('Recargos ')

        self.capit_proces = QLineEdit()
        self.interes_proces = QLineEdit()
        self.recargos_proces = QLineEdit()

        lay_proceso.addWidget(detalle,0,0)
        lay_proceso.addWidget(capital_process,1,0)
        lay_proceso.addWidget(interes_proceso,2,0)
        lay_proceso.addWidget(recargos_proceso,3,0)
        lay_proceso.addWidget(self.detalle,0,1)
        lay_proceso.addWidget(self.capit_proces,1,1)
        lay_proceso.addWidget(self.interes_proces,2,1)
        lay_proceso.addWidget(self.recargos_proces,3,1)

    def small_oper(self,capital,interes):

        self.capi =int(capital)
        self.inter = int(interes)

        result = self.capi + self.inter
        return result

class EstadoCuotas():
    def __init__(self):
        super(EstadoCuotas).__init__()
        self.mostrar_estado()

        self.base_datos = Comunicacion()

    def mostrar_estado(self):
        

        self.cuota_greal = QVBoxLayout()
        
        fr_proceso = QFrame(objectName='procesar_fr')
        fr_tabla = QFrame(objectName='procesar_fr')


        self.lay_proces = QGridLayout()
        self.lay_tabla = QVBoxLayout()

        fr_proceso.setLayout(self.lay_proces)
        fr_tabla.setLayout(self.lay_tabla)

        self.tabla_estado = Tabla(['Operacion','Fecha','Detalle','Capital','Interes','Recargo','Pagado','Pendiente'])

        self.lay_tabla.addWidget(self.tabla_estado)

        tipo_pago = QLabel('Tipo Pago: ')
        periodos = QLabel('Periodos: ')
        total_pagar = QLabel('Total a pagar: ')
        cuota_fija = QLabel('Cuota Fija: ')
        interes_total = QLabel('Intereses Totales: ')

        self.tipo_pago = QLineEdit()
        self.periodos = QLineEdit()
        self.total_pagar = QLineEdit()
        self.cuota_fija = QLineEdit()
        self.interes_total = QLineEdit()

        self.btn_printer = QPushButton(objectName='imprimir')

        self.lay_proces.addWidget(tipo_pago,0,0)
        self.lay_proces.addWidget(periodos,1,0)
        self.lay_proces.addWidget(total_pagar,0,2)
        self.lay_proces.addWidget(cuota_fija,1,2)
        self.lay_proces.addWidget(interes_total,2,2)
        self.lay_proces.addWidget(self.tipo_pago,0,1)
        self.lay_proces.addWidget(self.periodos,1,1)
        self.lay_proces.addWidget(self.total_pagar,0,3)
        self.lay_proces.addWidget(self.cuota_fija,1,3)
        self.lay_proces.addWidget(self.interes_total,2,3)
        self.lay_proces.addWidget(self.btn_printer,0,4)


        self.cuota_greal.addWidget(fr_proceso,30)
        self.cuota_greal.addWidget(fr_tabla,70)

    
    def show_estado(self,ref):
        self. show_es = MostrarDatos_in(self.tabla_estado)
        columnas = 'ref,fecha,detalle,capital,interes,recargo,pagado,pendiente'
        self.show_es.addDataTableCondicion(columnas,'procesando_pago','ref',ref)

    
    def datos_persona(self,ref):
        columnas = 'tipo_pago,periodos,saldo_total,cuota_mensual,intereses_totales'
        datos = self.base_datos.filtro_condicion(columnas,'prestamos','referencia',ref)
        for tipo_pago,periodos,total_pagar,cuota_fija,intereses in datos:

            self.tipo_pago.setText(f'{tipo_pago}')
            self.periodos.setText(f'{periodos}')
            self.total_pagar.setText(f'{total_pagar}')
            self.cuota_fija.setText(f'{cuota_fija}')
            self.interes_total.setText(f'{intereses}')
