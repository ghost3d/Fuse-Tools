'''
Created on Aug 14, 2014

@author: aldoruggiero
'''
import os
 
import pysideuic
import xml.etree.ElementTree as xml
from cStringIO import StringIO
 
import maya.cmds as cmds
import maya.OpenMayaUI as mui
import maya.mel as mel
 
import shiboken
import sys
from PySide.QtCore import QFile, SIGNAL, Qt,QCoreApplication
from PySide.QtGui import QBrush,QDialog,QListWidget, QApplication,QFileDialog,QPushButton,QLineEdit,QLabel,QRadioButton,QComboBox,QProgressBar,QPlainTextEdit,QMessageBox,QToolTip,QFont,QMainWindow
from PySide.QtUiTools import QUiLoader
try:
    #sys.path.remove('S:/outfit/artists/Aldo/00-WORKSPACES/GITeclipseSharedWorkspace/scenetoolmysql/CGPythonPipelineToolsMySQL/src/root/floatingMainInterface/')
	sys.path.remove('S:/outfit/shared/pythonPipeline/CGPythonPipelineToolsMySQL/src/root/floatingMainInterface/')
except:
        pass
for i in sys.path:
        print i
import sys
 
# uiFile = "S:/outfit/artists/Aldo/00-WORKSPACES/GITeclipseSharedWorkspace/scenetoolmysql/CGPythonPipelineToolsMySQL/src/root/floatingMainInterface/ui/shotSetUp23.ui"
#sys.path.append('S:/outfit/artists/Aldo/00-WORKSPACES/GITeclipseSharedWorkspace/scenetoolmysql/CGPythonPipelineToolsMySQL/src/root/floatingMainInterface/')
sys.path.append('S:/outfit/shared/pythonPipeline/CGPythonPipelineToolsMySQL/src/root/floatingMainInterface/')
from mainMySQL import *
 
from maya import OpenMayaUI as omui 
from PySide.QtCore import * 
from PySide.QtGui import * 
from shiboken import wrapInstance 

mayaMainWindowPtr = omui.MQtUtil.mainWindow() 
mayaMainWindow= wrapInstance(long(mayaMainWindowPtr), QWidget) 
 
filename = os.path.basename(cmds.file(q= True, sn = True))
            
def run():
    global my_window
    try:
        my_window.close()
        my_window.deleteLater()
    except: pass
    my_window = PySideSceneToolv002(parent = mayaMainWindow)
    my_window.setWindowTitle('%s'%(filename))
    my_window.setWindowFlags(Qt.Window)
    my_window.show()
    

run()
