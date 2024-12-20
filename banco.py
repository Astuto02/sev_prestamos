
from datetime import datetime  
from PySide6.QtWidgets import QVBoxLayout,QFrame,QLabel,QGridLayout,QPushButton,QLineEdit,QDateEdit,QComboBox

from backend import Tabla,MostrarDatos_in,SelecRow,OperacionesMath

from flotante import Flotante
from bd_prestamos import Comunicacion

class Banco(Flotante):
    def __init__(self):
        super(Banco).__init__()
        

        self.base_datos=Comunicacion()

        self.banca_show()

        


    def banca_show(self):

        self.lay_contenedor_banco = QVBoxLayout()

        
        self.datos_banco = QFrame()
        self.datos_banco.setFixedWidth(500)
        self.tabla_banco = QFrame()

        self.lay_contenedor_banco.addWidget(self.datos_banco,40)
        self.lay_contenedor_banco.addWidget(self.tabla_banco,60)

        self.datos_lay = QGridLayout()
        self.tabla_lay = QVBoxLayout()


        self.datos_banco.setLayout(self.datos_lay)
        self.tabla_banco.setLayout(self.tabla_lay)

        self.tabla_banco_wid = Tabla(['id','Fecha','Detalles','Depositos','Retiros','Referencia','Operador'])

        self.prestamo = QLabel('Prestamo Otorgado', objectName='otorgados')
        self.prestamo_edit = QLabel()
        self.prestamo_edit.setFixedHeight(25)

        self.fondos = QLabel('Fondos disponibles', objectName='disponibles')
        self.fondos_entry = QLabel()
        self.fondos_entry.setFixedHeight(25)

        self.deposito = QLabel('Depositos Realizados',objectName='depositos' )
        self.deposito_entry = QLabel()
        self.deposito_entry.setFixedHeight(25)

        self.retiros = QLabel('Retiros Realizados',objectName='retiros' )
        self.retiros_entry = QLabel()
        self.retiros_entry.setFixedHeight(25)

        self.capital = QLabel('Capìtal Recaudado',objectName='capital_rec')
        self.capital_entry = QLabel()
        self.capital_entry.setFixedHeight(25)

        self.intereses = QLabel('Intereses recaudados',objectName='intereses')
        self.intereses_entry = QLabel()
        self.intereses_entry.setFixedHeight(25)

        self.recargos = QLabel('Recargados recaudados',objectName='recargos')   
        self.recargos_entry = QLabel()
        self.recargos_entry.setFixedHeight(25)

        self.inyection = QPushButton('Capital',objectName='otros')

        


        self.datos_lay.addWidget(self.prestamo,0,0)
        self.datos_lay.addWidget(self.prestamo_edit,0,1)

        self.datos_lay.addWidget(self.fondos,1,0)
        self.datos_lay.addWidget(self.fondos_entry,1,1)

        self.datos_lay.addWidget(self.deposito,2,0)
        self.datos_lay.addWidget(self.deposito_entry,2,1)

        self.datos_lay.addWidget(self.retiros,3,0)
        self.datos_lay.addWidget(self.retiros_entry,3,1)

        self.datos_lay.addWidget(self.capital,0,2)
        self.datos_lay.addWidget(self.capital_entry,0,3)

        self.datos_lay.addWidget(self.intereses,1,2)
        self.datos_lay.addWidget(self.intereses_entry,1,3)

        self.datos_lay.addWidget(self.recargos,2,2)
        self.datos_lay.addWidget(self.recargos_entry,2,3)

        self.datos_lay.addWidget(self.inyection,1,4,2,2)

        self.tabla_lay.addWidget(self.tabla_banco_wid)

        self.show_tabla_bank()
        self.disponible_banco()
        

        

    def disponible_banco(self):
        total_deposito_b = self.base_datos.suma_element_misma_columna('deposito','tabla_banco')
        otorgado_b = self.base_datos.suma_element_misma_columna('prestamo','prestamos')
        try:
            if total_deposito_b and otorgado_b ==None:
                total_deposito=0
                otorgado=0
                restar = OperacionesMath(total_deposito,otorgado)
                fondos_disp = restar.resta()
                self.fondos_entry.setText(f'{"{:,}".format(int(fondos_disp))}')
            else:
                total_deposito= int(total_deposito_b)
                otorgado = int(otorgado_b)
                restar = OperacionesMath(total_deposito,otorgado)
                fondos_disp = restar.resta()
                self.fondos_entry.setText(f'{"{:,}".format(int(fondos_disp))}')
        except Exception as e:
            print(e)

    

    

    def show_tabla_bank(self):
        tabla = self.tabla_banco_wid
        show=MostrarDatos_in(tabla)
        show.addDataTable('*','tabla_banco')
        self.seter_banco()

    
    def seter_banco(self):
        total_deposito = self.base_datos.suma_element_misma_columna('deposito','tabla_banco')
        total_retiros = self.base_datos.suma_element_misma_columna('retiro','tabla_banco')
        quitado = self.base_datos.suma_element_misma_columna('prestamo','prestamos')

        if total_deposito==None:
            total_deposito = 0
            self.deposito_entry.setText(f'{"{:,}".format(int(total_deposito))}')
        else:
            self.deposito_entry.setText(f'{"{:,}".format(int(total_deposito))}')
        if total_retiros ==None:
            total_retiros=0
            self.retiros_entry.setText(f'{"{:,}".format(int(total_retiros))}')
        else:
            self.retiros_entry.setText(f'{"{:,}".format(int(total_retiros))}')
        if quitado==None:
            quitado=0
            self.prestamo_edit.setText(f'{"{:,}".format(int(quitado))}')
        else:
            self.prestamo_edit.setText(f'{"{:,}".format(int(quitado))}')
            


        
        
        

    def ver_capital(self):
        capital_t = self.base_datos.suma_element_misma_columna('capital','procesando_pago')
        if capital_t ==None:
            capital = 0
            self.capital_entry.setText(f'{"{:,}".format(int(capital))}')
            return capital
        else:
            self.capital_entry.setText(f'{"{:,}".format(int(capital_t))}')
            return capital_t
    
    def ver_interes(self):
        interes_t = self.base_datos.suma_element_misma_columna('interes','procesando_pago')
        if interes_t ==None:
            interes = 0
            self.intereses_entry.setText(f'{"{:,}".format(int(interes))}')
            return interes
        else:
            self.intereses_entry.setText(f'{"{:,}".format(int(interes_t))}')
            return interes_t
    
    def ver_recargos(self):
        recargo_t = self.base_datos.suma_element_misma_columna('recargo','procesando_pago')
        if recargo_t ==None:
            recargo = 0
            self.recargos_entry.setText(f'{"{:,}".format(int(recargo))}')
            return recargo
        else:
            self.recargos_entry.setText(f'{"{:,}".format(int(recargo_t))}')
            return recargo_t


class Operar():
    def __init__(self):
        super().__init__()
        

        self.main_root = QGridLayout()
        

        self.fecha_banco = QDateEdit()
        self.fecha_banco.setCalendarPopup(True)
        self.fecha_banco.setDate(datetime.today())
        self.fecha_banco.date().toString('dd/MM/yyyy') 


        self.detalle =QLabel('Detalle')
        self.deposito = QLabel('Deposito: ')
        self.retiros = QLabel('Retiros: ')

        self.detalles = QComboBox()
        self.deposito_banco = QLineEdit()
        self.retiros_banco = QLineEdit()

        self.btn_guardar = QPushButton('guardar',objectName='otros')

        detalles = ['Capital Inicial','Retiros','Más Capital']
        for item in detalles:
            self.detalles.addItem(item)

        self.main_root.addWidget(self.fecha_banco,0,1)
        self.main_root.addWidget(self.detalle,1,0)
        self.main_root.addWidget(self.deposito,2,0)
        self.main_root.addWidget(self.retiros,2,0)
        self.main_root.addWidget(self.detalles,1,1)
        self.main_root.addWidget(self.deposito_banco,2,1)
        self.main_root.addWidget(self.retiros_banco,2,1)
        self.main_root.addWidget(self.btn_guardar,3,0,1,2)

        self.retiros.hide()
        self.retiros_banco.hide()

        self.detalles.currentTextChanged.connect(self.opracion)
        

        

    def opracion(self):
        if self.detalles.currentText() =='Retiros':
            self.deposito.hide()
            self.deposito_banco.hide()
            self.retiros.show()
            self.retiros_banco.show()
        else:
            self.retiros.hide()
            self.retiros_banco.hide()
            self.deposito.show()
            self.deposito_banco.show()