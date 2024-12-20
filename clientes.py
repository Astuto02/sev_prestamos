
from PySide6.QtWidgets import  QVBoxLayout,QLabel,QFrame, QPushButton,QGridLayout, QLineEdit,QHBoxLayout,QTextEdit
   
from PySide6.QtCore import Qt

from backend import Tabla,MostrarDatos_in,SelecRow
from bd_prestamos import Comunicacion



class VerClientesDatos():
    def __init__(self):
        super(VerClientesDatos).__init__()

        self.show_clientes()

        self.base_datos = Comunicacion()
        self.guardar_cliente.clicked.connect(self.insert_clientes)

    def show_clientes(self):
        self.general_clientes = QVBoxLayout()

        fr_busqueda_clientes = QFrame()
        fr_main_clientes = QFrame()
        bottom_frame = QFrame()

        self.general_clientes.addWidget(fr_busqueda_clientes,10)
        self.general_clientes.addWidget(fr_main_clientes,80)
        self.general_clientes.addWidget(bottom_frame,10)

        lay_busqueda = QHBoxLayout()
        lay_main_clients = QHBoxLayout()
        bottom_lay_cliente = QHBoxLayout()

        fr_busqueda_clientes.setLayout(lay_busqueda)
        fr_main_clientes.setLayout(lay_main_clients)
        bottom_frame.setLayout(bottom_lay_cliente)

        self.buscar_clientes = QPushButton(' Buscar ',objectName='otros')
        #self.buscar_clientes.setMaximumWidth(50)
        lay_busqueda.addWidget(self.buscar_clientes)
        lay_busqueda.addStretch()


        fr_izq_cliente = QFrame()
        fr_der_cliente = QFrame(objectName='derecha_ref')

        lay_main_clients.addWidget(fr_izq_cliente)
        lay_main_clients.addWidget(fr_der_cliente)

        izq_lay_cliente = QGridLayout()
        der_lay_cliente = QGridLayout()

        fr_izq_cliente.setLayout(izq_lay_cliente)
        fr_der_cliente.setLayout(der_lay_cliente)

        nombre = QLabel('Nombre')
        doc_identidad= QLabel('Doc Identidad')
        id_cliente= QLabel('Id')
        correo = QLabel('correo')
        telefono= QLabel('Telefono')
        dirrecion= QLabel('Direccion')
        observacion= QLabel('Observacion')

        self.nombre_cliente = QLineEdit()
        self.doc_identidad = QLineEdit()
        self.id_cliente = QLineEdit()
        self.id_cliente.setReadOnly(True)
        self.correo_cliente = QLineEdit()
        self.telefono_cliente = QLineEdit()
        self.direccion_cliente = QLineEdit()
        self.observaciones = QTextEdit()

        trabajo =QLabel ('L Trabajo')
        banco =QLabel ('Banco')
        cuenta_banca =QLabel ('Cuenta Banco')

        self.trabajo_ed = QLineEdit()
        self.banco_ed = QLineEdit()
        self.cuenta_banca = QLineEdit()

        izq_lay_cliente.addWidget(nombre,0,0)
        izq_lay_cliente.addWidget(doc_identidad,1,0)
        izq_lay_cliente.addWidget(id_cliente,1,2)
        izq_lay_cliente.addWidget(trabajo,3,2)
        izq_lay_cliente.addWidget(banco,4,2)
        izq_lay_cliente.addWidget(cuenta_banca,5,2)
        izq_lay_cliente.addWidget(correo,2,0)
        izq_lay_cliente.addWidget(telefono,2,2)
        izq_lay_cliente.addWidget(dirrecion,3,0)
        izq_lay_cliente.addWidget(observacion,4,0)

        izq_lay_cliente.addWidget(self.nombre_cliente,0,1,1,3)
        izq_lay_cliente.addWidget(self.doc_identidad,1,1)
        izq_lay_cliente.addWidget(self.id_cliente,1,3)
        izq_lay_cliente.addWidget(self.trabajo_ed,3,3)
        izq_lay_cliente.addWidget(self.banco_ed,4,3)
        izq_lay_cliente.addWidget(self.cuenta_banca,5,3)
        izq_lay_cliente.addWidget(self.correo_cliente,2,1)
        izq_lay_cliente.addWidget(self.telefono_cliente,2,3)
        izq_lay_cliente.addWidget(self.direccion_cliente,3,1)
        izq_lay_cliente.addWidget(self.observaciones,4,1,2,1)

        referencias = QLabel ('Referencias')

        nombre_ref = QLabel('Nombre: ')
        telefono_ref = QLabel('Telefono: ')
        direccion_ref = QLabel('Relacion : ')

        self.nombre_ref = QLineEdit()
        self.telefono_ref = QLineEdit()
        self.relacion_ref = QLineEdit()

        der_lay_cliente.addWidget(referencias,0,1,1,2)
        der_lay_cliente.addWidget(nombre_ref,1,0)
        der_lay_cliente.addWidget(telefono_ref,2,0)
        der_lay_cliente.addWidget(direccion_ref,3,0)
        der_lay_cliente.addWidget(self.nombre_ref,1,1)
        der_lay_cliente.addWidget(self.telefono_ref,2,1)
        der_lay_cliente.addWidget(self.relacion_ref,3,1)

        self.guardar_cliente = QPushButton(' Guardar ',objectName='otros')
        self.actualizar_cliente = QPushButton(' Actualizar ',objectName='otros')
        self.borrar_cliente = QPushButton(' Borrar ',objectName='otros')
        bottom_lay_cliente.addStretch()
        bottom_lay_cliente.addWidget(self.guardar_cliente)
        bottom_lay_cliente.addWidget(self.actualizar_cliente)
        bottom_lay_cliente.addWidget(self.borrar_cliente)
        bottom_lay_cliente.addStretch()

    def insert_clientes(self):

        nombre= self.nombre_cliente.text()
        identidad=self.doc_identidad.text()
        id_reg = self.id_cliente.text()
        coreo= self.correo_cliente.text()
        telefono= self.telefono_cliente.text()
        address = self.direccion_cliente.text()
        observacion = self.observaciones.toPlainText()

        nombre_ref = self.nombre_ref.text()
        telefono_ref = self.telefono_ref.text()
        relacion_ref = self.relacion_ref.text()
        trabajo = self.trabajo_ed.text()
        banco = self.banco_ed.text()
        cuenta = self.cuenta_banca.text()
        values = (nombre,identidad,coreo,telefono,address,observacion,nombre_ref,telefono_ref,relacion_ref,trabajo,banco,cuenta)

        self.base_datos.insertar('clientes','nombre_cliente,identidad,correo,telefono,direccion,observacion,nombre_referencia,telefono_referencia,relacion,trabajo,banco,cuenta_bancaria',values)
        self.limpiar_campos_client()
        
    def limpiar_campos_client(self):
        self.nombre_cliente.clear()
        self.doc_identidad.clear()
        self.id_cliente.clear()
        self.correo_cliente.clear()
        self.telefono_cliente.clear()
        self.direccion_cliente.clear()
        self.observaciones.clear()

        self.nombre_ref.clear()
        self.telefono_ref.clear()
        self.relacion_ref.clear()
        self.banco_ed.clear()
        self.cuenta_banca.clear()
        self.trabajo_ed.clear()

    


class VerClientesPropios():
    def __init__(self):
        super(VerClientesPropios).__init__()

        self.base_datos = Comunicacion()

        self.client = VerClientesDatos()
        self.view_clientes()
        self.mostrar_clientes_tab()

    def view_clientes(self):
        
        self.general_clientes = QVBoxLayout()



        fr_buscar_clientes = QFrame()
        fr_tabla_clientes = QFrame()

        self.general_clientes.addWidget(fr_buscar_clientes)
        self.general_clientes.addWidget(fr_tabla_clientes)

        lay_buscar_clientes = QHBoxLayout()
        lay_tabla_clientes = QHBoxLayout()

        fr_buscar_clientes.setLayout(lay_buscar_clientes)
        fr_tabla_clientes.setLayout(lay_tabla_clientes)

        self.tabla_clientes_view = Tabla(['Id','Nombre','DIP/Pasaporte','correo','Telefono','Direccion'])
        lay_tabla_clientes.addWidget(self.tabla_clientes_view)
        self.buscar_clientes_view = QLineEdit()
        self.buscar_clientes_view.setPlaceholderText('Buscar clientes...')

        self.mostrar_todos = QPushButton('Mostrar Todos',objectName='otros')

        lay_buscar_clientes.addWidget(self.buscar_clientes_view)
        lay_buscar_clientes.addStretch()
        lay_buscar_clientes.addWidget(self.mostrar_todos)
        lay_buscar_clientes.addStretch()

        self.mostrar_todos.clicked.connect(self.mostrar_clientes)
        self.mostrar_todos.clicked.connect(self.mostrar_clientes_tab)
        self.buscar_clientes_view.textChanged.connect(self.mostrar_clientes_filtro)
        



    def mostrar_clientes(self):
        cliente = self.tabla_clientes_view
        mostrar_tabla = MostrarDatos_in(cliente)
        campos = 'id_cliente,nombre_cliente,identidad,correo,telefono,direccion'
        mostrar_tabla.addDataTable(campos,'clientes')


    def mostrar_clientes_tab(self):
        tabla=self.tabla_clientes_view
        datos_show= MostrarDatos_in(tabla)
        datos_show.addDataTable('id_cliente,nombre_cliente,identidad,correo,telefono,direccion','clientes')

    def mostrar_clientes_filtro(self):
        buscando = self.buscar_clientes_view.text()
        tabla=self.tabla_clientes_view
        datos_show= MostrarDatos_in(tabla)
        datos_show.addDataTableCondicion('id_cliente,nombre_cliente,identidad,correo,telefono,direccion','clientes','nombre_cliente',buscando)


    def select_item(self):
        
        tabla=self.tabla_clientes_view
        selected = SelecRow(tabla)
        valor = selected.obten_valor(0)
        datos=self.base_datos.filtro_select('id_cliente,nombre_cliente,identidad,correo,telefono,direccion,observacion,nombre_referencia,telefono_referencia,relacion,trabajo,banco,cuenta_bancaria','clientes','id_cliente',valor)
        
        return(datos)
    

