import maya.cmds as cmds

def sequential_Renamer(string):
    if string.count('_') > 2:
        prefix1, temp = string.partition('_')[0], string.partition("_")[2]
        prefix2 = temp.partition('_')[0]
        prefix = f"{prefix1}_{prefix2}"
    else:
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