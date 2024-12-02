import maya.cmds as cmds

def sequential_Renamer(string):
    prefix = string.partition('_')[0]
    suffix = string.rpartition('_')[-1]
    padCount = string.count('#')
    seqNum = 1
    selList = cmds.ls(selection=True)

    for selection in selList:
        padding = str(seqNum).zfill(padCount)
            
        cmds.rename(selection, f"{prefix}_{padding}_{suffix}")
        seqNum += 1

sequential_Renamer("Arm_##_Jnt")