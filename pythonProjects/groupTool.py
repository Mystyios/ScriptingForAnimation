import maya.cmds as cmds

selList = cmds.ls(selection=True)

for x in range (len(selList)): 
    objRot = cmds.xform(selList[x], rotation=True, q=True)
    objTrans = cmds.xform(selList[x], translation=True, q=True)
    cmds.xform(selList[x], rotation=[0,0,0], translation=[0,0,0])
    group = cmds.group(selList[x], name=f"{selList[x]}_Grp")
    cmds.xform(group, rotation=objRot, translation=objTrans)


