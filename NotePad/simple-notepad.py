from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter
import os, sys



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.path = None
        
        MainWindow.setWindowTitle('Untitled - Notepad')
        MainWindow.resize(500,600)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setStyleSheet("background-color: WHITE;border: 1px solid black;")

        
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        
        self.plainTextEdite = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.gridLayout.addWidget(self.plainTextEdite, 0, 0, 1, 1)
        
        font = QtGui.QFontDatabase.systemFont(QtGui.QFontDatabase.FixedFont)
        font.setPointSize(10)
        self.plainTextEdite.setFont(font)
        self.plainTextEdite.setStyleSheet("color: BLACK;")
        
        
        
        #MenuBar_File
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0 , 0, 501, 21))
        self.menuFile = QtWidgets.QMenu('File', self.menubar)
        self.menuEdit = QtWidgets.QMenu('Edit', self.menubar)
        MainWindow.setMenuBar(self.menubar)
        # MenuBar Options_NEW_File
        self.actionNew = QtWidgets.QAction('New', MainWindow)
        self.actionNew.setShortcut('Ctrl+N')
        self.actionNew.triggered.connect(self.new_file)
        # MenuBar Options_OPEN_File
        self.actionOpen = QtWidgets.QAction('Open', MainWindow)
        self.actionOpen.setShortcut('Ctrl+O')
        self.actionOpen.triggered.connect(self.open_file)
        # MenuBar Options_SAVE_File
        self.actionSave = QtWidgets.QAction('Save', MainWindow)
        self.actionSave.setShortcut('Ctrl+S')
        self.actionSave.triggered.connect(self.save_file)
        # MenuBar Options_SAVE_AS_File
        self.actionSave_As = QtWidgets.QAction('Save As', MainWindow)
        self.actionSave_As.setShortcut('Ctrl+Shift+S')
        self.actionSave_As.triggered.connect(self.file_save_as)
        # MenuBar Options_Exit_File
        self.actionExit = QtWidgets.QAction('Exit', MainWindow)
        self.actionExit.setShortcut('Ctrl+Q')
        self.actionExit.triggered.connect(self.exit)
        # MenuBar Options_UNDO_Edit
        self.actionUndo = QtWidgets.QAction('Undo', MainWindow)
        self.actionUndo.setShortcut('Ctrl+Z')
        self.actionUndo.triggered.connect(self.plainTextEdite.undo)
        # MenuBar Options_REDO_Edit
        self.actionRedo = QtWidgets.QAction('Redo', MainWindow)
        self.actionRedo.setShortcut('Ctrl+Y')
        self.actionRedo.triggered.connect(self.plainTextEdite.redo)
        # MenuBar Options_CUT_Edit
        self.actionCut = QtWidgets.QAction('Cut', MainWindow)
        self.actionCut.setShortcut('Ctrl+X')
        self.actionCut.triggered.connect(self.plainTextEdite.cut)
        # MenuBar Options_COPY_Edit
        self.actionCopy = QtWidgets.QAction('Copy', MainWindow)
        self.actionCopy.setShortcut('Ctrl+C')
        self.actionCopy.triggered.connect(self.plainTextEdite.copy)
        # MenuBar Options_PASTE_Edit
        self.actionPaste= QtWidgets.QAction('Paste', MainWindow)
        self.actionPaste.setShortcut('Ctrl+V')
        self.actionPaste.triggered.connect(self.plainTextEdite.paste)
        # MenuBar Options_SELECT_ALL_Edit
        self.actionSelect_All = QtWidgets.QAction('Select All', MainWindow)
        self.actionSelect_All.setShortcut('Ctrl+A')
        self.actionSelect_All.triggered.connect(self.plainTextEdite.selectAll)
        
        #ADD Action
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSelect_All)
        self.menuEdit.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        
       

        
        
    def new_file(self):
        MainWindow.setWindowTitle('Untitled - Notepad')
        self.plainTextEdite.clear()
            
    def open_file(self):
        global path
        path, _= QtWidgets.QFileDialog.getOpenFileName(MainWindow, 'Open File', '', 'Text documents (*.txt)')
        if path == "":
            path = None
        else:
            self.path = path
            with open(path, 'r') as f:
                text = f.read()
                self.plainTextEdite.setPlainText(text)
                self.update_title()
                
    def update_title(self):
        MainWindow.setWindowTitle('%s - PyQt5 Notepade' %(os.path.basename(self.path) if self.path else 'Untitled' ))
        
    def save_file(self):
        global path
        if self.path is None:
            self.file_save_as()
        else:
            text = self.plainTextEdite.toPlainText()
            with open(path, 'w') as f:
                f.write(text)
    
    def file_save_as(self):
        path, _ = QtWidgets.QFileDialog.getSaveFileName(MainWindow, 'Save File', '', 'Text documents (*.txt)')
        
        if path == "":
            path = None
        else:
            self.path = path
            text = self.plainTextEdite.toPlainText()
            
            with open(path, 'w') as f:
                f.write(text)
            self.update_title()
    
    def exit(self):
        MainWindow.close()
        
    
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())            
        
        

        
        

