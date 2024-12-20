import sys
from PySide6.QtWidgets import QApplication,QMainWindow,QDialog, QVBoxLayout,QLabel,QFrame, QPushButton,QWidget
from PySide6.QtCore import Qt
import estilos

class Flotante(QDialog):
    def __init__(self,ancho:int,alto:int,titulo):
        '''recibe el tamaño, en alto,ancho, y la posicion.
        El Frame de uso para tu Layout personalizado se llama "self.fr_container"
        '''
        super().__init__()

        self.setGeometry(100,100,ancho,alto)

        self.center()
        css_content = estilos.obtener_estilos()
        self.setStyleSheet(css_content)

        self.root = QVBoxLayout(self,objectName='todo')
        self.root.setContentsMargins(0,0,0,0)

        self.titulo = QLabel (f'{titulo}', objectName='titulo_flotante')
        self.titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.titulo.mouseMoveEvent = self.mover_ventana
        self.root.addWidget(self.titulo)

        self.fr_container = QFrame(objectName='entradas')
        self.btn_cerrar_ven = QPushButton(objectName='cerrar_btn_pop')
        self.btn_cerrar_ven.setMaximumWidth(40)

        self.root.addWidget(self.fr_container,80)
        self.root.addWidget(self.btn_cerrar_ven,10)

        self.btn_cerrar_ven.clicked.connect(lambda:self.close())
        self.setWindowFlag(Qt.FramelessWindowHint)  

    def center(self):
            screen_geometry = QApplication.primaryScreen().geometry()
            x = (screen_geometry.width() - self.width()) //2
            y =(screen_geometry.height() - self.height()) //2
            self.move(x, y)


    def mover_ventana(self, event):
            if self.isFullScreen() ==False:
                self.move(self.pos()+ event.globalPosition().toPoint() - self.dragPos )
                self.dragPos = event.globalPosition().toPoint()
                event.accept()

    def Quitar_barra_title(self):
            self.setWindowFlag(Qt.FramelessWindowHint)
            #self.setWindowOpacity(0.90)

    def mousePressEvent(self, event):
            self.dragPos = event.globalPosition().toPoint()