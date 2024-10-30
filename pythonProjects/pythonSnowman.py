import maya.cmds as cmds

#Create Bottom Sphere
cmds.polySphere(radius=3, subdivisionsX=20, subdivisionsY=20, axis=[0, 1, 0])
cmds.xform(translation=[0,3,0])

#Create Middle Sphere
cmds.polySphere(radius=2, subdivisionsX=20, subdivisionsY=20, axis=[0, 1, 0])
cmds.xform(translation=[0,7,0])

#Create Head Sphere
cmds.polySphere(radius=1, subdivisionsX=20, subdivisionsY=20, axis=[0, 1, 0])
cmds.xform(translation=[0,9.5,0])

#Create Right and Left Eyes
cmds.polySphere(radius=0.189, subdivisionsX=20, subdivisionsY=20, axis=[0, 1, 0])
cmds.xform(translation=[-0.3,9.839,0.826])
cmds.polySphere(radius=0.189, subdivisionsX=20, subdivisionsY=20, axis=[0, 1, 0])
cmds.xform(translation=[0.3,9.839,0.826])

#Create Nose
cmds.polyCone(radius=0.154, height=1, subdivisionsX=20, subdivisionsY=1, subdivisionsZ=0, axis=[0, 1, 0])
cmds.xform(translation=[0, 9.555, 1.122], rotation=[92.165, 0, 0])

#Create Mouth
cmds.polySphere(radius=0.153, subdivisionsX=20, subdivisionsY=20, axis=[0, 1, 0])
cmds.xform(translation=[-0.347, 9.31, 0.844])
cmds.polySphere(radius=0.153, subdivisionsX=20, subdivisionsY=20, axis=[0, 1, 0])
cmds.xform(translation=[0.347, 9.31, 0.844])
cmds.polySphere(radius=0.153, subdivisionsX=20, subdivisionsY=20, axis=[0, 1, 0])
cmds.xform(translation=[-0.136, 9.171, 0.844])
cmds.polySphere(radius=0.153, subdivisionsX=20, subdivisionsY=20, axis=[0, 1, 0])
cmds.xform(translation=[0.136, 9.171, 0.844])

#Create Right Arm
cmds.polyCylinder(radius=0.071, height=3, subdivisionsX=20, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0])
cmds.xform(translation=[-2.772, 7.477, 0], rotation=[0, 0, -61.014])

#Create Left Arm
cmds.polyCylinder(radius=0.071, height=3, subdivisionsX=20, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0])
cmds.xform(translation=[2.772, 7.477, 0], rotation=[0, 0, 61.014])

#Create Hat
cmds.polyTorus()
cmds.xform(translation=[0, 10.403, 0], scale=[0.619, 0.619, 0.619])
cmds.polyCylinder(radius=0.569, height=1)
cmds.xform(translation=[0, 11.191, 0])