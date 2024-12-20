

from PySide6.QtWidgets import QVBoxLayout,QFrame,QHBoxLayout,QLabel,QGridLayout,QPushButton,QLineEdit,QTextEdit,QStackedLayout,QWidget

from backend import Tabla,MostrarDatos_in,SelecRow,OperacionesMath


from datetime import datetime,timedelta

from bd_prestamos import Comunicacion



class Movimientos():
    def __init__(self):
        super(Movimientos).__init__()

        self.mostrar_movimientos()

    def mostrar_movimientos(self):
        self.general_move = QHBoxLayout()

        self.fr_botones= QFrame()
        self.fr_main_lab = QFrame()

        self.general_move.addWidget(self.fr_botones,20)
        self.general_move.addWidget(self.fr_main_lab,80)

        self.layout_b = QVBoxLayout()
        self.layout_main = QStackedLayout(objectName='stack')

        self.fr_botones.setLayout(self.layout_b)
        self.fr_main_lab.setLayout(self.layout_main)

        self.btn_cobros = QPushButton('Gestion Cobros',objectName='otros')
        self.inf_cancelados = QPushButton('Cancelados',objectName='otros')
        self.endeudados = QPushButton('Endeudados',objectName='otros')

        self.layout_b.addWidget(self.btn_cobros)
        self.layout_b.addWidget(self.inf_cancelados)
        self.layout_b.addWidget(self.endeudados)
        self.layout_b.addStretch()

        self.cobros = QWidget()
        self.deudas = QWidget()
        self.cancel = QWidget()

        self.layout_main.addWidget(self.cobros)
        self.layout_main.addWidget(self.cancel)
        self.layout_main.addWidget(self.deudas)

class Cobros():
    def __init__(self):
        super().__init__()

        self.base_datos = Comunicacion()


        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0,0,0,0)

        self.fr_top = QFrame()
        self.fr_bot = QFrame()

        self.lay_top = QHBoxLayout()
        self.lay_bot = QVBoxLayout()

        self.fr_top.setLayout(self.lay_top)
        self.fr_bot.setLayout(self.lay_bot)

        self.main_layout.addWidget(self.fr_top,10)
        self.main_layout.addWidget(self.fr_bot,90)

        self.tabla_cobros = Tabla(['ID','Nombre','Modo de Pago','Prestamo','Deuda Total','Telefono','Observaciones'])
        self.lay_bot.addWidget(self.tabla_cobros)

        self.buscando_cobros = QLineEdit()
        self.buscando_cobros.setPlaceholderText('Buscar... ')

        self.printr = QPushButton(objectName='imprimir')

        self.lay_top.addWidget(self.buscando_cobros)
        self.lay_top.addStretch()
        self.lay_top.addWidget(self.printr)

    def guardar_cobradores(self,nombre,pago,monto,saldo,telefono):
        self.base_datos = Comunicacion()
        self.base_datos.insertar('cobros','nombre,modo_pago,monto,saldo,telefono',(nombre,pago,monto,saldo,telefono))

    def show_cobros_all(self):
        query=MostrarDatos_in(self.tabla_cobros)
        query.addDataTable('id_cobros,nombre,modo_pago,monto,saldo,telefono,observaciones','cobros')

    def show_cobros(self):
        datos = self.buscando_cobros.text()
        query=MostrarDatos_in(self.tabla_cobros)
        query.addDataTableCondicion('id_cobros,nombre,modo_pago,monto,saldo,telefono,observaciones','cobros','nombre',datos)

    def select_item(self):
        try:
            tabla=self.tabla_cobros
            selected = SelecRow(tabla)
            self.valor = selected.obten_valor(0)
            return(self.valor)
        except Exception as e:
            print(f'No se ha podido seleccionar un elemneto {e}')
        
    
class Comentarios():
    def __init__(self):
        super(Comentarios).__init__()
        self.base_datos = Comunicacion()

        self.lay_gral = QVBoxLayout()

        self.texto = QTextEdit()
        self.lay_gral.addWidget(self.texto)

        self.btn_update = QPushButton(objectName='save_prest')
        self.lay_gral.addWidget(self.btn_update)

    def actualizar_comment(self,id_cobros):
        texto = self.texto.toPlainText()
        self.base_datos.update('cobros','observaciones',texto,'id_cobros',id_cobros)








class Cancelaciones():
    def __init__(self):
        super().__init__()


        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0,0,0,0)

        self.fr_top = QFrame()
        self.fr_bot = QFrame()

        self.lay_top = QHBoxLayout()
        self.lay_bot = QVBoxLayout()

        self.fr_top.setLayout(self.lay_top)
        self.fr_bot.setLayout(self.lay_bot)

        self.main_layout.addWidget(self.fr_top,10)
        self.main_layout.addWidget(self.fr_bot,90)

        self.tabla_cancelados = Tabla(['ID','Nombre','Prestamo','Fecha','Tasa','Deuda Total'])
        self.lay_bot.addWidget(self.tabla_cancelados)

        self.buscando_cancel = QLineEdit()
        self.buscando_cancel.setPlaceholderText('Buscar... ')

        self.printer = QPushButton(objectName='imprimir')

        self.lay_top.addWidget(self.buscando_cancel)
        self.lay_top.addStretch()
        self.lay_top.addWidget(self.printer)

    def show_cancelaciones(self):
        try:
            query=MostrarDatos_in(self.tabla_cancelados)
            query.addDataTableCondicion('referencia,nombre_prestador,prestamo,fecha_hoy,tasa_interes,monto_total_pagar,intereses_totales,fecha_cancelacion','prestamos','estado','CANCELADO')
        except Exception as e:
            print(f'No hay cancelados {e}')
    def sow_cancel_filter(self):
        try:
            datos = self.buscando_cancel.text()
            query=MostrarDatos_in(self.tabla_cancelados)
            query.addDataTable_filter_max('referencia,nombre_prestador,prestamo,fecha_hoy,tasa_interes,monto_total_pagar,intereses_totales,fecha_cancelacion','prestamos','estado','CANCELADO','nombre_prestador',datos,'','')
        except Exception as e:
            print(f'No existe este en el filtro {e}')

class Deudas():
    def __init__(self):
        super().__init__()


        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0,0,0,0)

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0,0,0,0)

        self.fr_top = QFrame()
        self.fr_bot = QFrame()

        self.lay_top = QHBoxLayout()
        self.lay_bot = QVBoxLayout()

        self.fr_top.setLayout(self.lay_top)
        self.fr_bot.setLayout(self.lay_bot)

        self.main_layout.addWidget(self.fr_top,10)
        self.main_layout.addWidget(self.fr_bot,90)

        self.tabla_deudas = Tabla(['ID','Nombre','Prestamo','Fecha','Tasa','Deuda Total'])
        self.lay_bot.addWidget(self.tabla_deudas)

        self.buscando_deudas = QLineEdit()
        self.buscando_deudas.setPlaceholderText('Buscar... ')

        self.printr = QPushButton(objectName='imprimir')

        self.lay_top.addWidget(self.buscando_deudas)
        self.lay_top.addStretch()
        self.lay_top.addWidget(self.printr)

    def show_deudas(self):
        try:
            query=MostrarDatos_in(self.tabla_deudas)
            query.addDataTableCondicion('referencia,nombre_prestador,prestamo,fecha_hoy,tasa_interes,saldo_total','prestamos','estado','ADEUDADO')
        except Exception as e:
            print(f'Deudas Vacias {e}')
    def sow_deudas_filter(self):
        try:
            datos = self.buscando_deudas.text()
            query=MostrarDatos_in(self.tabla_deudas)
            query.addDataTable_filter_max('referencia,nombre_prestador,prestamo,fecha_hoy,tasa_interes,monto_total_pagar,intereses_totales,fecha_cancelacion','prestamos','estado','ADEUDADO','nombre_prestador',datos,'','')
        except Exception as e:
            print(f' Error {e}')


    







