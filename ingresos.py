


from PySide6.QtWidgets import QMainWindow, QWidget,QVBoxLayout,QFrame,QHBoxLayout,QLabel,QGridLayout,QPushButton,QApplication,\
QLineEdit,QDateEdit,QComboBox

from datetime import datetime,timedelta

from backend import Tabla,MostrarDatos_in,SelecRow,OperacionesMath
import estilos

from flotante import Flotante
from bd_prestamos import Comunicacion


class VerIngresos():
    def __init__(self):
        super(VerIngresos).__init__()

        self.show_ingresos()
        self.buscar_año_ingr.textActivated.connect(self.filtro_meses)
        self.buscar_mes_ingr.textActivated.connect(self.filtro_meses)
        self.actualizar_btn.clicked.connect(self.show_all_ingreso)

    def show_ingresos(self):

        self.general_ingresos = QVBoxLayout()
        

        fr_ingresos = QFrame()
        ingresos_tabla = QFrame()

        self.general_ingresos.addWidget(fr_ingresos,20)
        self.general_ingresos.addWidget(ingresos_tabla,80)
        self.tabla_ingresos = Tabla(['Fecha','Referencia','Nombre','Detalle','Capital','Interes','Recargo'])

        lay_ingresos = QHBoxLayout()
        lay_tabla_ingresos = QVBoxLayout()
        lay_tabla_ingresos.setContentsMargins(0,0,0,0)

        fr_ingresos.setLayout(lay_ingresos)
        ingresos_tabla.setLayout(lay_tabla_ingresos)

        buscar_fecha = QLabel('Fecha')
        self.fecha_busqueda = QDateEdit()
        self.fecha_busqueda.setCalendarPopup(True)
        self.fecha_busqueda.setDate(datetime.today())
        self.fecha_busqueda.date().toString('dd/MM/yyyy') 
        buscar_mes = QLabel('Mes')
        buscar_año = QLabel('Año ')

        self.buscar_mes_ingr = QComboBox()
        self.buscar_año_ingr = QComboBox()
        self.buscar_mes_ingr.setFixedWidth(80)
        self.buscar_año_ingr.setFixedWidth(80)

        self.actualizar_btn = QPushButton(objectName='upd_tabla')
        self.printer = QPushButton(objectName='imprimir')

        lay_ingresos.addWidget(buscar_fecha)
        lay_ingresos.addWidget(self.fecha_busqueda)
        lay_ingresos.addWidget(self.actualizar_btn)
        lay_ingresos.addStretch()
        lay_ingresos.addWidget(self.printer)
        lay_ingresos.addStretch()

        lay_ingresos.addWidget(buscar_mes)
        lay_ingresos.addWidget(self.buscar_mes_ingr)
        lay_ingresos.addWidget(buscar_año)
        lay_ingresos.addWidget(self.buscar_año_ingr)


        lay_tabla_ingresos.addWidget(self.tabla_ingresos)

        años=['','2024','2025','2026','2027','2028','2029','2030','2031','2032','2033','2034']
        for año in años:
            self.buscar_año_ingr.addItem(año)

        self.meses=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
        for mes in self.meses:
            self.buscar_mes_ingr.addItem(mes)

    def datos_fecha(self):

        meses=self.buscar_mes_ingr.currentIndex() +1
        año =self.buscar_año_ingr.currentText()
        mes = f'{meses:02}'
        self.fecha_año =f'/{mes}/{año}'
        return self.fecha_año


    def filtro_meses(self):
        fecha = self.datos_fecha()
        columnas = 'fecha,ref,cliente_name,detalle,capital,interes,recargo'
        tabla = self.tabla_ingresos
        self.filtrar = MostrarDatos_in(tabla)
        self.filtrar.addDataTableCondicion(columnas,'procesando_pago','fecha',fecha)

    def filtro_fecha(self):
        fecha = self.fecha_busqueda.text()
        columnas = 'fecha,ref,cliente_name,detalle,capital,interes,recargo'
        tabla = self.tabla_ingresos
        self.filtrado = MostrarDatos_in(tabla)
        self.filtrado.addDataTableCondicion(columnas,'procesando_pago','fecha',fecha)

    def show_all_ingreso(self):
        columnas = 'fecha,ref,cliente_name,detalle,capital,interes,recargo'
        tabla = self.tabla_ingresos
        self.filtrado = MostrarDatos_in(tabla)
        self.filtrado.addDataTable(columnas,'procesando_pago')



