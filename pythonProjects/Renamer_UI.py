import maya.cmds as cmds
import sequential_Renamer

class RenamerUI():
    def __init__(self):
        self.mWindow = 'renamerWindow'

    def create(self):
        self.delete()

        self.mWindow = cmds.window(self.mWindow,
                                   title="Sequential Renamer",
                                   widthHeight=(300,400),
                                   resizeToFitChildren=True)
        mColumn = cmds.columnLayout(parent=self.mWindow, adjustableColumn=True)
        self.RenameField = cmds.textField(parent=mColumn, placeholderText="Enter Rename Format")
        cmds.button(parent=mColumn, label="Rename Selection(s)", command=lambda *args: self.RN_ButtonCmd())

        cmds.showWindow(self.mWindow)

    def delete(self):
        if (cmds.window(self.mWindow, exists=True)):
            cmds.deleteUI(self.mWindow)
    
    def RN_ButtonCmd(self):
        format = cmds.textField(self.RenameField, q=True, text=True)
        sequential_Renamer.sequential_Renamer(format)

#Use Instructions:
#Make sure the sequential_Renamer file is in the maya/scripts folder (I tested this using the maya/2024/scripts folder specifically)
#Select objects you want effected in your scene

#Run this code in the script editor:
#import Renamer_UI

#myUI = Renamer_UI.RenamerUI()
#myUI.create()