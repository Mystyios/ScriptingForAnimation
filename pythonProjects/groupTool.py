import maya.cmds as cmds

#Creates group for the current control and matches transform and rotation
def group_Selection(control):
    conRot = cmds.xform(control, worldSpace=True, rotation=True, q=True)
    conTrans = cmds.xform(control, worldSpace=True, translation=True, q=True)
    group = cmds.group(empty=True, world=True, name=f"{control}_Grp")
    cmds.xform(group, rotation=conRot, translation=conTrans)
    cmds.parent(control, group)

#Creates Control circle and moves it to the position of selected object
def create_Control():
    selList = cmds.ls(selection=True)
    for sel in selList:
        objRot = cmds.xform(sel, worldSpace=True, rotation=True, q=True)
        objTrans = cmds.xform(sel, worldSpace=True, translation=True, q=True)

        #Check for _Jnt and _Geo suffix and swaps with _Ctrl
        if "_Jnt" in sel or "_Geo" in sel:
            txt = sel
            txt2 = (txt.rpartition('_')[0])
            txt2 = '%s_Ctrl' % txt2
            currentControl = cmds.circle(c=[0,0,0], nr=[1,0,0], sw=360, r=1, d=3, ut=0, tol=0.01, s=8, ch=1, name=txt2)[0]
        else:
            currentControl = cmds.circle(c=[0,0,0], nr=[1,0,0], sw=360, r=1, d=3, ut=0, tol=0.01, s=8, ch=1, name=f"{sel}_Ctrl")[0]
        

        cmds.xform(currentControl, rotation=objRot, translation=objTrans)
        cmds.select(currentControl)
        group_Selection(currentControl)

create_Control()

#To use: select objects in maya and run code
