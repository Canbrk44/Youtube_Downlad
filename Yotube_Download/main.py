# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 23:07:45 2022

@author: Smurf
"""

#------------------Youtube Download----------------------#
#--------------------------------------------------------#
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from youtube import *
import pytube
import os
from hakkında import *

#------------------Application---------------------------#
#--------------------------------------------------------#
Uygulama=QApplication(sys.argv)
penAna=QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(penAna)
penAna.show()


penHakkinda=QDialog()
ui2=Ui_Dialog()
ui2.setupUi(penHakkinda)
#------------------Linki Al------------------------------#
#--------------------------------------------------------#


def indir():
    try:
        link = ui.line_link.text()
        yt = pytube.YouTube(link)
        yt.streams.filter(file_extension='mp4').first().download("indirilenler")
        ui.statusbar.showMessage("İnderme Tamamlandı")
        baslık = yt.title
        ui.label_dest.setText(baslık)
    except Exception as Hata: 
       ui.statusbar.showMessage("İndirme Tamamlanamadı")
       

def locations():
    if not os.path.exists ("indirilenler"):
        os.mkdir("indirilenler")
        os.startfile(os.getcwd()+"\indirilenler")
    else:
        os.startfile(os.getcwd()+"\indirilenler")




def Hakkında():
    penHakkinda.show()
#------------------Button--------------------------------#
#--------------------------------------------------------#
ui.button_indir.clicked.connect(indir)
ui.button_location.clicked.connect(locations)
ui.actionHakk_nda.triggered.connect(Hakkında)

sys.exit(Uygulama.exec_())
