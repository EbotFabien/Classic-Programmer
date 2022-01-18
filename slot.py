import sys
from PyQt4.QtCore import *
from PyQt4 import QtGui
menu = QtGui.QMenu( "Menu ILG", iface.mainWindow().menuBar() )
actions = iface.mainWindow().menuBar().actions()
lastAction = actions[-2]
f=menu.addAction('k')
def appl_():
    app=QtGui.QApplication(sys.argv)
    app1=QtGui.QWidget
    app1.show
    app.exec_()
    
    

f.connect(f,SIGNAL("triggered()"),appl_)
iface.mainWindow().menuBar().insertMenu( lastAction, menu )
menu.exec_()
