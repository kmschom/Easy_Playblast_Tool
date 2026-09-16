"""
Written by Kim Maglalang - Polyspawn https://www.youtube.com/channel/UCoP753pwrAjK6P3gcmZAHAw
Modified by Kelly Schombert
A PySide2 UI template to running your first UI in Maya.
Written for Python 3 and Maya 2020 and beyond.
"""
from maya import OpenMayaUI as omui
from maya import cmds
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance


class FirstToolUI(QWidget):

    def __init__(self, parent=None):
        super(FirstToolUI, self).__init__(parent)

        self.setWindowFlags(Qt.Window)

        # Set the object name     
        self.setObjectName('FirstToolUI_uniqueId')

        # Customize some window values
        self.setWindowTitle('Kellys Window')
        self.setGeometry(500, 500, 250, 150)

        # Add widgets to your window
        self.build_ui()
        self.connect_ui()

    def build_ui(self):
        vlayout = QVBoxLayout()
        self.setLayout(vlayout)
        self.playblast_button = QPushButton("Playblast", self)
        vlayout.addWidget(self.playblast_button)

    def connect_ui(self):
        self.playblast_button.clicked.connect(self.playblast_action)

    def playblast_action(self):
        listCameras = ['Quarter','Side','Front']
        for cam in listCameras:
            print("Playblasting from " + cam)
            cmds.lookThru(cam)
            filename = "C:/Users/kmsch/Downloads/EnemyStun_" + cam + ".avi"
            cmds.playblast(format="avi", filename=filename, sequenceTime=0, clearCache=1, viewer=0, showOrnaments=1, offScreen=1, fp=4, percent=100, compression="none", quality=100, widthHeight=[1280, 720], forceOverwrite=1)
        print("All done!")

def get_main_window():
    """Get the maya window pointer to parent this tool under."""
    ptr = omui.MQtUtil.mainWindow()
    # for Py3 use int() , for Py2 use long() , more info: https://docs.python.org/3/whatsnew/3.0.html#integers
    maya_window = wrapInstance(int(ptr), QWidget)
    return maya_window

# Get Maya's main window to parent to
maya_window = get_main_window()
tool = FirstToolUI(maya_window)
tool.show()
