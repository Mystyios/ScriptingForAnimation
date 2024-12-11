import maya.cmds as cmds
import change_Shape_Color

class ChangeColorUI():
    def __init__(self):
        self.mWindow = 'colorChangeWindow'

    def create(self):
        self.delete()

        self.mWindow = cmds.window(self.mWindow,
                                   title="Change Shape Color",
                                   widthHeight=(300,400),
                                   resizeToFitChildren=True)
        mColumn = cmds.columnLayout(parent=self.mWindow, adjustableColumn=True)
        cmds.textField(parent=mColumn, text="Select Color To Change To:", editable=False)
        self.ColorSlider = cmds.intSlider(parent=mColumn, minValue=0, maxValue=31, step=1, changeCommand=lambda *args: self.UpdateTextButton())
        self.IconTextButton = cmds.iconTextButton(parent=mColumn, width=55, bgc=[0.467, 0.467, 0.467])
        cmds.button(parent=mColumn, label="Change Color", command=lambda *args: self.CC_ButtonCmd())

        cmds.showWindow(self.mWindow)

    def delete(self):
        if (cmds.window(self.mWindow, exists=True)):
            cmds.deleteUI(self.mWindow)
    
    def UpdateTextButton(self):
        value = cmds.intSlider(self.ColorSlider, q=True, value=True)
        
        match value:
            case 0:
                cmds.iconTextButton(self.IconTextButton, e=True, bgc=[0.467, 0.467, 0.467])
            case 1:
                cmds.iconTextButton(self.IconTextButton, e=True, bgc=[0, 0, 0])
            case 2:
                cmds.iconTextButton(self.IconTextButton, e=True, bgc=[0.247, 0.247, 0.247])
            case 3:
                cmds.iconTextButton(self.IconTextButton, e=True, bgc=[0.498, 0.498, 0.498])
            case 4:
                cmds.iconTextButton(self.IconTextButton, e=True, bgc=[0.608, 0, 0.157])
            case 5:
                cmds.iconTextButton(self.IconTextButton, e=True, bgc=[0, 0.016, 0.373])
            case 6:
                cmds.iconTextButton(self.IconTextButton, e=True, bgc=[0, 0, 1])
            case 7:
                cmds.iconTextButton(self.IconTextButton, e=True, bgc=[0, 0.275, 0.094])
            case 8:
                cmds.iconTextButton(self.IconTextButton, e=True, bgc=[0.145, 0, 0.263])
            case 9:
                cmds.iconTextButton(self.IconTextButton, e=True, bgc=[0.78, 0, 0.78])
            case 10:
                cmds.iconTextButton(self.IconTextButton, e=True, bgc=[0.537, 0.278, 0.2])
            case 11:
                cmds.iconTextButton(self.IconTextButton, e=True, bgc=[0.243, 0.133, 0.122])
            case 12:
                cmds.iconTextButton(self.IconTextButton, e=True, bgc=[0.6, 0.145, 0])
            case 13:
                cmds.iconTextButton(self.IconTextButton, e=True, bgc=[1, 0, 0])
            case 14:
                cmds.iconTextButton(self.IconTextButton, e=True, bgc=[0, 1, 0])
            case 15:
                cmds.iconTextButton(self.IconTextButton, e=True, bgc=[0, 0.255, 0.6])
            case 16:
                cmds.iconTextButton(self.IconTextButton, e=True, bgc=[1, 1, 1])
            case 17:
                cmds.iconTextButton(self.IconTextButton, e=True, bgc=[1, 1, 0])
            case 18:
                cmds.iconTextButton(self.IconTextButton, e=True, bgc=[0.388, 0.863, 1])
            case 19:
                cmds.iconTextButton(self.IconTextButton, e=True, bgc=[0.263, 1, 0.635])
            case 20:
                cmds.iconTextButton(self.IconTextButton, e=True, bgc=[1, 0.686, 0.686])
            case 21:
                cmds.iconTextButton(self.IconTextButton, e=True, bgc=[0.89, 0.675, 0.475])
            case 22:
                cmds.iconTextButton(self.IconTextButton, e=True, bgc=[1, 1, 0.384])
            case 23:
                cmds.iconTextButton(self.IconTextButton, e=True, bgc=[0, 0.6, 0.325])
            case 24:
                cmds.iconTextButton(self.IconTextButton, e=True, bgc=[0.627, 0.412, 0.188])
            case 25:
                cmds.iconTextButton(self.IconTextButton, e=True, bgc=[0.62, 0.627, 0.188])
            case 26:
                cmds.iconTextButton(self.IconTextButton, e=True, bgc=[0.408, 0.627, 0.188])
            case 27:
                cmds.iconTextButton(self.IconTextButton, e=True, bgc=[0.188, 0.627, 0.365])
            case 28:
                cmds.iconTextButton(self.IconTextButton, e=True, bgc=[0.188, 0.627, 0.627])
            case 29:
                cmds.iconTextButton(self.IconTextButton, e=True, bgc=[0.188, 0.404, 0.627])
            case 30:
                cmds.iconTextButton(self.IconTextButton, e=True, bgc=[0.435, 0.188, 0.627])
            case 31:
                cmds.iconTextButton(self.IconTextButton, e=True, bgc=[0.631, 0.188, 0.412])
    
    def CC_ButtonCmd(self):
        value = cmds.intSlider(self.ColorSlider, q=True, value=True)
        change_Shape_Color.assign_Color(value)

#Use Instructions:
#Make sure the change_Shape_Color.py file is in the maya/scripts folder (I tested this using the maya/2024/scripts folder specifically)
#Select objects you want effected in your scene

#Run this code in the script editor:
#import Change_Color_UI

#myUI = Change_Color_UI.ChangeColorUI()
#myUI.create()