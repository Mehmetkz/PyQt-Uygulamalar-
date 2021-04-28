# uygulamanın çıkış durumunu ele alır.
import sys

# Gerekli olan PyQt5 kütüphaneleri
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

# QApplication nesnesi, komut satırı argümanı liste içerir.
# PyQt5 Merhaba Uygulaması

uygulama = QApplication(sys.argv)

# Grafik arayüzü
window = QWidget()
window.setWindowTitle('PyQt5 Merhaba')
window.setGeometry(100,100,480,200)
window.move(60,15)
window.resize(300,300)
helloMsg = QLabel('<h1> Merhaba <h1>',parent=window)
helloMsg.move(60,15)
# window nesnesi uygulama penceresi oluşturmak için geçerli Qwidget örneğidir.
# Uygulama penceresi için başlık setWindowTitle komutu ile sağlanır.
# Set geometry komutunun ilk iki parametresi x ve y kordinatlarını içerir.
# Diğer iki parametre ise pencerenin yükseklik ve genişliğidir. Qlabel nesnesi
# pencerede mesaj yayınlamayı sağlar ve HTML komutlarını alabilir. (<h1>) Son
# olarak move komutu uygulama penceresini belirlenen koordinatlara taşımayı sağlar.
window.show()
sys.exit(uygulama.exec_())
# show komutu uygulama arayüzünü göstermeyi sağlar. xx.exec komutu uygulamayı başlatır.

# PyQt Bilgi kutusu uygulaması

from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout

class bilgi(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Bilgi Kutusu")
        dLayout = QVBoxLayout()
        fLayout = QFormLayout()
        fLayout.addRow('isim: ',QLineEdit())
        fLayout.addRow('yas: ',QLineEdit())
        fLayout.addRow('meslek: ',QLineEdit())
        fLayout.addRow('ulke: ',QLineEdit())
        dLayout.addLayout(fLayout)
        buton = QDialogButtonBox()
        buton.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        dLayout.addWidget(buton)
        self.setLayout(dLayout)

    if __name__ == '__main__': # Program ana dosya tarafından çalıştırıldı -> print(__name__)
        uygulama = QApplication(sys.argv)
        d = bilgi()
        d.show()
        sys.exit(uygulama.exec_())

# __name__ == '__main__ ifadesi programa iki işlec sağlar. Birincisi doğrudan program içerisinde
# çalıştırılır. İkincisi modül kullanarak çalıştırılır.

# QMain Window

from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar

class sekme(QMainWindow):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setWindowTitle("Yeni Sekme")
        self.setCentralWidget(QLabel("Merkez widget"))
        self.Menu()
        self.ToolBar()
        self.StatusBar()

    def Menu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction('&Exit',self.close)

    def ToolBar(self):
        tool = QToolBar()
        self.addToolBar(tool)
        tool.addAction('Exit',self.close)

    def StatusBar(self):
        gosterge = QStatusBar()
        gosterge.showMessage("Durum Cubugu")
        self.setStatusBar(gosterge)

if __name__ == '__main__':
    uygulama3 = QApplication(sys.argv)
    pencere = sekme()
    pencere.show()
    sys.exit(uygulama3.exec_())

################################################
#
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

def selam():
    if mesaj.text():
        mesaj.setText("")
    else:
        mesaj.setText("Merhaba Ptyhon")

def haber():
    if mesaj.text():
        mesaj.setText("Bugün çarşamba")
    else:
        mesaj.setText("")

uygulama4 = QApplication(sys.argv)
sekme = QWidget()
sekme.setWindowTitle('Uygulama penceresi')
sekme.setGeometry(100,100,480,200)
layout = QVBoxLayout()

buton = QPushButton('merhaba')
buton.setGeometry(100,100,40,40)
buton2 = QPushButton('ben Coco!!')
buton2.setGeometry(0,0,40,40)
buton.clicked.connect(selam)
buton2.clicked.connect(haber)

dLayout = QVBoxLayout()
fLayout = QFormLayout()
fLayout.addRow('isim: ',QLineEdit())
fLayout.addRow('yas: ',QLineEdit())
fLayout.addRow('meslek: ',QLineEdit())
fLayout.addRow('ulke: ',QLineEdit())
dLayout.addLayout(fLayout)

buton = QDialogButtonBox()
buton.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
dLayout.addWidget(buton)

dLayout.addWidget()
layout.addWidget(buton)
layout.addWidget(buton2)
mesaj = QLabel(' ')
layout.addWidget(mesaj)
sekme.setLayout(layout)
sekme.show()
sys.exit(uygulama4.exec_())
