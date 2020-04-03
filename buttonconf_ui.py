from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMessageBox,QVBoxLayout,QCheckBox,QButtonGroup 
from PyQt5 import uic
import main
from helper import res_path,classlistToIds

class ButtonOptionsDialog(QDialog):
    def __init__(self,name,id, parent):
        self.id = id
        self.main = parent #type: main.MainUi
        QDialog.__init__(self, parent)
        uic.loadUi(res_path('buttonoptions.ui'), self)
        self.setWindowTitle(name)        
        self.connectItems()

    def showEvent(self,event):
        self.readValues()
    def readValues(self):
        request = "btnpol?"+str(self.id)+";btncut?"+str(self.id)+";btnnum?"+str(self.id)+";"
        print(request)
        invert,cutleft,num = [int(s) for s in self.main.serialGet(request).split("\n")]
        self.checkBox_invert.setChecked(invert==1)
        self.checkBox_cutleft.setChecked(cutleft==1)
        self.spinBox_btnnum.setValue(num)

    def connectItems(self):
        self.checkBox_invert.stateChanged.connect(lambda v : self.main.serialWrite("btnpol?"+str(self.id)+"="+str(v)+";"))
        self.checkBox_cutleft.stateChanged.connect(lambda v : self.main.serialWrite("btncut?"+str(self.id)+"="+str(v)+";"))
        self.spinBox_btnnum.valueChanged.connect(lambda v : self.main.serialWrite("btnnum?"+str(self.id)+"="+str(v)+";"))