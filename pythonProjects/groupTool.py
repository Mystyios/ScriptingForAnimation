import maya.cmds as cmds

selList = cmds.ls(selection=True)
currentIndex = 0

def group_Selection(control):
    conRot = cmds.xform(control, worldSpace=True, rotation=True, q=True)
    conTrans = cmds.xform(control, worldSpace=True, translation=True, q=True)
    group = cmds.group(empty=True, name=f"{control[0]}_Grp")
    cmds.xform(group, rotation=conRot, translation=conTrans)
    cmds.parent(control, group)

def create_Control(sel):
    objRot = cmds.xform(sel, worldSpace=True, rotation=True, q=True)
    objTrans = cmds.xform(sel, worldSpace=True, translation=True, q=True)

    if "_Jnt" in sel or "_Geo" in sel:
        txt = sel
        txt2 = (txt.rpartition('_')[0])
        txt2 = '%s_Ctrl' % txt2
        currentControl = cmds.circle(c=[0,0,0], nr=[1,0,0], sw=360, r=1, d=3, ut=0, tol=0.01, s=8, ch=1, name=txt2)
    else:
        currentControl = cmds.circle(c=[0,0,0], nr=[1,0,0], sw=360, r=1, d=3, ut=0, tol=0.01, s=8, ch=1, name=f"{sel}_Ctrl")
    

    cmds.xform(currentControl, rotation=objRot, translation=objTrans)
    cmds.select(currentControl)
    group_Selection(currentControl)


for i in selList:
    create_Control(selList[currentIndex])
    currentIndex += 1
