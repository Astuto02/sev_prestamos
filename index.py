
from PySide6.QtWidgets import QMainWindow, QWidget,QVBoxLayout,QFrame,QHBoxLayout,QLabel,QGridLayout,QPushButton,QApplication
from PySide6.QtCore import Qt
import estilos
from PySide6.QtGui import QPixmap


class Prestamos(QMainWindow):
    def __init__(self):
        super().__init__()

        self.iniciar()
        css_content = estilos.obtener_estilos()
        self.setStyleSheet(css_content)

    def iniciar(self):
        '''funcion que inicializa la aplicacion le da forma'''
        self.setGeometry(100,20,1080,700)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.central_widget = QWidget(objectName= 'central')
        self.root = QVBoxLayout(objectName= 'central')
        self.root.setContentsMargins(0,0,0,0)
        self.central_widget.setLayout(self.root)
        self.setCentralWidget(self.central_widget)

        self.center()
        self.interno_top()
        self.interno_central()
        self.interno_bottom()

        self.fr_titulo.mouseMoveEvent = self.mover_ventana

    def interno_top(self):

        self.fr_titulo = QFrame()
        self.fr_titulo.setFixedHeight(50)
        self.lay_fr_titulo = QHBoxLayout()

        self.fr_titulo.setLayout(self.lay_fr_titulo)

        self.titulo = QLabel('SISTEMA DE PRESTAMO EXPRESS',objectName='titulo_principal')
        self.titulo.setAlignment(Qt.AlignCenter)
        self.mi_logo = QLabel()

        pixmap = QPixmap("img/mi_logo.ico")
        self.mi_logo.setPixmap(pixmap)
        self.mi_logo.setFixedSize(pixmap.size())
        self.lay_fr_titulo.addWidget(self.mi_logo)
        self.lay_fr_titulo.addWidget(self.titulo)

        self.root.addWidget(self.fr_titulo,10)



    def interno_central(self):

        self. fr_central = QFrame()
        self.main_layout= QHBoxLayout()

        self.fr_central.setLayout(self.main_layout)
        
        self.fr_central_izq = QFrame()
        self.fr_central_der = QFrame()

        self.lay_cent_izq = QGridLayout()
        self.lay_cent_der = QVBoxLayout()

        self.fr_central_izq.setLayout(self.lay_cent_izq)
        self.fr_central_der.setLayout(self.lay_cent_der)

        self.main_layout.addWidget(self.fr_central_izq,60)
        self.main_layout.addWidget(self.fr_central_der,40)

        self.logo = QLabel (objectName='img_pub')
        self.lay_cent_der.addWidget(self.logo)

        self.btn_prestamos = QPushButton('  Préstamo  ',objectName='btn_prestamo')
        self.btn_clientes = QPushButton('  Clientes  ',objectName='btn_clientes')
        self.btn_caja = QPushButton('  Caja  ',objectName='btn_caja')
        self.btn_ingresos = QPushButton('  Ingresos  ',objectName='btn_ingresos')
        self.btn_banco = QPushButton('  Banco  ',objectName='btn_banca')
        self.btn_movimientos = QPushButton('  Movimientos  ',objectName='btn_movi')

        self.lay_cent_izq.addWidget(self.btn_prestamos,0,0)
        self.lay_cent_izq.addWidget(self.btn_clientes,0,1)
        self.lay_cent_izq.addWidget(self.btn_caja,0,2)
        self.lay_cent_izq.addWidget(self.btn_ingresos,1,0)
        self.lay_cent_izq.addWidget(self.btn_banco,1,1)
        self.lay_cent_izq.addWidget(self.btn_movimientos,1,2)


        self.root.addWidget(self.fr_central,80)


    def interno_bottom(self):

        self.fr_bottom = QFrame(objectName='bottom')
        self.fr_bottom.setFixedWidth(700)
        self.lay_bot = QHBoxLayout()

        self.fr_bottom.setLayout(self.lay_bot)

        self.btn_salir = QPushButton(objectName='salir')
        self.btn_Actualizar = QPushButton('Actualizar',objectName='salir')
        self.btn_Usuarios = QPushButton(objectName='users')
        self.btn_Permisos = QPushButton(objectName='permisos')
        self.btn_BackUp = QPushButton(objectName='backup')
        self.btn_Ajustes = QPushButton(objectName='config')

        self.lay_bot.addWidget(self.btn_salir)
        #self.lay_bot.addWidget(self.btn_Actualizar)
        self.lay_bot.addWidget(self.btn_Usuarios)
        self.lay_bot.addWidget(self.btn_Permisos)
        self.lay_bot.addWidget(self.btn_BackUp)
        self.lay_bot.addWidget(self.btn_Ajustes)

        self.root.addWidget(self.fr_bottom)

        self.btn_salir.clicked.connect(lambda:self.close())



        
    def center(self):
        screen_geometry = QApplication.primaryScreen().geometry()
        x = (screen_geometry.width() - self.width()) //2
        y =(screen_geometry.height() - self.height()) //2
        self.move(x, y)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mover_ventana(self, event):
        if self.isFullScreen() ==False:
            self.move(self.pos()+ event.globalPosition().toPoint() - self.dragPos )
            self.dragPos = event.globalPosition().toPoint()
            event.accept()