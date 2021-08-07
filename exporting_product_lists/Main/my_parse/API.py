

#from . import Mainwindowdes
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets

import sys

#from Mainwindowdes import Ui_MainWindow






class My_Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        #self.ui.menuGenel.addActions(""" ilgili diğer window yazılıcıcak  """)
        #self.ui.menuSe_enekler.addActions((""" ilgili diğer window yazılıcıcak  """)
        #self.ui.menuAlanlar_E_leme.addActions(""" ilgili diğer window yazılıcıcak  """)
        
        #self.ui.menuCategory_Mapping.addActions(""" ilgili diğer window yazılıcıcak  """)
        #self.ui.menuCron.addActions(""" ilgili diğer window yazılıcıcak  """)
        










#create()
#createWindowContainer(window)
#cursor()
#changeEvent(a0)
#connectNotify(signal)

#setContextMenuPolicy(policy)