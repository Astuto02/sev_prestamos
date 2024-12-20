

from PySide6.QtWidgets import QVBoxLayout,QFrame,QHBoxLayout,QLabel,QGridLayout,QPushButton,QLineEdit,QComboBox,QCheckBox,QWidget


from backend import Tabla,MostrarDatos_in,SelecRow,OperacionesMath

from bd_prestamos import Comunicacion
from flotante import Flotante
from PySide6.QtCore import Qt


class UserRegistration():
    def __init__(self):
        super().__init__()

        self.general_layout = QGridLayout()

        self.img_user = QLabel(objectName='user_img')
        self.img_user.setFixedHeight(80)
        self.img_user.setFixedWidth(150)
        self.img_user.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.nombre_completo = QLabel('Nombre Completo')
        self.correo = QLabel('E-Mail')
        self.nombre_usuario = QLabel('Nombre usuario')
        self.contraseña = QLabel('Contraseña')
        self.telefono = QLabel('Telefono')
        self.dip_pasaporte = QLabel('DIP/Pasaporte')
        self.domicil = QLabel('Domicilio')

        self.nombre_compl_entry = QLineEdit()
        self.correo_entry = QLineEdit()
        self.nom_user_entry = QLineEdit()
        self.contraseña_entry = QLineEdit()
        self.telefono_entry = QLineEdit()
        self.dip_pasaporte_entry = QLineEdit()
        self.domiclio_entry = QLineEdit()

        self.btn_save_user = QPushButton(' Guardar ',objectName='otros')

        self.general_layout.addWidget(self.img_user,0,0,1,2)

        self.general_layout.addWidget(self.nombre_completo,1,0)
        self.general_layout.addWidget(self.correo,2,0)
        self.general_layout.addWidget(self.nombre_usuario,3,0)
        self.general_layout.addWidget(self.contraseña,4,0)
        self.general_layout.addWidget(self.telefono,5,0)
        self.general_layout.addWidget(self.dip_pasaporte,6,0)
        self.general_layout.addWidget(self.domicil,7,0)

        self.general_layout.addWidget(self.nombre_compl_entry,1,1)
        self.general_layout.addWidget(self.correo_entry,2,1)
        self.general_layout.addWidget(self.nom_user_entry,3,1)
        self.general_layout.addWidget(self.contraseña_entry,4,1)
        self.general_layout.addWidget(self.telefono_entry,5,1)
        self.general_layout.addWidget(self.dip_pasaporte_entry,6,1)
        self.general_layout.addWidget(self.domiclio_entry,7,1)

        self.general_layout.addWidget(self.btn_save_user,8,0,1,2)

    def guardar_usuario(self):
        nombre = self.nombre_compl_entry.text()
        correo = self.correo_entry.text()
        user_name = self.nom_user_entry.text()
        password = self.contraseña_entry.text()
        telefono = self.telefono_entry.text()
        pasaporte = self.dip_pasaporte_entry.text()
        domicil = self.domiclio_entry.text()

        values = (nombre,correo,user_name,password,telefono,pasaporte,domicil)
        campos = 'nombre,correo,user_name,passwd,telefono,pasport,domicilio'
        self.base_datos = Comunicacion()
        self.base_datos.insertar('users',campos,values)
        self.limpiar_cajas()

    def limpiar_cajas(self):
        self.nombre_compl_entry.clear()
        self.correo_entry.clear()
        self.nom_user_entry.clear()
        self.contraseña_entry.clear()
        self.telefono_entry.clear()
        self.dip_pasaporte_entry.clear()
        self.domiclio_entry.clear()

        
class UserPermision():
    def __init__(self):
        super().__init__()


        self.general_layout = QVBoxLayout()


        self.buscar_usuario = QFrame()
        self.fr_permisos = QFrame()

        self.general_layout.addWidget(self.buscar_usuario)
        self.general_layout.addWidget(self.fr_permisos)

        self.buscando = QVBoxLayout()
        self.permision = QGridLayout()

        self.buscar_usuario.setLayout(self.buscando)
        self.fr_permisos.setLayout(self.permision)

        self.top_fr = QFrame()
        self.bottom_fr = QFrame()

        self.buscando.addWidget(self.top_fr,50) 
        self.buscando.addWidget(self.bottom_fr,50)
        self.lay_top = QHBoxLayout() 
        self.lay_bott = QHBoxLayout() 

        self.top_fr.setLayout(self.lay_top)
        self.bottom_fr.setLayout(self.lay_bott)

        self.line_id = QLineEdit()
        self.line_id.setReadOnly(True)
        self.line_id.setFixedWidth(30)

        self.line_nombre = QLineEdit()
        self.line_nombre.setReadOnly(True)

        self.btn_ver_user = QPushButton(objectName='ver_tabla_user')

        self.filtro_busqueda = QComboBox()
        self.filtro_busqueda.setPlaceholderText('Elije un nombre')
        self.filtro_busqueda.setFixedWidth(200)
        self.lay_top.addWidget(self.line_id)
        self.lay_top.addWidget(self.filtro_busqueda)
        self.lay_top.addWidget(self.btn_ver_user)
        self.lay_top.addStretch()



        ##########   los btones

        self.prestamo_chk = QCheckBox(text='Prestamo')
        self.clientes_chk= QCheckBox(text='Clientes')
        self.caja_chk = QCheckBox(text='Caja')
        self.banco_chk = QCheckBox(text='Banco')
        self.ingresos_chk = QCheckBox(text='Ingresos')
        self.movimiento_chk = QCheckBox(text='Movimientos')
        self.config_chk = QCheckBox(text='Configuracion')
        self.backup_chk = QCheckBox(text='Backup')
        self.permisos_chk = QCheckBox(text='Permisos')

        self.btn_aceptar = QPushButton(' Aceptar ')

        self.permision.addWidget(self.prestamo_chk,0,1)
        self.permision.addWidget(self.clientes_chk,1,1)
        self.permision.addWidget(self.caja_chk,2,1)

        self.permision.addWidget(self.banco_chk,0,3)
        self.permision.addWidget(self.ingresos_chk,1,3)
        self.permision.addWidget(self.movimiento_chk,2,3)

        self.permision.addWidget(self.config_chk,0,5)
        self.permision.addWidget(self.backup_chk,1,5)
        self.permision.addWidget(self.permisos_chk,2,5)

        self.permision.addWidget(self.btn_aceptar,3,2,3,2)






class Backups():
    def __init__(self):
        super().__init__()

        self.general_layout = QVBoxLayout()

        self.btn_crear_back = QPushButton('Crear BackUp')
        self.general_layout.addWidget(self.btn_crear_back)

    def back_todo(self):
        pass


from PySide6.QtGui import QPixmap
from io import BytesIO

class Settings():
    def __init__(self):
        super().__init__()

        self.base_datos = Comunicacion()
        self.general_layout = QVBoxLayout()

        self.frame_image = QFrame()
        self.frame_datos = QFrame()

        self.lay_imagen = QGridLayout()
        self.lay_datos = QGridLayout()

        self.frame_image.setLayout(self.lay_imagen)
        self.frame_datos.setLayout(self.lay_datos)

        self.general_layout.addWidget(self.frame_image,40)
        self.general_layout.addWidget(self.frame_datos,60)

        self.btn_select = QPushButton('Imagen ...')
        self.etiqueta_imagen = QLabel()
        self.etiqueta_imagen.setFixedSize(80,70)

        self.lay_imagen.addWidget(self.btn_select,0,0)
        self.lay_imagen.addWidget(self.etiqueta_imagen,0,1)


        self.nombre_emp = QLabel('Nombre Empresa: ')
        self.contacto_emp = QLabel('Contacto Empresa: ')
        self.direccion_emp = QLabel('Direccion Empresa: ')

        self.nombre_em_line = QLineEdit()
        self.contacto_em_line = QLineEdit()
        self.direccion_em_line = QLineEdit()

        self.btn_save_datos = QPushButton(' Guardar ')

        self.lay_datos.addWidget(self.nombre_emp,0,0)
        self.lay_datos.addWidget(self.contacto_emp,1,0)
        self.lay_datos.addWidget(self.direccion_emp,2,0)

        self.lay_datos.addWidget(self.nombre_em_line,0,1)
        self.lay_datos.addWidget(self.contacto_em_line,1,1)
        self.lay_datos.addWidget(self.direccion_em_line,2,1)

        self.lay_datos.addWidget(self.btn_save_datos,3,0,1,2)
    
    def obtener_imagen(self):

            conn = self.base_datos.config
            cursor = conn.cursor()
            cursor.execute("SELECT imagen from imagenes ORDER by id_imagen DESC limit 1")
            resultado = cursor.fetchone()[0]
            try:
                if resultado:
                    imagen_bytes = BytesIO(resultado)
                    with open("imagen_recuperada.png", "wb") as archivo:
                        archivo.write(imagen_bytes.getvalue())
                    return resultado
                else:
                    return None
            except Exception as e:
                print(f'Esta vacio {e}')


    def crear_ima(self):
        try:
            resultado = self.obtener_imagen()
            if resultado:
                pixmap = QPixmap()
                imagen_bytes = BytesIO(resultado)
                imagen= pixmap.loadFromData(imagen_bytes.read())
                return imagen
            else:
                return None
        except Exception as e:
            print(f'Esta vacio {e}')
        

    def imagen_logo(self):
        datos_imagen = self.obtener_imagen()
        if datos_imagen:
            pixmap = QPixmap()
            imagen_bytes = BytesIO(datos_imagen)
            pixmap.loadFromData(imagen_bytes.read())
            self.etiqueta_imagen.setPixmap(pixmap)
            self.etiqueta_imagen.setScaledContents(True)
            self.etiqueta_imagen.setFixedSize(pixmap.size())
        else:
            print('no hay imagen en la base de datos')

    def guardar_imagen_db(self,nombre,ruta):
        with open (ruta,'rb') as archivo:
            datos_imagen = archivo.read()
        conn = self.base_datos.config
        cursor = conn.cursor()
        cursor.execute(""" CREATE TABLE IF NOT EXISTS" imagenes" (
                "id_imagen"	INTEGER NOT NULL,
                "nombre"	TEXT,
                "imagen"	BLOB,
                PRIMARY KEY("id_imagen" AUTOINCREMENT)
            )""")
        
        cursor.execute("INSERT INTO imagenes (nombre,imagen) VALUES (?,?)",(nombre,datos_imagen))
        conn.commit()

    def crea_tabla_guardar(self):
        nombre = self.nombre_em_line.text()
        contacto = self.contacto_em_line.text()
        direccion = self.direccion_em_line.text()
        conn = self.base_datos.config
        cursor = conn.cursor()
        cursor.execute(""" CREATE TABLE IF NOT EXISTS "empresa" (
                "id_empresa"	INTEGER NOT NULL,
                "nombre_empresa"	TEXT,
                "contacto"	TEXT,
                "direccion"	TEXT,
                PRIMARY KEY("id_empresa" AUTOINCREMENT))
            """)
        cursor.execute("INSERT INTO empresa (nombre_empresa,contacto,direccion) VALUES (?,?,?)",(nombre,contacto,direccion))
        conn.commit()

    def limpiar(self):
        self.nombre_em_line.clear()
        self.contacto_em_line.clear()
        self.direccion_em_line.clear()


    
class UserUpdate(UserPermision):
    def __init__(self):
        super().__init__()

        self.general_layout = QGridLayout()

        self.img_user = QLabel(objectName='user_img')
        self.img_user.setFixedHeight(80)
        self.img_user.setFixedWidth(150)
        self.img_user.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.nombre_completo = QLabel('Nombre Completo')
        self.correo = QLabel('E-Mail')
        self.nombre_usuario = QLabel('Nombre usuario')
        self.contraseña = QLabel('Contraseña')
        self.telefono = QLabel('Telefono')
        self.dip_pasaporte = QLabel('DIP/Pasaporte')
        self.domicil = QLabel('Domicilio')

        self.nombre_compl_entry = QLineEdit()
        self.correo_entry = QLineEdit()
        self.nom_user_entry = QLineEdit()
        self.contraseña_entry = QLineEdit()
        self.telefono_entry = QLineEdit()
        self.dip_pasaporte_entry = QLineEdit()
        self.domiclio_entry = QLineEdit()

        self.btn_update_user = QPushButton(' Actualizar ',objectName='otros')

        self.general_layout.addWidget(self.img_user,0,0,1,2)

        self.general_layout.addWidget(self.nombre_completo,1,0)
        self.general_layout.addWidget(self.correo,2,0)
        self.general_layout.addWidget(self.nombre_usuario,3,0)
        self.general_layout.addWidget(self.contraseña,4,0)
        self.general_layout.addWidget(self.telefono,5,0)
        self.general_layout.addWidget(self.dip_pasaporte,6,0)
        self.general_layout.addWidget(self.domicil,7,0)

        self.general_layout.addWidget(self.nombre_compl_entry,1,1)
        self.general_layout.addWidget(self.correo_entry,2,1)
        self.general_layout.addWidget(self.nom_user_entry,3,1)
        self.general_layout.addWidget(self.contraseña_entry,4,1)
        self.general_layout.addWidget(self.telefono_entry,5,1)
        self.general_layout.addWidget(self.dip_pasaporte_entry,6,1)
        self.general_layout.addWidget(self.domiclio_entry,7,1)

        self.general_layout.addWidget(self.btn_update_user,8,0,1,2)

    def acualizar_usuario(self,id_user):
        
        nombre = self.nombre_compl_entry.text()
        correo = self.correo_entry.text()
        user_name = self.nom_user_entry.text()
        password = self.contraseña_entry.text()
        telefono = self.telefono_entry.text()
        pasaporte = self.dip_pasaporte_entry.text()
        domicil = self.domiclio_entry.text()

        values = (nombre,correo,user_name,password,telefono,pasaporte,domicil)
        campos = 'nombre,correo,user_name,passwd,telefono,pasport,domicilio'
        self.base_datos = Comunicacion()
        datos = f'nombre="{nombre}",correo="{correo}",user_name="{user_name}",passwd="{password}",telefono="{telefono}",pasport="{pasaporte}",domicilio="{domicil}"'
        self.base_datos.update_multiple('users',datos,'id_users',id_user)
        self.limpiar_cajas()

    def limpiar_cajas(self):
        self.nombre_compl_entry.clear()
        self.correo_entry.clear()
        self.nom_user_entry.clear()
        self.contraseña_entry.clear()
        self.telefono_entry.clear()
        self.dip_pasaporte_entry.clear()
        self.domiclio_entry.clear()

