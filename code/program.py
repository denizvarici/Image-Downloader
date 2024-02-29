from PyQt5 import QtWidgets
import sys
from MainWindow import Ui_MainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl

from image_puller import get_smallimage_url,get_linkimage_url,get_downloadimage_url

import requests

import time

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.image_box = [self.ui.img_1,self.ui.img_2,self.ui.img_3]
        self.show_urls = []
        self.real_urls= []
        self.download_urls= []

        self.ui.btnSearch.clicked.connect(lambda : self.set_image_from_url(self.image_box))
        
        
        
    def set_image_from_url(self,image_box):
        list.clear(self.show_urls)
        list.clear(self.real_urls)

        self.ui.btnImg_1.disconnect()
        self.ui.btnImg_2.disconnect()
        self.ui.btnImg_3.disconnect()


        self.show_urls = get_smallimage_url(self.ui.tbxKeyword.text())
        time.sleep(1)
        for i in range(0,3):
            image_data = requests.get(self.show_urls[i]).content
            self.applyImage(image_data,image_box[i])
            
            

        self.real_urls = get_linkimage_url(self.ui.tbxKeyword.text())
        time.sleep(1)
        self.ui.btnImg_1.clicked.connect(lambda: self.openURL(self.real_urls[0]))
        self.ui.btnImg_2.clicked.connect(lambda: self.openURL(self.real_urls[1]))
        self.ui.btnImg_3.clicked.connect(lambda: self.openURL(self.real_urls[2]))

        
        self.ui.btnDownload_1.clicked.connect(lambda: self.downloadImage(0))        
        self.ui.btnDownload_2.clicked.connect(lambda: self.downloadImage(1))        
        self.ui.btnDownload_3.clicked.connect(lambda: self.downloadImage(2))        

        
    def applyImage(self,image_data,label):
        pixmap = QPixmap()
        pixmap.loadFromData(image_data)
        
        # QLabel'ın boyutunu al
        label_size = label.size()
        
        # Resmi QLabel'ın boyutuna göre ölçekle
        scaled_pixmap = pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        
        # Ölçeklenmiş resmi QLabel'a ayarla
        label.setPixmap(scaled_pixmap)
        label.setAlignment(Qt.AlignCenter)

    def openURL(self,url):
        QDesktopServices.openUrl(QUrl(url))


    def downloadImage(self,btnIndex):
        get_downloadimage_url(self.real_urls[btnIndex])
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()
