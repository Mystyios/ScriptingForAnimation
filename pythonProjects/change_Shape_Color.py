import maya.cmds as cmds

def assign_Color(colNum):
    if 0 <= colNum <= 31:
        selList = cmds.ls(selection=True)

        for selection in selList:
            shape_node = cmds.listRelatives(selection, shapes=True)
            cmds.setAttr(f"{shape_node[0]}.overrideEnabled", 1)
            cmds.setAttr(f"{shape_node[0]}.overrideColor", colNum)
    else:
        print("Please Use A Number Between 0-31")

#assign_Color(-1)